---
name: weekly
description: Produce the weekly issue of Stablecoin Brief, the newsletter covering stablecoins and payments. Use this whenever kvn types "weekly", asks to "run the weekly", "write this week's issue", "create the Stablecoin Brief", "draft the newsletter", or mentions producing, drafting, or publishing any Stablecoin Brief issue, even casually ("let's do this week's brief", "newsletter time"). The skill runs the full pipeline, research the past week, write the issue in the weekly format (one deep-dive highlight story plus a bulleted roundup), quality check, publish to Notion. Do not write a Stablecoin Brief issue without this skill.
---

# Stablecoin Brief: Weekly Issue

One issue per week. Format: Morning Brew tone, one deep-dive highlight story (The Big One), then LegalTech Fund style bulleted news (The Roundup). This skill replaces the old monday/wednesday/friday skills.

## On activation

1. Detect today's date. The coverage window is the most recent complete Monday through Sunday. If today is mid-week and the user clearly wants the current week, use Monday through today instead.
2. Create folder: `editions/[YYYY-MM-DD]-weekly/` (dated to the upcoming or current Tuesday, the send day).
3. Begin Step 1 immediately. No prompts, no confirmations. If the user supplied a specific date range, use that instead of the default window.

## Audience and voice

Readers are financially literate and crypto-aware. They know what USDC, USDT, on-chain settlement, and the GENIUS Act are. Do not explain basics. The bar for every issue: the reader finishes thinking "I did not know that" or "I had not thought about it that way."

The voice is Morning Brew applied to serious research: casual, conversational, written to one reader ("you") with contractions, like a smart friend explaining the news over coffee. Jokes are woven into hard news but never at the expense of accuracy, and never more than one joke per section. Humor seasons the news; it is not the meal. Every claim is attributed inline. Sections end with a kicker, a light one-liner that lands the point, not a summary.

### Style rules (non-negotiable)

- No em dashes
- No filler: "it remains to be seen", "in the ever-evolving landscape", "as the industry matures", "going forward", "at the end of the day", "significant milestone", "it is worth noting"
- No corporate jargon, no rhetorical question openers, no definition openers, no passive voice where avoidable
- Paragraphs are 1-3 sentences. Bullets are 1-2 sentences. Hard stops.
- All numbers need comparison context (vs last month, last year, or a legacy finance equivalent like Visa, ACH, SWIFT)
- Every citation is an inline hyperlink embedded in natural anchor text: link the claim, not the attribution. The anchor is the most specific meaningful phrase in the sentence (an action, a company doing something, a data point). Never link "here", "this", "report", or "announced". Never use "per [Publication]" as the anchor. No floating source tags at sentence ends.
- Bold is for mini-headers and lead-in phrases only, not mid-sentence emphasis

Wrong: "...scraped 73,000 pages per visitor. [Cloudflare](url)"
Right: "[Cloudflare's own data](url) showed that AI crawlers scraped 73,000 pages per visitor."

## Content pillars (priority order)

1. Regulation: GENIUS Act, MiCA, Treasury, OCC, tax treatment
2. Issuer dynamics: USDC, USDT, yield-bearing coins, bank-issued tokens, new entrants
3. Payments infrastructure: Visa, Mastercard, on/off ramps, B2B settlement
4. Institutional adoption: treasury management, RWA tokenization, corporate uptake
5. Emerging markets: remittances, cross-border, EM adoption
6. Technology and protocol: mechanisms, de-peg events, chain-level shifts

## Trusted sources

Primary: Artemis, DeFiLlama, Nansen, Dune Analytics, official company blogs, regulatory filings, earnings transcripts, on-chain data.
Secondary: CoinDesk, The Block, Bloomberg, Reuters, FT, WSJ, Axios, Decrypt, Bankless, a16z crypto research, Fed publications, BIS papers, analyst reports.
Prefer primary sources over aggregators. If only an aggregator covers a story, use it but flag it in the research brief so the editor can swap the link.

---

