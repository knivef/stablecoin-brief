"""News items for the weekly brief and the Notion News Tracker.

    python3 scripts/news.py check  --file editions/2026-10-26-weekly/news.json
    python3 scripts/news.py render --file editions/2026-10-26-weekly/news.json [--jobs editions/.../jobs.json]
    python3 scripts/news.py lint   --draft editions/2026-10-26-weekly/draft.md
    python3 scripts/news.py push   --file editions/2026-10-26-weekly/news.json [--dry-run]

check validates every item (20-word cap, one link, fields, window) and looks
for duplicates in the News Tracker and across every past edition. render prints
the categorized sections for the draft. lint re-checks the finished draft. push
writes the items to the News Tracker, skipping any already there.
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import notion_api as n
from setup_notion import NEWS, REGIONS, SECTORS

TYPES = [o["name"] for o in NEWS["Type"]["select"]["options"]]
ROUNDS = [o["name"] for o in NEWS["Round"]["select"]["options"]]
SECTIONS = [
    ("Fundraise", "💰 FUNDRAISING"),
    ("M&A", "🤝 M&A"),
    ("People move", "🔄 PEOPLE MOVES"),
    ("Regulation & licensing", "⚖️ REGULATION & LICENSING"),
    ("Launch", "🚀 LAUNCHES"),
    ("Partnership", "🔗 PARTNERSHIPS"),
    ("Layoffs & shutdowns", "📉 LAYOFFS & SHUTDOWNS"),
    ("Other", "📌 ALSO NOTABLE"),
]
TIERS = [(25, "$25M+"), (5, "$5M to $25M"), (0, "Under $5M")]
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
BAD_ANCHOR = re.compile(r"^(here|this|report|announced|link|source|read more)$", re.I)
DASHES = re.compile(r"[—–]| -- |--")
EDITIONS = n.REPO / "editions"


def words(markdown):
    return len(LINK.sub(r"\1", markdown).replace("**", "").split())


def load(path):
    data = json.loads(Path(path).read_text())
    for item in data["items"]:
        item.setdefault("in_edition", True)
    return data


def problems(item, window):
    out, warn = [], []
    for field in ("company", "type", "date", "summary", "source"):
        if not item.get(field):
            out.append("missing %s" % field)
    if item.get("type") and item["type"] not in TYPES:
        out.append("type %r not in %s" % (item["type"], TYPES))
    if item.get("round") and item["round"] not in ROUNDS:
        out.append("round %r not in %s" % (item["round"], ROUNDS))
    if item.get("sector") and item["sector"] not in SECTORS:
        out.append("sector %r not in Sector options" % item["sector"])
    if item.get("region") and item["region"] not in REGIONS:
        out.append("region %r not in %s" % (item["region"], REGIONS))
    summary = item.get("summary", "")
    if words(summary) > 20:
        out.append("summary is %d words (max 20)" % words(summary))
    links = LINK.findall(summary)
    if len(links) != 1:
        out.append("summary needs exactly one [anchor](url) link, has %d" % len(links))
    for anchor, _ in links:
        if BAD_ANCHOR.match(anchor.strip()):
            out.append("weak link anchor %r" % anchor)
    if DASHES.search(summary):
        out.append("dash in summary (no em dashes, en dashes or --)")
    if item.get("type") == "Fundraise" and item.get("amount_musd") is None:
        warn.append("no amount_musd: renders under Undisclosed, so only if the amount really wasn't disclosed")
    if item.get("type") == "People move" and not item.get("person"):
        warn.append("people move without person")
    if item.get("date") and window and not (window["start"] <= item["date"] <= window["end"]):
        warn.append("date %s is outside the window %s to %s" % (item["date"], window["start"], window["end"]))
    return out, warn


def whole_name(name):
    """Match a company name as a whole word, so "Rain" doesn't match "Ukraine"."""
    return re.compile(r"(?<!\w)%s(?!\w)" % re.escape(name), re.I)


