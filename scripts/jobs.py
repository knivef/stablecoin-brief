"""Weekly job openings for the Stablecoin Brief Jobs Tracker.

    python3 scripts/jobs.py fetch --start 2026-10-19 --end 2026-10-25 --out editions/2026-10-26-weekly/jobs.json
    python3 scripts/jobs.py push --file editions/2026-10-26-weekly/jobs.json [--dry-run] [--no-close] [--exclude "Company"]
    python3 scripts/jobs.py feature --ids greenhouse:stripe:123 ashby:paxos:abc

fetch reads every board in data/job-boards.json, keeps roles first posted inside
the window, and saves them with every currently listed ID per company.
push adds roles the Jobs Tracker doesn't have yet (matched on Job ID, and skipping
reposts of a role already open under the same company, title and location) and
marks tracked roles that have left their board as Closed.
feature ticks Featured on the roles the edition runs.
"""
import argparse
import datetime
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import notion_api as n

BOARDS = n.REPO / "data" / "job-boards.json"
UA = {"User-Agent": "Mozilla/5.0 (stablecoin-brief jobs)", "Accept": "application/json"}
SOURCE = {"greenhouse": "Greenhouse", "lever": "Lever", "ashby": "Ashby", "workday": "Workday",
          "smartrecruiters": "SmartRecruiters", "workable": "Workable"}
SKIP_TITLE = re.compile(r"general application|talent (community|pool|network)|open application|"
                        r"don.t fit|expression of interest|future opportunit|spontaneous application|\(test\)", re.I)