## Step 1: Research

Research everything before writing a word. Four workstreams:

### A. The Big One (highlight story)

Search the coverage window across trusted sources. Evaluate candidates against:

- A non-obvious angle most coverage has missed
- A strong data point that reframes the narrative
- A real character or company whose decision drives the story
- Stakes that matter beyond crypto-native audiences
- A unique position: something this piece can say that other coverage has not said this week

Pick the single strongest story. Do not surface options or ask for input. If two are genuinely equal, pick the one with the stronger data point. For the chosen story gather: the primary source, at least 3 secondary sources, THE NUMBER (with comparison context), THE CHARACTER (named, with the decision they made or face), THE COMPLICATION (what makes the obvious take incomplete), THE STAKES (who wins, who sweats, named), and the UNIQUE POSITION in one sentence. If the unique position is unclear after real research, note "UNIQUE POSITION UNCLEAR" and proceed with the strongest angle.

### B. The Roundup (8-12 items)

Find distinct stablecoin and payments news items from the window, excluding whatever The Big One covers. For each: headline, key fact (the number or detail that matters), why a stablecoin reader cares (one sentence), source name and URL. Rank by newsworthiness. Assign each to one of: Regulation and policy, Infrastructure and launches, Adoption and partnerships, Money moves (funding, M&A). Use only the 2-4 groups that earned items this week; never pad a group.

### C. The Numbers

Gather the week's readings for the standing metrics table: total stablecoin market cap, USDT supply, USDC supply, Bitcoin price (with YTD move), Nasdaq (with YTD move), and Circle stock CRCL (most recent close). Pull market cap and supplies from DeFiLlama or equivalent; note the as-of date for each. If a metric had a newsworthy move this week (a downgrade, a spike), say so in its note cell.

### D. Worth Your Time (2-4 picks)

Longer-form pieces published this week: research reports, essays, policy papers, podcasts. Each must be genuinely worth the reader's Saturday morning; if nothing strong exists, run fewer picks rather than recommending a weak one. For audio, note the duration.

Save everything to `editions/[YYYY-MM-DD]-weekly/research-brief.md`:

```
# Weekly Research Brief
Date: [DATE] | Coverage: [MON] to [SUN]

## The Big One
### Story selected and why
### Primary source
### Secondary sources
### The Number / The Character / The Complication / The Stakes
### Unique position

## Roundup (ranked, grouped)
[headline / key fact / why it matters / source + URL for each]

## The Numbers
[metric: value, as-of date, source, note]

## Worth Your Time
[title, author, publication, URL, why read it, duration if audio]

## Discarded items
[one-line reason each]

## Aggregator links to swap
[any non-primary sources used]
```

Proceed immediately to Step 2.

---

## Step 2: Write the draft

Write the complete publish-ready issue. Use this exact structure:

### Metadata block (top of draft, not part of the published body)

```
**Subject Line Options**
1. [Best]
2. [Second]
3. [Third]

**SEO Description**
[One sentence, 160 chars max] ([N] chars)
```

Subject lines: format is 🪙 plus a short punchy theme drawn from The Big One, 2-6 words after the emoji (like "🪙 Visa builds the plumbing"). At least the first option must carry a searchable named entity (company, regulation, or stablecoin name), since this doubles as the indexed post title. Specific beats clever; wordplay welcome when it keeps the keyword.

SEO description: teases the angle or names 2-3 top stories in plain language, includes "stablecoin" or a stablecoin name, no clickbait, ends with a period, never repeats the subject line. Confirm the character count.

### Body

```
---
[SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
---
```

**Cold open (50-80 words, no header).** One surprising stat or fact from the week, delivered with a light joke. Then:

**In this week's brief:**

- Highlight story teaser
- Second most important theme
- Third item or the fun one

**📊 THE NUMBERS.** A three-column table (Metric, Value, Note) with the six standing metrics from research workstream C. Notes carry the as-of date, source, and any newsworthy context.

**💥 THE BIG ONE (300-450 words).** The deep dive:

