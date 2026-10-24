"""Create the News Tracker and Jobs Tracker databases under the Stablecoin Brief
page in Notion and record their IDs in data/notion.json. Run once.

    python3 scripts/setup_notion.py [--force]
"""
import json
import sys

import notion_api as n

PARENT_PAGE = "32b7f3d2-e709-80bf-b981-e69ae10cc902"  # Stablecoin Brief

SECTORS = [
    "Stablecoin issuer", "Stablecoin infra", "Payments & PSPs", "Cards & issuing",
    "Cross-border & remittance", "On/off ramps", "Banking & BaaS", "B2B & spend",
    "Open banking", "Core processing", "Exchanges & brokers", "Custody & wallets",
    "Chains & protocols", "Tokenization & RWA", "Compliance & risk", "DeFi",
    "Banks & FIs", "Regulators & policy", "Other",
]
REGIONS = [
    "North America", "Latin America", "UK", "Europe", "Middle East", "Africa",
    "Asia-Pacific", "Global",
]
COLORS = ["green", "blue", "purple", "orange", "yellow", "red", "pink", "brown", "gray", "default"]


def options(names, colors=None):
    colors = colors or COLORS
    return [{"name": name, "color": colors[i % len(colors)]} for i, name in enumerate(names)]


NEWS = {
    "Company": {"title": {}},
    "Date": {"date": {}},
    "Week": {"select": {"options": []}},
    "Type": {"select": {"options": options([
        "Fundraise", "M&A", "People move", "Launch", "Partnership",
        "Regulation & licensing", "Layoffs & shutdowns", "Other",
    ], ["green", "purple", "blue", "orange", "yellow", "red", "gray", "default"])}},
    "Round": {"select": {"options": options([
        "Pre-seed", "Seed", "Series A", "Series B", "Series C", "Series D+",
        "Strategic", "Debt", "Token sale", "Grant", "IPO", "Undisclosed",
    ])}},
    "Amount ($M)": {"number": {"format": "number"}},
    "Valuation ($M)": {"number": {"format": "number"}},
    "Lead investors": {"multi_select": {"options": []}},
    "Other investors": {"multi_select": {"options": []}},
    "Sector": {"select": {"options": options(SECTORS)}},
    "Region": {"select": {"options": options(REGIONS)}},
    "Chains": {"multi_select": {"options": []}},
    "Summary": {"rich_text": {}},
    "Person": {"rich_text": {}},
    "Role": {"rich_text": {}},
    "Counterparty": {"rich_text": {}},
    "Source": {"url": {}},
    "In edition": {"checkbox": {}},
    "Notes": {"rich_text": {}},
}

JOBS = {
    "Role": {"title": {}},
    "Company": {"select": {"options": []}},
    "Sector": {"select": {"options": options(SECTORS)}},
    "Function": {"select": {"options": options([
        "Engineering", "Product", "Design", "Data", "Research", "Sales & BD",
        "Marketing", "Customer success", "Operations", "Finance",
        "Compliance & risk", "Legal", "People", "Other",
    ])}},
    "Seniority": {"select": {"options": options([
        "Intern", "Entry", "Mid", "Senior", "Lead/Staff", "Director/Head", "VP", "C-level",
    ], ["gray", "brown", "default", "blue", "purple", "orange", "red", "pink"])}},
    "Location": {"rich_text": {}},
    "Region": {"multi_select": {"options": options(REGIONS)}},
    "Work mode": {"select": {"options": options(
        ["Remote", "Hybrid", "On-site", "Unspecified"], ["green", "yellow", "blue", "gray"])}},
    "Employment type": {"select": {"options": options(
        ["Full-time", "Part-time", "Contract", "Internship"], ["blue", "yellow", "orange", "gray"])}},
    "Salary": {"rich_text": {}},
    "Posted": {"date": {}},
    "Week": {"select": {"options": []}},
    "First seen": {"date": {}},
    "Closed on": {"date": {}},
    "Status": {"select": {"options": options(["Open", "Closed"], ["green", "gray"])}},
    "Apply URL": {"url": {}},
    "Source": {"select": {"options": options([
        "Greenhouse", "Lever", "Ashby", "Workday", "SmartRecruiters", "Workable",
        "Careers page", "Job board",
    ])}},
    "Job ID": {"rich_text": {}},
    "Featured": {"checkbox": {}},
}


def create(name, emoji, description, properties):
    db = n.request("POST", "/databases", {
        "parent": {"type": "page_id", "page_id": PARENT_PAGE},
        "title": [{"type": "text", "text": {"content": name}}],
        "description": [{"type": "text", "text": {"content": description}}],
        "icon": {"type": "emoji", "emoji": emoji},
        "is_inline": False,
        "initial_data_source": {"properties": properties},
    })
    return {"database_id": db["id"], "data_source_id": db["data_sources"][0]["id"], "url": db.get("url")}


def main():
    if n.CONFIG.exists() and "--force" not in sys.argv:
        raise SystemExit("data/notion.json already exists; pass --force to create new databases")
    cfg = {
        "parent_page_id": PARENT_PAGE,
        "news": create("News Tracker", "📰",
                       "Every stablecoin and payments development the weekly brief researches: "
                       "raises, M&A, people moves, launches, partnerships, licenses. Written by scripts/news.py.",
                       NEWS),
        "jobs": create("Jobs Tracker", "💼",
                       "New roles at stablecoin and payments companies, pulled from public job boards "
                       "by scripts/jobs.py every week.",
                       JOBS),
    }
    n.CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")
    print(json.dumps(cfg, indent=2))


if __name__ == "__main__":
    main()