def get(url, body=None):
    req = urllib.request.Request(url, headers=dict(UA, **({"Content-Type": "application/json"} if body else {})),
                                 data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


# --- classification -------------------------------------------------------

FUNCTIONS = [
    ("Legal", r"\b(counsel|legal|attorney|paralegal|lawyer)\b"),
    ("Compliance & risk", r"compliance|\baml\b|\bkyc\b|\bbsa\b|mlro|\brisk\b|fraud|financial crime|sanctions|regulatory|audit|governance"),
    ("Sales & BD", r"sales engineer|solutions engineer|solutions consultant|solutions architect"),
    ("Marketing", r"product marketing"),
    ("Design", r"product design"),
    ("Engineering", r"engineer|engenheir|developer|devops|\bsre\b|architect|security|infrastructure|\bqa\b|\bsdet\b|"
                    r"software|technical lead|information technology|sistemas|testing|technician|blockchain|"
                    r"smart contract|\bcto\b"),
    ("Data", r"\bdata\b|analytics|machine learning|scientist|\bquant|business intelligence|\bbi\b|business analyst|systems analyst"),
    ("Design", r"design|\bux\b|\bui\b|creative"),
    ("Product", r"product|program manager|technical program"),
    ("Research", r"research"),
    ("Sales & BD", r"sales|account exe?cutive|account excutive|business development|\bbdr?\b|\bsdr\b|partnership|account manag|commercial|\bgtm\b|go-to-market|revenue|relationship manag|merchant|cuentas|comercial|\bkam\b"),
    ("Marketing", r"marketing|growth|content|communications|\bpr\b|social media|brand|community|events|\bseo\b|"
                  r"demand gen|lifecycle|user reach"),
    ("Customer success", r"customer|support|success|client|onboarding|implementation|professional services|"
                         r"consultant|deployment|solution expert"),
    ("Finance", r"financ|accounting|accountant|controller|\btax\b|treasury|fp&a|payroll|payable|receivable|billing|"
                r"reporting|record to report"),
    ("People", r"recruit|talent|people|\bhr\b|human resources|workplace|total rewards|training"),
    ("Operations", r"operations|\bops\b|project manag|program lead|chief of staff|strategy|strategist|admin|office|"
                   r"procurement|vendor|incident|operator|processing|delivery"),
]
SENIORITY = [
    ("Intern", r"\bintern|internship|co-op|apprentice|working student"),
    ("C-level", r"\bchief\b|\bc[eftmor]o\b|\bciso\b|general counsel|\bpresident\b"),
    ("VP", r"\bvp\b|vice president|\bsvp\b|\bevp\b"),
    ("Director/Head", r"director|head of|\bhead\b"),
    ("Lead/Staff", r"\blead\b|\bstaff\b|principal|distinguished"),
    ("Senior", r"senior|\bsr\.?\b|\biii\b"),
    ("Entry", r"junior|\bjr\.?\b|entry|graduate|new grad|\bassociate\b|trainee"),
]
REGIONS = [
    ("North America", r"united states|\busa?\b|u\.s\.|canada|new york|\bnyc\b|san francisco|bay area|"
                      r"los angeles|chicago|austin|boston|seattle|miami|denver|toronto|vancouver|montreal|atlanta|"
                      r"dallas|washington|salt lake|phoenix|charlotte|portland|nashville|houston|\bsf\b|"
                      r"arizona|california|texas|florida|georgia|utah|colorado|illinois|ohio|pennsylvania|"
                      r"virginia|massachusetts|carolina|tennessee|oregon|michigan|minnesota|missouri|wisconsin|"
                      r"indiana|kentucky|nebraska|nevada|delaware|maryland|connecticut|new jersey|ontario|"
                      r"british columbia|quebec|alberta"),
    ("Latin America", r"latam|latin america|mexico|brazil|s[aã]o paulo|argentina|buenos aires|colombia|bogot|"
                      r"chile|santiago|peru|\blima\b|uruguay|montevideo|costa rica|south america|venezuela|caracas|"
                      r"nicaragua|managua|guatemala|ecuador|bolivia|paraguay|dominican|panama|el salvador|"
                      r"honduras|jamaica|puerto rico"),
    ("UK", r"united kingdom|\buk\b|\bgbr\b|london|england|scotland|edinburgh|manchester|belfast|wales"),
    ("Europe", r"europe|\bemea\b|germany|berlin|munich|france|paris|spain|madrid|barcelona|lisbon|portugal|"
               r"amsterdam|netherlands|ireland|dublin|poland|warsaw|krak|switzerland|z[uü]rich|\bzug\b|"
               r"malta|cyprus|limassol|lithuania|vilnius|estonia|tallinn|bulgaria|sofia|italy|milan|austria|"
               r"vienna|sweden|stockholm|denmark|copenhagen|norway|oslo|finland|helsinki|belgium|brussels|"
               r"luxembourg|czech|prague|romania|bucharest|greece|gibraltar|serbia|belgrade|ukraine|kyiv|"
               r"hungary|budapest|croatia|slovakia|slovenia|latvia|riga|armenia|iceland"),
    ("Middle East", r"dubai|\buae\b|abu dhabi|united arab emirates|israel|tel aviv|saudi|riyadh|qatar|doha|"
                    r"bahrain|turkey|istanbul|jordan|amman|kuwait|oman|lebanon"),
    ("Africa", r"africa|nigeria|lagos|kenya|nairobi|cape town|johannesburg|ghana|accra|egypt|cairo|morocco|rwanda|"
               r"kigali|tunisia|senegal|dakar|ivoire|uganda|kampala|tanzania|ethiopia|zambia|cameroon|algeria|"
               r"mauritius"),
    ("Asia-Pacific", r"\bapac\b|\bapj\b|asia|singapore|hong kong|japan|tokyo|korea|seoul|\bindia\b|bangalore|bengaluru|"
                     r"mumbai|delhi|gurgaon|gurugram|pune|hyderabad|chennai|australia|sydney|melbourne|"
                     r"philippines|manila|taguig|cebu|indonesia|jakarta|vietnam|ho chi minh|thailand|bangkok|"
                     r"malaysia|kuala lumpur|taiwan|taipei|china|shanghai|beijing|shenzhen|new zealand|auckland|"
                     r"pakistan|sri lanka|bangladesh|dhaka|nepal|kazakhstan|almaty|uzbekistan|tashkent|cambodia|"
                     r"macau"),
]
# Two-letter codes are only trusted from structured country fields, or as a US
# state after a comma ("Austin, TX"): in free text "IN" or "DE" is ambiguous.
US_STATE = re.compile(r",\s*(A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|"
                      r"S[CD]|T[NX]|UT|V[AT]|W[AIVY])\b")
COUNTRY = {
    "North America": "US USA CA",
    "Latin America": "MX BR AR CO CL PE UY CR",
    "UK": "GB UK",
    "Europe": "DE FR ES PT NL IE PL CH MT CY LT EE BG IT AT SE DK NO FI BE LU CZ RO GR GI RS UA",
    "Middle East": "AE IL SA QA BH TR",
    "Africa": "NG KE ZA GH EG MA RW",
    "Asia-Pacific": "SG HK JP KR IN AU PH ID VN TH MY TW CN NZ PK",
}
COUNTRY = {code: region for region, codes in COUNTRY.items() for code in codes.split()}


def match_first(rules, *texts):
    blob = " ".join(t for t in texts if t).lower()
    for label, pattern in rules:
        if re.search(pattern, blob):
            return label
    return None


def regions(location, country=None):
    blob = (location or "").lower()
    found = [label for label, pattern in REGIONS if re.search(pattern, blob)]
    if US_STATE.search(location or ""):
        found.append("North America")
    if country and COUNTRY.get(country.upper()):
        found.append(COUNTRY[country.upper()])
    if not found and re.search(r"anywhere|worldwide|global|remote", blob):
        found = ["Global"]
    order = [label for label, _ in REGIONS] + ["Global"]
    return sorted(set(found), key=order.index)


def work_mode(hint, location):
    blob = ("%s %s" % (hint or "", location or "")).lower()
    if "hybrid" in blob:
        return "Hybrid"
    if "remote" in blob:
        return "Remote"
    if re.search(r"on-?site|in office|in-office", blob):
        return "On-site"
    return "Unspecified"


def employment(hint, title):
    blob = ("%s %s" % (hint or "", title)).lower()
    if re.search(r"intern", blob):
        return "Internship"
    if re.search(r"contract|temporary|temp\b|freelance|fixed.term", blob):
        return "Contract"
    if re.search(r"part.?time", blob):
        return "Part-time"
    return "Full-time"


def record(company, ats, job_id, title, location, posted, url, mode_hint=None, type_hint=None, dept=None,
           salary=None, country=None):
    title = re.sub(r"\s+", " ", title).strip()
    return {
        "id": "%s:%s" % (ats, job_id),
        "title": title,
        "company": company["name"],
        "sector": company["sector"],
        "source": SOURCE[ats],
        "location": location or "",
        "regions": regions(location, country),
        "work_mode": work_mode(mode_hint, location),
        "employment_type": employment(type_hint, title),
        "function": match_first(FUNCTIONS, title) or match_first(FUNCTIONS, dept) or "Other",
        "seniority": match_first(SENIORITY, title) or "Mid",
        "salary": salary or "",
        "posted": posted,
        "url": url,
    }


# --- board readers: each returns (all listed IDs, records posted in window) ---

def greenhouse(c, start, end):
    out, ids = [], []
    for j in get("https://boards-api.greenhouse.io/v1/boards/%s/jobs" % c["slug"])["jobs"]:
        jid = "%s:%s" % (c["slug"], j["id"])
        ids.append("greenhouse:" + jid)
        posted = (j.get("first_published") or j.get("updated_at") or "")[:10]
        if start <= posted <= end:
            out.append(record(c, "greenhouse", jid, j["title"], (j.get("location") or {}).get("name"),
                              posted, j["absolute_url"]))
    return ids, out


def lever(c, start, end):
    out, ids = [], []
    for j in get("https://api.lever.co/v0/postings/%s?mode=json" % c["slug"]):
        jid = "%s:%s" % (c["slug"], j["id"])
        ids.append("lever:" + jid)
        posted = datetime.datetime.utcfromtimestamp(j["createdAt"] / 1000).date().isoformat()
        if start <= posted <= end:
            cat = j.get("categories") or {}
            loc = "; ".join(cat.get("allLocations") or [cat.get("location") or ""])
            sal = j.get("salaryRange") or {}
            salary = ("%s %s-%s %s" % (sal.get("currency", ""), sal.get("min"), sal.get("max"),
                                       sal.get("interval", ""))).strip() if sal.get("min") else ""
            out.append(record(c, "lever", jid, j["text"], loc, posted, j["hostedUrl"],
                              mode_hint=j.get("workplaceType"), type_hint=cat.get("commitment"),
                              dept=cat.get("department") or cat.get("team"), salary=salary, country=j.get("country")))
    return ids, out


def ashby(c, start, end):
    out, ids = [], []
    data = get("https://api.ashbyhq.com/posting-api/job-board/%s?includeCompensation=true" % c["slug"])
    for j in data["jobs"]:
        if j.get("isListed") is False:
            continue
        jid = "%s:%s" % (c["slug"], j["id"])
        ids.append("ashby:" + jid)
        posted = (j.get("publishedAt") or "")[:10]
        if start <= posted <= end:
            locs = [j.get("location") or ""] + [s.get("location", "") for s in j.get("secondaryLocations") or []]
            comp = (j.get("compensation") or {}).get("compensationTierSummary") or ""
            mode = "remote" if j.get("isRemote") else j.get("workplaceType")
            country = ((j.get("address") or {}).get("postalAddress") or {}).get("addressCountry")
            out.append(record(c, "ashby", jid, j["title"], "; ".join(l for l in locs if l), posted, j["jobUrl"],
                              mode_hint=mode, type_hint=j.get("employmentType"),
                              dept=j.get("department") or j.get("team"), salary=comp,
                              country=country if country and len(country) <= 3 else None))
    return ids, out


def smartrecruiters(c, start, end):
    out, ids, offset = [], [], 0
    while True:
        page = get("https://api.smartrecruiters.com/v1/companies/%s/postings?limit=100&offset=%d" % (c["slug"], offset))
        for j in page["content"]:
            jid = "%s:%s" % (c["slug"], j["id"])
            ids.append("smartrecruiters:" + jid)
            posted = (j.get("releasedDate") or "")[:10]
            if start <= posted <= end:
                loc = j.get("location") or {}
                where = ", ".join(x for x in [loc.get("city"), loc.get("region")] if x)
                mode = "remote" if loc.get("remote") else "hybrid" if loc.get("hybrid") else None
                out.append(record(c, "smartrecruiters", jid, j["name"], where, posted,
                                  "https://jobs.smartrecruiters.com/%s/%s" % (j["company"]["identifier"], j["id"]),
                                  mode_hint=mode, type_hint=(j.get("typeOfEmployment") or {}).get("label"),
                                  dept=(j.get("function") or {}).get("label"), country=loc.get("country")))
        offset += 100
        if offset >= page.get("totalFound", 0):
            return ids, out


def workday_days_ago(posted_on):
    s = (posted_on or "").lower()
    if "today" in s:
        return 0
    if "yesterday" in s:
        return 1
    m = re.search(r"(\d+)\+? days? ago", s)
    return int(m.group(1)) + (1 if "+" in s else 0) if m else 999


def workday(c, start, end):
    # Workday pages are 20 roles and each call takes a second or two, so pages
    # and role details are fetched in parallel. The listing only says "Posted 3
    # Days Ago", relative to today: close enough to skip the detail call for
    # every role outside the window.
    base = "https://%s/wday/cxs/%s/%s" % (c["host"], c["tenant"], c["site"])
    today = datetime.date.today()
    day = datetime.timedelta(days=1)  # allow a day either side: "N days ago" rounds
    edge = (datetime.date.fromisoformat(start) - day, datetime.date.fromisoformat(end) + day)

    def listing(offset):
        return get(base + "/jobs", {"appliedFacets": {}, "limit": 20, "offset": offset, "searchText": ""})

    first = listing(0)
    with ThreadPoolExecutor(max_workers=6) as pool:
        pages = [first] + list(pool.map(listing, range(20, first.get("total") or 0, 20)))
        ids, candidates = [], []
        for page in pages:
            for j in page.get("jobPostings") or []:
                path = j.get("externalPath")
                if not path:
                    continue
                jid = "%s:%s" % (c["tenant"], path.rsplit("/", 1)[-1])
                ids.append("workday:" + jid)
                approx = today - datetime.timedelta(days=workday_days_ago(j.get("postedOn")))
                if edge[0] <= approx <= edge[1]:
                    candidates.append((jid, path))
        details = list(pool.map(lambda jp: get(base + jp[1])["jobPostingInfo"], candidates))
    out = []
    for (jid, path), info in zip(candidates, details):
        posted = (info.get("startDate") or "")[:10]
        if start <= posted <= end:
            locs = [info.get("location") or ""] + list(info.get("additionalLocations") or [])
            locs.append((info.get("country") or {}).get("descriptor") or "")
            out.append(record(c, "workday", jid, info["title"], "; ".join(l for l in locs if l), posted,
                              info.get("externalUrl") or "https://%s/%s%s" % (c["host"], c["site"], path),
                              mode_hint=info.get("remoteType"), type_hint=info.get("timeType")))
    return ids, out


def workable(c, start, end):
    out, ids = [], []
    for j in get("https://apply.workable.com/api/v1/widget/accounts/%s" % c["slug"]).get("jobs", []):
        jid = "%s:%s" % (c["slug"], j["shortcode"])
        ids.append("workable:" + jid)
        posted = (j.get("published_on") or j.get("created_at") or "")[:10]
        if start <= posted <= end:
            where = ", ".join(x for x in [j.get("city"), j.get("country")] if x)
            out.append(record(c, "workable", jid, j["title"], where, posted, j["url"],
                              mode_hint="remote" if j.get("telecommuting") else None,
                              type_hint=j.get("employment_type"), dept=j.get("department")))
    return ids, out


READERS = {"greenhouse": greenhouse, "lever": lever, "ashby": ashby, "workday": workday,
           "smartrecruiters": smartrecruiters, "workable": workable}


# --- commands ---------------------------------------------------------------

def fetch(args):
    companies = json.loads(BOARDS.read_text())["companies"]

    def run(c):
        began = time.time()
        try:
            ids, jobs = READERS[c["ats"]](c, args.start, args.end)
            jobs = [j for j in jobs if not SKIP_TITLE.search(j["title"])]
            print("  %-32s %4d listed %3d new  %4.0fs" % (c["name"], len(ids), len(jobs), time.time() - began),
                  file=sys.stderr, flush=True)
            return c["name"], ids, jobs, None
        except Exception as e:  # one broken board shouldn't sink the run
            return c["name"], None, [], "%s: %s" % (type(e).__name__, str(e)[:120])

    slow_first = sorted(companies, key=lambda c: c["ats"] != "workday")
    with ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(run, slow_first))

    listed, new, errors = {}, [], {}
    for name, ids, jobs, err in results:
        if err:
            errors[name] = err
        else:
            listed[name] = ids
            new.extend(jobs)
    new.sort(key=lambda j: (j["company"].lower(), j["posted"], j["title"]))
    out = {"window": {"start": args.start, "end": args.end},
           "fetched": datetime.date.today().isoformat(),
           "new": new, "errors": errors, "listed": listed}
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)

    per_company = {}
    for j in new:
        per_company[j["company"]] = per_company.get(j["company"], 0) + 1
    print("%d new roles posted %s to %s across %d of %d boards" % (
        len(new), args.start, args.end, len(per_company), len(companies)))
    for name, count in sorted(per_company.items(), key=lambda kv: -kv[1]):
        print("  %-32s %d" % (name, count))
    for name, count in per_company.items():
        if count >= 30 and count > 0.5 * len(listed.get(name, [])):
            print("  WARNING %s: %d of %d listed roles are new this week; likely a board migration or mass repost."
                  " Check, then push with --exclude \"%s\" unless they're genuinely new" % (
                      name, count, len(listed[name]), name))
    for name, err in errors.items():
        print("  BOARD FAILED %s: %s" % (name, err))
    print("Saved %s" % args.out)