1. A punchy story-specific headline as a subheading, wordplay welcome
2. Hook, 2-3 sentences: what happened and why the reader cares, one joke allowed
3. 3-4 bolded mini-headers that move the story forward. Make them story-specific, not generic labels. "**The backstory:**", "**Who wins, who sweats:**", "**What's next:**" are fine defaults, but prefer headers written for this story (like "**The OUSD angle:**")
4. A "**By the numbers:**" block with stats as short bullets, each attributed
5. Kicker: one closing line with a point of view

```
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
```

**🗞️ THE ROUNDUP (8-12 bullets).** Grouped under the earned themed sub-headers: ⚖️ Regulation and policy, 🏗️ Infrastructure and launches, 🤝 Adoption and partnerships, 💰 Money moves. Bullet formula: [what happened, link embedded on the key phrase] plus one clause of context or why it matters. One to two sentences, hard stop. No intro sentence before the bullets; the header does that job.

Example: "Stripe [expanded stablecoin payouts to 12 new markets](url), bringing its total coverage to 70 countries and putting more pressure on legacy cross-border rails."

**⏳ WORTH YOUR TIME (2-4 bullets).** Link plus one specific line on what the reader gets, duration for audio. Emoji prefixes fine here. Lighter tone allowed.

**Sign-off (1-2 lines, no header).** One line back to the reader with a point of view, a question, or a tease for next week. Not a summary.

Save to `editions/[YYYY-MM-DD]-weekly/draft.md`.

---

## Step 3: Quality check

Run before publishing. Fix all failures first.

- [ ] No em dashes anywhere
- [ ] No filler phrases from the banned list
- [ ] Every specific number has an inline citation and comparison context
- [ ] All links embedded in natural anchor text, no floating source tags, no "per [Publication]" anchors
- [ ] 3 subject line options, ranked, first one carries a named entity, all start with 🪙
- [ ] SEO description present, 160 chars or under, includes a stablecoin keyword, does not repeat the subject
- [ ] Cold open is 50-80 words with a 3-item preview list
- [ ] Numbers table has all six standing metrics with as-of dates
- [ ] The Big One is 300-450 words with story-specific mini-headers and a point-of-view kicker
- [ ] Roundup bullets are 1-2 sentences each, grouped only under earned headers, no padded groups
- [ ] No story appears in both The Big One and The Roundup
- [ ] One joke per section maximum
- [ ] Sponsor Slot 1 above the cold open, Sponsor Slot 2 between The Big One and The Roundup, placeholders only, never write sponsor copy
- [ ] Sign-off is a point of view, not a summary
- [ ] Total body 900-1,400 words excluding sponsor slots and metadata

Print: "Weekly done. Research: [path]. Draft: [path]. Word count: [N]."

---

## Step 4: Publish to Notion

Run after Step 3 passes. No confirmation needed. Skip this step only if the user asked for a local draft or Notion is unavailable (note it and finish).

Stablecoin Brief page ID: `32b7f3d2-e709-80bf-b981-e69ae10cc902`

1. Create a new page directly under the Stablecoin Brief page.
2. Title: `DRAFT: [chosen theme] ([Mon D-D, YYYY])`, for example "DRAFT: Visa builds the plumbing (Jul 13-19, 2026)". Icon: 🪙
3. Content: the full draft including the metadata block, matching the draft exactly.
4. Notion stores tables in its own markup. If a post-publish edit to the table is ever needed, fetch the page first and match the stored format exactly rather than resending pipe-table markdown.

Print: "Notion: [URL of created page]"

---

## Error handling

- No strong Big One candidate: pick the best available and note the limitation at the top of the research brief
- Fewer than 8 roundup items: use what exists, note the gap; never pad
- A standing metric unavailable: leave the row with "n/a" and a note, do not guess
- Never fabricate sources, numbers, or quotes; unverifiable claim: omit it and note the gap in the brief
- Never duplicate a story between The Big One and The Roundup
