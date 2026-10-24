---
name: weekly
description: Produce the weekly issue of Stablecoin Brief, the newsletter tracking money, people and licenses moving through stablecoins and payments. Use this whenever kvn types "weekly", asks to "run the weekly", "write this week's issue", "create the Stablecoin Brief", "draft the newsletter", or mentions producing, drafting, or publishing any Stablecoin Brief issue, even casually ("let's do this week's brief", "newsletter time"). The skill runs the full pipeline: sweep the past week for fundraises, M&A, people moves, licenses, launches and partnerships; pull new job openings from company job boards; present the lineup for kvn's review; write every item in 20 words or fewer under its category; quality check; log every item to the Notion News Tracker and Jobs Tracker; publish the draft to Notion. Do not write a Stablecoin Brief issue without this skill.
---

# Stablecoin Brief: Weekly Issue

One issue per week, sent Mondays. The format is a scannable record of what moved in stablecoins and payments: who raised, who bought whom, who moved where, who got licensed, what launched, and who's hiring. Every item is one sentence of 20 words or fewer, grouped by category, with fundraises tiered by size. The model is The LegalTech Fund's [Funds Flow](https://www.legaltech.com/post/funds-flow-october-2026) and [The Docket](https://www.legaltech.com/post/the-docket-october-2026).

Every item researched also lands in the Notion **News Tracker**, a filterable deals-and-moves database modeled on [DefiLlama Raises](https://defillama.com/raises). Every new role at tracked companies lands in the Notion **Jobs Tracker**. The newsletter is the curated cut; the trackers are the complete record.

This format replaced The Big One deep-dive format on 2026-10-26. That version is in git history (commit `19015a8`); the Monday/Wednesday/Friday skills are archived at [knivef/stablecoin-brief-legacy](https://github.com/knivef/stablecoin-brief-legacy).

## On activation

1. Detect today's date. The coverage window is the most recent complete Monday through Sunday. If today is mid-week and the user clearly wants the current week, use Monday through today instead.
2. Create folder: `editions/[YYYY-MM-DD]-weekly/` (dated to the upcoming or current Monday, the send day).
3. Begin Step 1 immediately, with no preamble and no confirmation of scope. If the user supplied a specific date range, use that instead of the default window.
4. The pipeline runs unattended except for one gate: Step 2 presents the lineup and waits for kvn's edits. Every other step runs straight through.

Scripts live in `scripts/` and run from the repo root with the system `python3` (stdlib only). Notion IDs for both trackers are in `data/notion.json`. The scripts find the Notion token in `NOTION_TOKEN` or, failing that, in the local Notion MCP config in `~/.claude.json`.

## Audience and voice

Readers work in or around stablecoins and payments: operators, investors, BD, compliance. They know what USDC, USDT, on-chain settlement, MiCA and the GENIUS Act are. Do not explain basics. They scan. The bar for every issue: a reader who spends three minutes on it knows every deal, move and license that mattered this week, and finds at least one they hadn't seen.

The items read like a sharp wire service: plain, specific, past tense, no adjectives doing the work a number should do. Personality lives in three places only: the subject line, the intro, and the sign-off. One light line in the intro is welcome. Jokes never go inside items.

### Style rules (non-negotiable)

- No em dashes, no en dashes, no `--` as punctuation
- No filler: "it remains to be seen", "in the ever-evolving landscape", "as the industry matures", "going forward", "at the end of the day", "significant milestone", "it is worth noting"
- No corporate jargon, no rhetorical questions, no passive voice where avoidable
- **Every item is one sentence of 20 words or fewer.** Count the rendered text: link anchor text counts, URLs don't, "$30M" is one word. Hard stop. `scripts/news.py` enforces it.
- Item formula: **Company** + verb + the specific fact (link on this phrase) + the one detail that makes it matter (what the company does, the lead investor, the market, the person's previous role). Lead with the company name. Past tense for completed events.
- Exactly one inline link per item, embedded on the most specific phrase: the action ("raised $30M", "acquired Bridge", "named Jane Smith CFO", "won a MiCA license"). Never anchor on "here", "this", "report", "announced", or a bare publication name. No floating source tags.
- Numbers are specific: amount, round, valuation when disclosed. State the original currency in the item ("€20M") and convert to USD for tiers and the tracker. Comparison context (vs last week, vs a precedent) belongs in the intro and the numbers table, where there's room; inside an item, add it only when it fits in the 20 words and has a source behind it.
- Get the deal stage right: "raised" (closed), "is raising" or "in talks to raise" (reported), "agreed to acquire" (signed), "completed its acquisition" (closed). These are factual claims.
- Never mirror a source's headline or subhead closely enough that an item reads like a paraphrase of it. Same facts, this newsletter's own sentence structure and word choices, every time.
- Bold is for section headers and the company name that leads each item, nothing else.
- US spelling ("license", "tokenization"), except inside a proper name.

The examples below use made-up companies; they show the shape, not news.

Wrong (26 words, a headline paraphrase): "Northwind Pay Secures $30 Million Series B Funding Round Led By Acme Ventures To Accelerate Its Mission Of Transforming Stablecoin Payouts For Freelancers Across Latin America"
Right (18 words): "**Northwind Pay** [raised a $30M Series B led by Acme Ventures](url) for stablecoin payouts to Latin American freelancers."

Wrong: "Big news for Acme as the company welcomes a seasoned executive to its leadership team."
Right: "**Acme Pay** [named Jane Smith CFO](url); she ran treasury at Stripe for six years."

## Coverage scope

Stablecoins plus all of payments, with or without a crypto angle:

- **Stablecoins:** issuers, issuance and orchestration infrastructure, payment chains, reserve managers, bank-issued tokens and tokenized deposits
- **Crypto payments:** on/off ramps, wallets and custody, stablecoin cards, merchant acceptance
- **Payments:** PSPs and acquirers, cross-border and remittance, B2B payments and spend, card issuing, open banking, BaaS and payments-focused banks, core processing
- **Adjacent, only when the news is payments-led:** exchanges launching payment or stablecoin products, tokenization with a stablecoin cash leg, compliance and blockchain-analytics vendors

Out of scope: token prices and trading, DeFi yield, NFTs, memecoins, and fintech lending, insurance or wealth news without a payments product in it.

## Categories

Every item gets exactly one Type. These are the News Tracker's Type values and the newsletter's sections, in this order.

| Type | Section | Qualifies | Doesn't |
| --- | --- | --- | --- |
| Fundraise | 💰 FUNDRAISING | Equity rounds, strategic investments, debt facilities, token sales with a named amount or a confirmed "undisclosed". Tiered: $25M+, $5M to $25M, under $5M, undisclosed. | Rumored rounds with no source on the record |
| M&A | 🤝 M&A | Acquisitions, mergers, majority stakes, acqui-hires, signed or closed (say which) | "Exploring a sale" |
| People move | 🔄 PEOPLE MOVES | C-suite, founders, heads of payments, stablecoin or digital-asset units at notable firms; board seats; regulator appointments; notable departures | Routine VP hires at small firms |
| Regulation & licensing | ⚖️ REGULATION & LICENSING | Licenses and charters granted (MiCA CASP or EMI, OCC, NYDFS, MAS, VARA, state MTLs), laws passed, final rules, enforcement actions, central-bank decisions | Speeches and consultations, unless major (then Other) |
| Launch | 🚀 LAUNCHES | Products, stablecoins, chains or corridors that went live, or have a firm public date | Vague roadmaps |
| Partnership | 🔗 PARTNERSHIPS | Integrations and commercial deals with a named counterparty and concrete scope | MOUs with no substance |
| Layoffs & shutdowns | 📉 LAYOFFS & SHUTDOWNS | Layoffs, wind-downs, market exits, licenses surrendered | |
| Other | 📌 ALSO NOTABLE | Depegs, data milestones, major reports. Use sparingly. | |

Sector and Region values are fixed lists in `scripts/setup_notion.py` (`SECTORS`, `REGIONS`); use them exactly.

## Trusted sources

Primary always wins: company newsrooms and blogs, press-release wires (PR Newswire, Business Wire, GlobeNewswire), regulatory filings and registers (SEC EDGAR including Form D, OCC, NYDFS, FCA register, ESMA's MiCA register, MAS, VARA), earnings transcripts, and on-chain or dashboard data (DeFiLlama, Artemis, Dune).

Where to find the week's flow:

- **Deals:** [DefiLlama Raises](https://defillama.com/raises) (WebFetch gets a 403; read it with the built-in browser pane's `get_page_text` when available, otherwise search for its entries), Crunchbase News weekly round-ups, This Week in Fintech, Fintech Business Weekly, TechCrunch fintech, The Block, CoinDesk, Fortune Crypto, Blockworks, Finextra, PYMNTS, Payments Dive, The Paypers, FinTech Futures, Axios Pro headlines. Regional: Sifted (Europe), TechCabal (Africa), LatamList and Contxto (LatAm), Entrackr and Inc42 (India), DealStreetAsia (Asia), Ledger Insights (banks, tokenization).
- **People moves:** company releases, Finextra people news, FinTech Futures "Movers and shakers", The Paypers, Payments Dive, American Banker, CoinDesk and The Block.
- **Regulation:** regulator press pages first; The Block and CoinDesk policy desks, Ledger Insights.

Prefer primary sources over aggregators. If only an aggregator covers a story, use it but flag it in the research brief so the editor can swap the link. When a fact is covered by both a primary or company source and an SEO-farm aggregator, use the primary source even if the aggregator's copy reads better: aggregator URLs (news-mill sites in particular) go dead more often.

---

## Step 1: Research

Research everything before writing a word.

Three checks apply to every candidate item, by default, not only when asked:

- **Verify the real event date via primary source.** Web search summaries blend an older event with newer follow-up coverage (a round announced one week gets analysis coverage the next, which then reads as "this week's news" in search results). Before including any item, fetch the primary source and confirm the underlying event happened inside the Monday-Sunday window, not just that some article discussing it was published in-window.
  - **When secondary sources disagree on the date, the primary document's own stamp wins.** Outlets publish on different days and each writes "this week," so one event can appear under three or four dates. Do not average them or pick the most common one. Open the underlying document and use its date.
  - **Regulatory primaries are usually PDFs, and WebFetch cannot parse them.** WebFetch still saves the file locally and names the path in its result: extract it with `python3 -c "import pypdf,sys; print('\n'.join(p.extract_text() for p in pypdf.PdfReader(sys.argv[1]).pages))" <path>` (pypdf is installed; `pdftotext` is not), then read it. Regulatory documents carry the exact license type, conditions and dates that coverage rounds off.
- **Check the trackers and the whole archive, not just recent editions.** `scripts/news.py check` (workstream H) looks every company up in the News Tracker and searches every past edition. A story can recur as a slow-building saga weeks apart (a raise reported as "in talks", then "raising", then "closed"; a license "applied for", then "in principle", then "granted"), where each mention reads like fresh news in isolation.
- **Re-read the facts from the source, not from the search snippet.** Amount, round, lead investor, valuation, person, title, previous employer, license type: each one checked on the page itself.

### A. Fundraising sweep

Aim to capture every disclosed round in scope during the window, not a sample. Search by category ("stablecoin startup raises", "payments startup Series A", "cross-border payments funding", "seed round stablecoin infrastructure") and by region, then cross-check DefiLlama Raises (Payments, Stablecoin, Banking and related categories) and the weekly round-ups. For each: company, what it does in eight words or fewer, amount and currency, round, lead investors, other investors, valuation if disclosed, HQ region, sector, chains if relevant, event date, primary source.

### B. M&A sweep

Acquirer, target, what the target does, price if disclosed, signed or closed, date, primary source.

### C. People moves sweep

Person, new organization and title, previous organization and title, start date if given, primary source (the company's release or the person's own announcement as reported by a reliable outlet).

### D. Regulation and licensing sweep

Regulator, recipient or rule, the exact license or rule type, conditions that matter, date on the document itself.

### E. Launches and partnerships

Only the ones a reader in the space would forward: named counterparties, live dates, real scope. Skip press-release filler.

### F. Jobs

Run the jobs pipeline:

```bash
python3 scripts/jobs.py fetch --start [MON] --end [SUN] --out editions/[DATE]-weekly/jobs.json
python3 scripts/jobs.py push --file editions/[DATE]-weekly/jobs.json --dry-run
```

`fetch` reads every board in `data/job-boards.json` (Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable) and keeps roles first posted inside the window. Read its output before pushing:

- **Board failed:** note it in the brief and move on; one broken board never blocks the run.
- **Migration or mass-repost warning:** a board where most listed roles look new in one week (a company switching job-board providers republishes everything). Push with `--exclude "[Company]"` unless the roles are genuinely new, and say which you excluded in the brief.

Then push for real (`push` without `--dry-run`). It adds roles the Jobs Tracker doesn't have, skips reposts of a role already open under the same company, title and location, and marks tracked roles that left their board as Closed.

**Grow the board list every week.** For each company in this week's Fundraise or M&A items that isn't in `data/job-boards.json`, find its careers page and check whether it runs on a supported board. Confirm the board belongs to that company before adding it (read the board's name or a posting's "About us"): slugs collide, and `ashby/circle` is Circle.so, not Circle. Add confirmed boards and re-run `fetch` and `push`. Add companies with no public board to `no_public_board` so the next run doesn't re-check them.

Pick 8-10 **featured role candidates** for Step 2: senior or hard-to-fill roles, roles at companies in this week's news (a company that just raised is hiring with that money), stablecoin-native companies, roles with disclosed salary, and a spread across functions and regions. Never feature a role the fetch didn't return or one already marked Closed.

### G. The Numbers

Standing metrics for the table: total stablecoin market cap, USDT supply, USDC supply (DeFiLlama, `https://stablecoins.llama.fi/stablecoins` or stablecoincharts; note the as-of date for each), plus this week's tracker totals from `news.py check` (raised and round count, biggest round, new roles). Compare the raise total with the previous week by querying the News Tracker for the prior Week value; until the tracker has a prior week, say "n/a (tracking began 2026-10-26)" rather than guessing.

### H. Write news.json and run the duplicate check

Write every researched item, in-edition or not, to `editions/[DATE]-weekly/news.json`, ranked by newsworthiness within each Type:

```json
{
  "window": {"start": "2026-10-19", "end": "2026-10-25"},
  "items": [
    {
      "company": "Northwind Pay",
      "type": "Fundraise",
      "date": "2026-10-21",
      "summary": "Northwind Pay [raised a $30M Series B led by Acme Ventures](https://primary-source) for stablecoin payouts to Latin American freelancers.",
      "source": "https://primary-source",
      "sector": "Cross-border & remittance",
      "region": "Latin America",
      "round": "Series B",
      "amount_musd": 30,
      "valuation_musd": null,
      "lead_investors": ["Acme Ventures"],
      "other_investors": [],
      "chains": [],
      "person": null,
      "role": null,
      "counterparty": null,
      "in_edition": true,
      "notes": "aggregator link? date conflicts? anything the editor should know"
    }
  ]
}
```

Field rules: `summary` is the newsletter sentence, starting with the company name, with exactly one `[anchor](url)` link. `amount_musd` is USD millions (convert non-USD amounts and record the rate's source in `notes`). For M&A, `company` is the acquirer and `counterparty` the target. For people moves, `company` is the new employer, `person` and `role` the hire, `counterparty` the previous employer. `in_edition: false` keeps an item in the tracker but out of the newsletter.

Then run:

```bash
python3 scripts/news.py check --file editions/[DATE]-weekly/news.json
```

It enforces the 20-word cap, one link per summary, valid Type/Round/Sector/Region values, no dashes, and the window, and it flags every company that already appears in the News Tracker or a past edition. Resolve every ERROR. A **LIKELY DUPLICATE** gets cut, unless it is a genuinely new event in a running story (a round that closed after being reported as in progress, a license granted after being applied for); then the item must be about the new event, and `notes` says so. Re-run until it reports 0 errors. Read the "info" lines too: a company named in a past edition is often fine, but check that this item isn't the same news.

If more than about 45 items qualify, keep the full set in news.json and set `in_edition: false` on the least newsworthy launches, partnerships and undisclosed micro-rounds. Never pad a thin week.

Save `editions/[DATE]-weekly/research-brief.md`:

```
# Weekly Research Brief
Date: [DATE] | Coverage: [MON] to [SUN]

## Week in numbers
[the line news.py check prints, plus the market metrics with as-of dates and sources]

## Lineup by section
[each section's items in rank order: company, the fact, date verified against which primary source]

## Featured job candidates
[8-10: company, role, location, salary if shown, why it's worth featuring, Job ID]

## Jobs run
[roles fetched, added, closed; boards that failed; boards excluded as migrations; boards added this week]

## Discarded items
[one line each with the reason: out of window, duplicate, out of scope, unverifiable, vetoed]

## Duplicate check performed
[the news.py check result: errors found and how each was resolved, and the info-line matches reviewed]

## Aggregator links to swap
[any non-primary sources used]
```

---

## Step 2: Lineup review

This is the pipeline's only stop. Present the lineup in chat and wait. Do not draft before kvn responds.

Present, in this order:

1. **Week in numbers**, one line.
2. **The lineup**, section by section in newsletter order, one line per item: the summary sentence (link text only, no URL). Fundraises grouped under their tiers. Mark items that are `in_edition: false` as tracker-only.
3. **Featured job candidates**, 8-10, one line each, recommending 5-8.
4. **Judgment calls worth surfacing**, only when there are any: a likely duplicate that was kept as a new event, a thin or aggregator-only source, an item borderline in scope, a deal stage that's unclear, a board migration excluded from the jobs push.

Then stop and wait.

Handling the response:

- **kvn edits or vetoes items:** apply them in news.json. An item vetoed as wrong or out of scope is deleted; one vetoed for space gets `in_edition: false` and stays in the tracker.
- **kvn adds an item:** research it to the same standard (date, primary source, duplicate check) before it goes in. If the reporting doesn't support it, say so.
- **kvn picks jobs:** those are the featured roles. No pick means the recommended 5-8.
- **"go", "looks good", or no steer:** proceed with the lineup as presented.

Re-run `news.py check` after any edit. kvn's edits here are final: do not reinstate a vetoed item at draft time.

---

## Step 3: Write the draft

Generate the sections, then write around them:

```bash
python3 scripts/news.py render --file editions/[DATE]-weekly/news.json --jobs editions/[DATE]-weekly/jobs.json
```

`render` prints every non-empty section in order, fundraises tiered by size and sorted by amount, each item with its company name bolded, then a closing `<!-- Week in numbers -->` comment for the intro. Paste the sections into the draft as they are and leave the comment out. Fix wording in news.json and re-render, not in the draft, so the newsletter and the News Tracker never disagree.

Use this exact structure:

### Metadata block (top of draft, not part of the published body)

```
**Subject Line Options**
1. [Best]
2. [Second]
3. [Third]

**SEO Description**
[One sentence, 160 chars max] ([N] chars)
```

Subject lines: 🪙 plus 2-6 words drawn from the week's biggest item (largest round, biggest acquisition, or the move everyone will talk about), like "🪙 Visa buys a stablecoin shop". At least the first option carries a searchable named entity, since it doubles as the indexed post title.

SEO description: names 2-3 of the week's biggest items in plain language, includes "stablecoin" or "payments", no clickbait, ends with a period, never repeats the subject line. Confirm the character count.

### Body

```
---
[SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
---
```

**Intro (40-70 words, no header).** The week in numbers with comparison context ("$412M across 14 rounds, double last week's total"), then the one development that matters most and why, in a sentence. One light line allowed. Every figure matches the `news.py` stats line.

**📊 THE NUMBERS.** A three-column table (Metric, Value, Note) with six rows: total stablecoin market cap, USDT supply, USDC supply, raised this week (total and round count), biggest round, new roles tracked. Notes carry the as-of date, source, and any comparison.

**The news sections**, exactly as `render` printed them. Section order: 💰 Fundraising, 🤝 M&A, 🔄 People moves, ⚖️ Regulation & licensing, 🚀 Launches, 🔗 Partnerships, 📉 Layoffs & shutdowns, 📌 Also notable. Only sections that earned items appear. No intro sentence under any header; the header does that job.

```
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
```

Slot 2 sits directly after 💰 FUNDRAISING.

**💼 WHO'S HIRING (5-8 bullets).** One role per bullet, 20 words or fewer: "**Company** is hiring a [Role title](apply URL) in Location (salary when disclosed)." Link straight to the posting.

**⏳ WORTH YOUR TIME (0-3 bullets, optional).** Reports, filings or long reads from the week on deals, payments or regulation, 20 words or fewer each, link on the title. Confirm the publish date on the source itself. Never re-link a URL already used above. Skip the section rather than recommend something weak.

**Sign-off (1-2 lines, no header).** A point of view on the week, a question, or a tease for next week. Not a summary. Check the sign-offs of the last 2 editions (tail of their draft.md) and don't reuse the same structural formula back to back.

Save to `editions/[DATE]-weekly/draft.md`.

---

## Step 4: Quality check

Run before publishing. Fix all failures first. Check each item against the actual draft text and the source pages, link by link, not from memory of what was intended while writing.

```bash
python3 scripts/news.py check --file editions/[DATE]-weekly/news.json
python3 scripts/news.py lint --draft editions/[DATE]-weekly/draft.md
```

- [ ] `news.py check` reports 0 errors, and its result is logged in the research brief
- [ ] `news.py lint` reports 0 issues: no dashes, no bare URLs, no weak link anchors, no bullet over 20 words
- [ ] No filler phrases from the banned list
- [ ] Every item leads with the company name, has exactly one link on its key phrase, and uses a primary source where one exists; aggregator links are flagged in the brief
- [ ] Every item's underlying event date, confirmed via primary source, falls inside the Monday-Sunday window
- [ ] Every amount, currency, round, lead investor, valuation, person, title, previous employer and license type matches the source page
- [ ] Every deal stage is stated correctly: raised vs raising, agreed vs completed, granted vs applied for
- [ ] Every fundraise sits in the right tier for its USD amount; non-USD conversions are recomputed and their rate source noted
- [ ] No item is a close paraphrase of its source's headline or subhead
- [ ] No event appears in two sections, and a company appears twice only for two distinct events
- [ ] The edition reflects kvn's Step 2 edits: vetoed items are gone, added items carry the same verification
- [ ] Intro figures match the `news.py` stats line; every comparison traces to a source (prior-week totals from the News Tracker, not from recall)
- [ ] Re-do every number derived rather than quoted: totals, round counts, conversions, percentages, "double last week". State the direction correctly too
- [ ] Every named weekday matches its date on the calendar, and every "last month" or "in July" matches the actual date
- [ ] The Numbers table has all six rows with as-of dates
- [ ] Featured roles are in the Jobs Tracker as Open, links go to the live posting, and location and salary match it
- [ ] 3 subject line options, ranked, all starting with 🪙, the first carrying a named entity
- [ ] SEO description present, 160 chars or under, includes "stablecoin" or "payments", does not repeat the subject
- [ ] Sponsor Slot 1 above the intro, Sponsor Slot 2 directly after 💰 FUNDRAISING, placeholders only, never sponsor copy
- [ ] Sign-off is a point of view, not a summary, and doesn't repeat the last edition's closing structure
- [ ] Spot-check that aggregator links resolve; swap to the primary source if one exists. Only 404 and 410 mean dead. Many publishers bot-filter `curl` and return 403 or 429 on pages that load fine in a browser, so confirm with WebFetch before calling a link broken. Never downgrade a working primary source to a weaker one on the strength of a 403

Print: "Weekly done. Research: [path]. Draft: [path]. Items: [N in edition] of [N researched]. Roles added: [N]."

---

## Step 5: Publish to Notion

Run after Step 4 passes. No confirmation needed. Skip this step only if the user asked for a local draft or Notion is unavailable (note it and finish; every command below is safe to re-run later).

1. **News Tracker:** `python3 scripts/news.py push --file editions/[DATE]-weekly/news.json`. It writes every item, in-edition or not, and skips any already tracked (same source URL, or same company, Type and date).
2. **Featured roles:** `python3 scripts/jobs.py feature --ids [Job ID] [Job ID] ...` with the Job IDs from the brief.
3. **The draft page:** create a page under the Stablecoin Brief page (`32b7f3d2-e709-80bf-b981-e69ae10cc902`) with `API-post-page`, titled `DRAFT: [chosen theme] ([Mon D-D, YYYY])` (for example "DRAFT: Visa buys a stablecoin shop (Oct 19-25, 2026)"), icon 🪙. Then write the full draft, metadata block included, into it with `API-update-page-markdown`, `type: "replace_content"`. Fetch the page back with `API-retrieve-page-markdown` and confirm the content landed, since a write can report success while changing nothing.
4. For a later edit to that page, fetch it first and use `update_content` with an `old_str` copied from the fetched markdown, one block at a time. Notion stores its own markup, so text copied from draft.md often won't match: it escapes `$` as `\$` and `[` as `\[`, turns pipe tables into `<table>` blocks, and drops blank lines between blocks. Re-fetch after every edit to verify.

Print: "Notion: [URL of created page]. News Tracker: [N] added. Jobs Tracker: [N] added, [N] closed, [N] featured."

---

## Error handling

- Thin week: ship fewer items and say so in the intro if it's notable; never pad
- A board fails in `jobs.py fetch`: note it in the brief, carry on
- A standing metric unavailable: leave the row with "n/a" and a note, do not guess
- Never fabricate sources, numbers, names, titles or quotes; if a claim can't be verified, omit it and note the gap in the brief
- Never run one event in two sections, and never run an event the trackers or past editions already covered unless it's a genuinely new development in that story
