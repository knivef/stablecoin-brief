# Stablecoin Brief

Skill definitions and tooling for **Stablecoin Brief**, a weekly newsletter that tracks the money, people and licenses moving through stablecoins and payments.

This repo holds no newsletter content. It holds the instructions and scripts that produce it. Clone it, open Claude Code in the folder, type `/weekly`, and a full issue gets researched, reviewed by you, written, quality checked, logged to two Notion trackers, and published to Notion as a draft.

## The format

Every news item is one sentence of 20 words or fewer, grouped by category and led by the company name:

- 💰 Fundraising, tiered by size: $25M+, $5M to $25M, under $5M, undisclosed
- 🤝 M&A
- 🔄 People moves
- ⚖️ Regulation & licensing
- 🚀 Launches
- 🔗 Partnerships
- 📉 Layoffs & shutdowns
- 💼 Who's hiring: 5 to 8 featured roles

An intro and a six-row numbers table sit on top; a one-line sign-off closes it. The model is The LegalTech Fund's [Funds Flow](https://www.legaltech.com/post/funds-flow-october-2026) and [The Docket](https://www.legaltech.com/post/the-docket-october-2026). Coverage is stablecoins plus all of payments, with or without a crypto angle.

The newsletter is the curated cut. Two Notion databases under the Stablecoin Brief page are the complete record:

| Tracker | What goes in | Tags |
| --- | --- | --- |
| 📰 **News Tracker** | Every item researched each week, in the edition or not. Modeled on [DefiLlama Raises](https://defillama.com/raises). | Week, Type, Round, Amount ($M), Valuation ($M), Lead investors, Other investors, Sector, Region, Chains, Person, Role, Counterparty, In edition |
| 💼 **Jobs Tracker** | Every role first posted that week at the companies in `data/job-boards.json` | Company, Sector, Function, Seniority, Region, Work mode, Employment type, Posted, Week, Status (Open/Closed), Source, Featured |

The Notion API can't create views, so add these by hand once: on the News Tracker, a **Raises** table filtered to Type = Fundraise and sorted by Date, and a board grouped by **Week**; on the Jobs Tracker, a table filtered to Status = Open and a board grouped by **Function**.

## Repo layout

```
.
├── CLAUDE.md                  # Master context: audience, format, voice, style rules, scope, sources
├── skills/
│   └── weekly/
│       └── SKILL.md           # The weekly pipeline
├── scripts/
│   ├── notion_api.py          # Shared Notion client (token from NOTION_TOKEN or the Notion MCP config)
│   ├── setup_notion.py        # One-time: creates both trackers, writes data/notion.json
│   ├── news.py                # check / render / lint / push for the week's news items
│   └── jobs.py                # fetch / push / feature for the week's job openings
├── data/
│   ├── notion.json            # Tracker database and data source IDs
│   └── job-boards.json        # Companies whose public job boards get read every week
├── .claude/
│   └── commands/
│       └── weekly.md          # /weekly slash command, invokes the skill
└── .gitignore                 # editions/ stays local
```

The scripts need only the system `python3` (3.9+, standard library). The previous Big One deep-dive format is in git history at commit `19015a8`. The Monday/Wednesday/Friday skills that ran before 2026-07-21 are archived in [knivef/stablecoin-brief-legacy](https://github.com/knivef/stablecoin-brief-legacy) with the `CLAUDE.md` they depend on.

## How the skill works

The skill fires on `/weekly` or on natural phrasing like "run the weekly" or "newsletter time". It runs five steps end to end, with one stop at Step 2 for your review.

### Step 1: research

Sweeps the most recent Monday-to-Sunday window for fundraises, M&A, people moves, regulation and licensing, launches and partnerships. It aims for every disclosed round in scope, not a sample. Every item goes into `editions/[date]-weekly/news.json` with its 20-word summary and its tags.

Jobs come from the public job-board APIs (Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable) of about 80 companies, from Stripe, Visa and Circle to Paxos and BVNK. `jobs.py fetch` keeps every role first posted in the window, and `jobs.py push` adds it to the Jobs Tracker. Push skips roles already tracked and reposts of an open role, and closes roles that have left their board. It flags boards where most roles look new at once, which usually means the company switched job-board providers. Each week, companies that raised money or did a deal get checked for a public board and added to the list.

Three checks run on every item by default: the event date is confirmed against the primary source, the facts are re-read from the source page, and `news.py check` looks the company up in the News Tracker and searches every past edition, so a running story doesn't run twice under a new headline.

### Step 2: lineup review

The only stop. You see the week in numbers, every item section by section, 8 to 10 featured-job candidates, and any judgment calls (a likely duplicate kept as a new development, thin sourcing, an excluded board). Veto, add, reword or pick jobs; "go" runs it as presented. An item vetoed as wrong is deleted; one cut for space stays in the tracker.

### Step 3: draft

`news.py render` prints the categorized sections from news.json, so the newsletter and the News Tracker never disagree. The skill writes the metadata block (3 subject lines, SEO description), the intro, the numbers table, Who's hiring, an optional Worth your time, and the sign-off around them. Sponsor Slot 1 sits above the intro; Slot 2 sits after Fundraising.

### Step 4: quality check

`news.py check` and `news.py lint` enforce the mechanical rules: 20 words per item, one well-anchored link, no dashes, no bare URLs, valid tags, in-window dates, no duplicates. The checklist covers what scripts can't: amounts, rounds, titles and deal stages match the source; tiers and currency conversions are right; derived numbers are recomputed; weekdays match dates; featured roles are still open.

### Step 5: publish

Pushes every item to the News Tracker, ticks Featured on the chosen roles, and creates a `DRAFT: [theme] ([dates])` page under the Stablecoin Brief page with the full draft. Every command is safe to re-run.

## First-time setup

The trackers already exist (IDs in `data/notion.json`). On a fresh workspace, run `python3 scripts/setup_notion.py` once with a Notion integration that has access to the Stablecoin Brief page.

## Editing the skill

Change the standing voice, style rules, scope or sources in `CLAUDE.md`. Change the pipeline, sections or quality gates in `skills/weekly/SKILL.md`. Change tags in `scripts/setup_notion.py` (and add the new option to the Notion database too). Add job boards in `data/job-boards.json`, after confirming the board belongs to that company: slugs collide.

## Error handling

The skill degrades rather than fabricates. A thin week ships short instead of padded. A failed job board is noted and skipped. An unavailable metric shows `n/a` with a note. Unverifiable claims are dropped and flagged. If Notion is down, everything stays local and the push commands can run later.