def archive_hits(term, exclude):
    hits = []
    pattern = whole_name(term)
    for path in sorted(EDITIONS.glob("*/*.md")):
        if path.parent.name == exclude:
            continue
        if pattern.search(path.read_text(errors="ignore")):
            hits.append("%s/%s" % (path.parent.name, path.name))
    return hits


def tracked(company):
    ds = n.config()["news"]["data_source_id"]
    same = whole_name(company)
    rows = []
    for page in n.query(ds, {"property": "Company", "title": {"contains": company}}):
        p = page["properties"]
        if not same.search(n.plain(p["Company"])):
            continue
        rows.append({"date": n.plain(p["Date"]), "type": n.plain(p["Type"]), "summary": n.plain(p["Summary"]),
                     "source": p["Source"]["url"] or "", "company": n.plain(p["Company"])})
    return rows


def stats(items, jobs_file=None):
    live = [i for i in items if i["in_edition"]]
    raises = [i for i in live if i["type"] == "Fundraise"]
    total = sum(i.get("amount_musd") or 0 for i in raises)
    count = lambda t: sum(1 for i in live if i["type"] == t)
    parts = ["%d raises totalling $%sM" % (len(raises), ("%.1f" % total).rstrip("0").rstrip("."))]
    if raises:
        top = max(raises, key=lambda i: i.get("amount_musd") or 0)
        if top.get("amount_musd"):
            parts.append("biggest: %s $%sM" % (top["company"], ("%.1f" % top["amount_musd"]).rstrip("0").rstrip(".")))
    parts += ["%d M&A" % count("M&A"), "%d people moves" % count("People move"),
              "%d regulation/licensing" % count("Regulation & licensing"), "%d launches" % count("Launch"),
              "%d partnerships" % count("Partnership")]
    if jobs_file:
        parts.append("%d new roles tracked" % len(json.loads(Path(jobs_file).read_text())["new"]))
    return "; ".join(parts)


def check(args):
    data = load(args.file)
    window, edition = data.get("window"), Path(args.file).resolve().parent.name
    errors = 0
    seen = {}
    for idx, item in enumerate(data["items"], 1):
        label = "%d. %s [%s]" % (idx, item.get("company", "?"), item.get("type", "?"))
        bad, warn = problems(item, window)
        key = (item.get("company", "").lower(), item.get("type"))
        if key in seen:
            bad.append("same company and type as item %d" % seen[key])
        seen[key] = idx
        notes = []
        if not args.offline and item.get("company"):
            for row in tracked(item["company"]):
                same_source = row["source"] and row["source"] == item.get("source")
                recent = row["date"] and item.get("date") and abs(
                    (datetime.date.fromisoformat(row["date"]) - datetime.date.fromisoformat(item["date"])).days) <= 90
                if same_source or (row["type"] == item.get("type") and recent):
                    bad.append("LIKELY DUPLICATE in News Tracker: %s %s %s" % (row["date"], row["type"], row["summary"]))
                else:
                    notes.append("tracked before: %s %s %s" % (row["date"], row["type"], row["summary"][:90]))
        hits = archive_hits(item.get("company", ""), edition) if item.get("company") else []
        if hits:
            notes.append("named in past editions: %s" % ", ".join(hits[-6:]) + (" (+%d more)" % (len(hits) - 6) if len(hits) > 6 else ""))
        if bad or warn or notes:
            print(label)
            for b in bad:
                print("   ERROR  " + b)
            for w in warn:
                print("   warn   " + w)
            for x in notes:
                print("   info   " + x)
        errors += len(bad)
    print("\n%d items, %d errors" % (len(data["items"]), errors))
    print("Week in numbers: " + stats(data["items"]))
    return 1 if errors else 0


def bullet(item):
    summary = item["summary"]
    company = item["company"]
    if summary.startswith(company):
        summary = "**%s**%s" % (company, summary[len(company):])
    return "- " + summary