def properties(j, today):
    return {
        "Role": n.title(j["title"]),
        "Company": n.select(j["company"]),
        "Sector": n.select(j["sector"]),
        "Function": n.select(j["function"]),
        "Seniority": n.select(j["seniority"]),
        "Location": n.text(j["location"]),
        "Region": n.multi(j["regions"]),
        "Work mode": n.select(j["work_mode"]),
        "Employment type": n.select(j["employment_type"]),
        "Salary": n.text(j["salary"]),
        "Posted": n.date(j["posted"]),
        "Week": n.select(n.iso_week(j["posted"])),
        "First seen": n.date(today),
        "Status": n.select("Open"),
        "Apply URL": n.url(j["url"]),
        "Source": n.select(j["source"]),
        "Job ID": n.text(j["id"]),
    }


def repost_key(company, title, location):
    return (company.lower(), re.sub(r"\W+", " ", title.lower()).strip(), location.lower().strip())


def push(args):
    data = json.loads(open(args.file).read())
    ds = n.config()["jobs"]["data_source_id"]
    today = datetime.date.today().isoformat()
    since = (datetime.date.fromisoformat(data["window"]["start"]) - datetime.timedelta(days=45)).isoformat()
    excluded = {e.lower() for e in args.exclude}

    tracked = set()
    for page in n.query(ds, {"property": "Posted", "date": {"on_or_after": since}}):
        tracked.add(n.plain(page["properties"]["Job ID"]))
    open_rows, open_keys = [], set()
    for page in n.query(ds, {"property": "Status", "select": {"equals": "Open"}}):
        p = page["properties"]
        row = (page["id"], n.plain(p["Company"]), n.plain(p["Role"]), n.plain(p["Location"]), n.plain(p["Job ID"]))
        open_rows.append(row)
        open_keys.add(repost_key(row[1], row[2], row[3]))

    fresh, reposts, skipped_excluded = [], 0, 0
    for j in data["new"]:
        if j["company"].lower() in excluded:
            skipped_excluded += 1
        elif j["id"] in tracked:
            continue
        elif repost_key(j["company"], j["title"], j["location"]) in open_keys:
            reposts += 1
        else:
            fresh.append(j)
            open_keys.add(repost_key(j["company"], j["title"], j["location"]))
    print("%d roles in file: %d to add, %d already tracked, %d duplicates of an open role (same company, title and location), %d excluded" % (
        len(data["new"]), len(fresh), len(data["new"]) - len(fresh) - reposts - skipped_excluded,
        reposts, skipped_excluded))

    to_close = []
    if not args.no_close:
        listed = {name: set(ids) for name, ids in data["listed"].items()}
        to_close = [(pid, company, role) for pid, company, role, _, jid in open_rows
                    if company in listed and jid and jid not in listed[company]]
        print("%d tracked roles no longer listed, to close" % len(to_close))

    if args.dry_run:
        for j in fresh[:15]:
            print("  + %s | %s | %s | %s | %s" % (j["company"], j["title"], j["function"], j["seniority"], j["posted"]))
        for _, company, role in to_close[:15]:
            print("  - %s | %s" % (company, role))
        print("Dry run: nothing written")
        return
    # Three writers in parallel keep close to Notion's ~3 requests/second;
    # one at a time is mostly waiting on network round trips.
    def add(item):
        i, j = item
        n.create_page(ds, properties(j, today))
        if i % 100 == 0:
            print("  added %d/%d" % (i, len(fresh)), flush=True)

    def close(row):
        n.update_page(row[0], {"Status": n.select("Closed"), "Closed on": n.date(today)})

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(add, enumerate(fresh, 1)))
        list(pool.map(close, to_close))
    print("Added %d, closed %d" % (len(fresh), len(to_close)))


def feature(args):
    ds = n.config()["jobs"]["data_source_id"]
    for jid in args.ids:
        pages = list(n.query(ds, {"property": "Job ID", "rich_text": {"equals": jid}}))
        if not pages:
            print("  not tracked: %s" % jid)
        for page in pages:
            n.update_page(page["id"], {"Featured": n.checkbox(True)})
            print("  featured: %s" % jid)


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--start", required=True)
    f.add_argument("--end", required=True)
    f.add_argument("--out", required=True)
    u = sub.add_parser("push")
    u.add_argument("--file", required=True)
    u.add_argument("--dry-run", action="store_true")
    u.add_argument("--no-close", action="store_true")
    u.add_argument("--exclude", nargs="*", default=[], help="company names to leave out of this push")
    t = sub.add_parser("feature")
    t.add_argument("--ids", nargs="+", required=True)
    args = p.parse_args()
    {"fetch": fetch, "push": push, "feature": feature}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
