"""Minimal Notion API client shared by the Stablecoin Brief scripts.

Token lookup: the NOTION_TOKEN environment variable, else the token the local
Notion MCP server already uses (~/.claude.json, mcpServers.notion.env). The
token is never printed.
"""
import datetime
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.notion.com/v1"
VERSION = "2025-09-03"
REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "data" / "notion.json"


def token():
    if os.environ.get("NOTION_TOKEN"):
        return os.environ["NOTION_TOKEN"]
    cfg = Path.home() / ".claude.json"
    if cfg.exists():
        servers = json.loads(cfg.read_text()).get("mcpServers", {})
        tok = (servers.get("notion", {}).get("env") or {}).get("NOTION_TOKEN")
        if tok:
            return tok
    raise SystemExit("No Notion token: set NOTION_TOKEN or configure the notion MCP server in ~/.claude.json")


def request(method, path, body=None, retries=5):
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={
            "Authorization": "Bearer " + token(),
            "Notion-Version": VERSION,
            "Content-Type": "application/json",
        },
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                time.sleep(0.34)  # stay under Notion's ~3 requests/second
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(float(e.headers.get("Retry-After") or 2 ** attempt))
                continue
            raise SystemExit("Notion %s %s failed: %s %s" % (method, path, e.code, e.read().decode()[:500]))


def config():
    if not CONFIG.exists():
        raise SystemExit("data/notion.json missing: run scripts/setup_notion.py first")
    return json.loads(CONFIG.read_text())


def query(data_source_id, filter=None, sorts=None):
    """Yield every page in a data source matching the filter."""
    body = {"page_size": 100}
    if filter:
        body["filter"] = filter
    if sorts:
        body["sorts"] = sorts
    while True:
        res = request("POST", "/data_sources/%s/query" % data_source_id, body)
        yield from res["results"]
        if not res.get("has_more"):
            return
        body["start_cursor"] = res["next_cursor"]


def create_page(data_source_id, properties):
    return request("POST", "/pages", {
        "parent": {"type": "data_source_id", "data_source_id": data_source_id},
        "properties": properties,
    })


def update_page(page_id, properties):
    return request("PATCH", "/pages/%s" % page_id, {"properties": properties})


# Property value builders. Select names can't contain commas.

def _clean(name):
    return re.sub(r"\s+", " ", name.replace(",", "")).strip()[:100]


def title(text):
    return {"title": [{"text": {"content": text[:2000]}}]}


def text(value):
    return {"rich_text": [{"text": {"content": value[:2000]}}] if value else []}


def linked_text(markdown):
    """Rich text from a string that may contain [anchor](url) links."""
    parts, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", markdown):
        if m.start() > pos:
            parts.append({"text": {"content": markdown[pos:m.start()]}})
        parts.append({"text": {"content": m.group(1), "link": {"url": m.group(2)}}})
        pos = m.end()
    if pos < len(markdown):
        parts.append({"text": {"content": markdown[pos:]}})
    return {"rich_text": parts}


def select(name):
    return {"select": {"name": _clean(name)} if name else None}


def multi(names):
    seen, out = set(), []
    for n in names or []:
        n = _clean(n)
        if n and n.lower() not in seen:
            seen.add(n.lower())
            out.append({"name": n})
    return {"multi_select": out}


def date(iso):
    return {"date": {"start": iso} if iso else None}


def url(value):
    return {"url": value or None}


def number(value):
    return {"number": value}


def checkbox(value):
    return {"checkbox": bool(value)}


def plain(prop):
    """Plain-text value of a page property returned by the API."""
    kind = prop["type"]
    val = prop[kind]
    if kind in ("title", "rich_text"):
        return "".join(t["plain_text"] for t in val)
    if kind == "select":
        return val["name"] if val else ""
    if kind == "multi_select":
        return [v["name"] for v in val]
    if kind == "date":
        return val["start"] if val else ""
    return val


def iso_week(iso_date):
    y, w, _ = datetime.date.fromisoformat(iso_date[:10]).isocalendar()
    return "%d-W%02d" % (y, w)