def render(args):
    items = [i for i in load(args.file)["items"] if i["in_edition"]]
    out = []
    for kind, header in SECTIONS:
        group = [i for i in items if i["type"] == kind]
        if not group:
            continue
        out.append("**%s**\n" % header)
        if kind == "Fundraise":
            disclosed = sorted([i for i in group if i.get("amount_musd")], key=lambda i: -i["amount_musd"])
            for floor, label in TIERS:
                tier = [i for i in disclosed if i["amount_musd"] >= floor and
                        all(i["amount_musd"] < f for f, _ in TIERS if f > floor)]
                if tier:
                    out.append("*%s*\n" % label)
                    out.extend(bullet(i) for i in tier)
                    out.append("")
            undisclosed = [i for i in group if not i.get("amount_musd")]
            if undisclosed:
                out.append("*Undisclosed*\n")
                out.extend(bullet(i) for i in undisclosed)
                out.append("")
        else:
            out.extend(bullet(i) for i in group)
            out.append("")
    print("\n".join(out).rstrip())
    print("\n<!-- Week in numbers: %s -->" % stats(items, args.jobs))


def lint(args):
    text = Path(args.draft).read_text()
    issues = []
    for no, line in enumerate(text.splitlines(), 1):
        if DASHES.search(line) and not line.strip().startswith(("[SPONSOR", "---")):
            issues.append("line %d: dash: %s" % (no, line.strip()[:80]))
        for anchor, _ in LINK.findall(line):
            if BAD_ANCHOR.match(anchor.strip()):
                issues.append("line %d: weak link anchor %r" % (no, anchor))
        if re.search(r"(?<!\()https?://\S+", LINK.sub("", line)):
            issues.append("line %d: bare URL" % no)
        if line.lstrip().startswith("- ") and words(line.lstrip()[2:]) > 20:
            issues.append("line %d: bullet is %d words (max 20): %s" % (no, words(line.lstrip()[2:]), line.strip()[:70]))
    for issue in issues:
        print(issue)
    print("%d issues" % len(issues))
    return 1 if issues else 0


def push(args):
    data = load(args.file)
    ds = n.config()["news"]["data_source_id"]
    added = skipped = 0
    for item in data["items"]:
        bad, _ = problems(item, None)
        if bad:
            print("  NOT PUSHED %s: %s" % (item.get("company"), "; ".join(bad)))
            continue
        rows = tracked(item["company"])
        if any(r["source"] == item["source"] or (r["type"] == item["type"] and r["date"] == item["date"]) for r in rows):
            skipped += 1
            continue
        props = {
            "Company": n.title(item["company"]),
            "Date": n.date(item["date"]),
            "Week": n.select(n.iso_week(item["date"])),
            "Type": n.select(item["type"]),
            "Round": n.select(item.get("round")),
            "Amount ($M)": n.number(item.get("amount_musd")),
            "Valuation ($M)": n.number(item.get("valuation_musd")),
            "Lead investors": n.multi(item.get("lead_investors")),
            "Other investors": n.multi(item.get("other_investors")),
            "Sector": n.select(item.get("sector")),
            "Region": n.select(item.get("region")),
            "Chains": n.multi(item.get("chains")),
            "Summary": n.linked_text(item["summary"]),
            "Person": n.text(item.get("person") or ""),
            "Role": n.text(item.get("role") or ""),
            "Counterparty": n.text(item.get("counterparty") or ""),
            "Source": n.url(item["source"]),
            "In edition": n.checkbox(item["in_edition"]),
            "Notes": n.text(item.get("notes") or ""),
        }
        if args.dry_run:
            print("  + %s | %s | %s" % (item["date"], item["type"], item["company"]))
        else:
            n.create_page(ds, props)
        added += 1
    print("%s %d, skipped %d already tracked" % ("Would add" if args.dry_run else "Added", added, skipped))


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", required=True)
    c.add_argument("--offline", action="store_true", help="skip the News Tracker lookup")
    r = sub.add_parser("render")
    r.add_argument("--file", required=True)
    r.add_argument("--jobs")
    l = sub.add_parser("lint")
    l.add_argument("--draft", required=True)
    u = sub.add_parser("push")
    u.add_argument("--file", required=True)
    u.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    return {"check": check, "render": render, "lint": lint, "push": push}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
