---
name: weekly
description: Produce the weekly issue of Stablecoin Brief, the newsletter covering stablecoins and payments. Use this whenever kvn types "weekly", asks to "run the weekly", "write this week's issue", "create the Stablecoin Brief", "draft the newsletter", or mentions producing, drafting, or publishing any Stablecoin Brief issue, even casually ("let's do this week's brief", "newsletter time"). The skill runs the full pipeline, research the past week, present a ranked shortlist for kvn to pick the highlight story, write the issue in the weekly format (one deep-dive highlight story plus a bulleted roundup), quality check, publish to Notion. Do not write a Stablecoin Brief issue without this skill.
---

# Stablecoin Brief: Weekly Issue

One issue per week. Format: Morning Brew tone, one deep-dive highlight story (The Big One), then LegalTech Fund style bulleted news (The Roundup). This skill replaces the old monday/wednesday/friday skills.

## On activation

1. Detect today's date. The coverage window is the most recent complete Monday through Sunday. If today is mid-week and the user clearly wants the current week, use Monday through today instead.
2. Create folder: `editions/[YYYY-MM-DD]-weekly/` (dated to the upcoming or current Tuesday, the send day).
3. Begin Step 1 immediately, with no preamble and no confirmation of scope. If the user supplied a specific date range, use that instead of the default window.
4. The pipeline runs unattended except for one gate: Step 2 presents a shortlist and waits for kvn to pick The Big One. Every other step runs straight through.

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
- Never mirror a source's own headline or subhead closely enough that a Roundup or Worth Your Time bullet reads like a paraphrase of it. Same facts, this newsletter's own sentence structure and word choices, every time.
- Avoid stacking two finite verbs back to back around a date or citation (e.g. "study published July 30 mystery-shopped 200 transfers"). Break it into a clause instead: "mystery-shopped 200 transfers... in a study published July 30."

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
Prefer primary sources over aggregators. If only an aggregator covers a story, use it but flag it in the research brief so the editor can swap the link. When a fact is covered by both a primary/company source (e.g. Circle's own blog) and an SEO-farm aggregator, use the primary source even if the aggregator's copy reads better: aggregator URLs (news-mill sites in particular) go dead more often.

---

## Step 1: Research

Research everything before writing a word. Five workstreams:

Two checks apply to every candidate in every workstream below, by default, not only when asked:

- **Verify the real event date via primary source.** Web search summaries blend an older event with newer follow-up coverage (a rule published one week gets analysis coverage the next, which then reads as "this week's news" in search results). Before including any story, fetch the primary source and confirm the underlying event actually happened inside the Monday-Sunday coverage window, not just that some article discussing it was published in-window.
- **Grep every past edition, not just the 1-2 most recent.** Run `grep -ril "<term>" editions/*/draft.md editions/*/research-brief.md` for each candidate's key terms (company, protocol, ticker) before it's allowed into the brief. A story can recur as a slow-building saga across non-adjacent editions weeks apart (a licensed issuer's launch covered at "targeted for next quarter," then "on track for later this year," then "launched"), where each mention reads like fresh news in isolation and only a full-archive search catches the pattern.

### A. The Big One (highlight story)

Search the coverage window across trusted sources. Evaluate candidates against:

- A non-obvious angle most coverage has missed
- A strong data point that reframes the narrative
- A real character or company whose decision drives the story
- Stakes that matter beyond crypto-native audiences
- A unique position: something this piece can say that other coverage has not said this week

Rank every candidate that clears the bar and carry the strongest 3-4 forward as the shortlist for Step 2. Do not pick one and start writing: the pick is kvn's.

Research each shortlisted candidate far enough to make the choice real, but no further. For each, get: the angle in one line, the headline data point, the primary source, and any caveat the pick should account for (thin sourcing, a company that ran recently, an event date that only just clears the window). Both default checks above apply to every shortlisted candidate before it reaches the shortlist, so kvn is never choosing a story that turns out to be out of window or already covered.

The full deep dive happens only on the story kvn picks. After the pick, gather for that story: the primary source, at least 3 secondary sources, THE NUMBER (with comparison context), THE CHARACTER (named, with the decision they made or face), THE COMPLICATION (what makes the obvious take incomplete), THE STAKES (who wins, who sweats, named), and the UNIQUE POSITION in one sentence. If the unique position is unclear after real research, note "UNIQUE POSITION UNCLEAR" and proceed with the strongest angle.

### B. The Roundup (8-12 items)

Find distinct stablecoin and payments news items from the window, excluding whatever The Big One covers. For each: headline, key fact (the number or detail that matters), why a stablecoin reader cares (one sentence), source name and URL. Rank by newsworthiness. Assign each to one of: Regulation and policy, Infrastructure and launches, Adoption and partnerships, Money moves (funding, M&A). Use only the 2-4 groups that earned items this week; never pad a group.

### C. The Numbers

Gather the week's readings for the standing metrics table: total stablecoin market cap, USDT supply, USDC supply, Bitcoin price (with YTD move), Nasdaq (with YTD move), and Circle stock CRCL (most recent close). Pull market cap and supplies from DeFiLlama or equivalent; note the as-of date for each. If a metric had a newsworthy move this week (a downgrade, a spike), say so in its note cell.

### D. Worth Your Time (2-4 picks)

Longer-form pieces published this week: research reports, essays, policy papers, podcasts. Each must be genuinely worth the reader's Saturday morning; if nothing strong exists, run fewer picks rather than recommending a weak one. For audio, note the duration. None of these picks may reuse a URL already cited in The Big One or The Roundup: Worth Your Time exists to surface a different read, not to re-link a story the reader already saw above. Confirm the publish date on the source itself, not on a search snippet describing it, before counting it as this week's.

### E. Duplicate check

Before finalizing story selection, grep the full archive for every candidate still in play (see the two default checks above). Log the result, even when it's a clean pass. Any confirmed duplicate or near-duplicate gets cut or swapped, not run a third time with a new headline.

Save everything to `editions/[YYYY-MM-DD]-weekly/research-brief.md`:

```
# Weekly Research Brief
Date: [DATE] | Coverage: [MON] to [SUN]

## The Big One
### Candidates shortlisted (ranked)
[for each: the angle in one line / the headline data point / primary source URL / the caveat]
### Selected
[which candidate, whether kvn picked it or it ran as the default, and why]
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
[one-line reason each, including any candidate cut for failing the date-verification or duplicate check]

## Duplicate check performed
[terms searched, folders covered, and the result: confirmed clean, or what was cut/swapped and why]

## Aggregator links to swap
[any non-primary sources used]
```

Save the brief with the full ranked candidate list before presenting the shortlist. Then go to Step 2.

---

## Step 2: Shortlist and pick

This is the pipeline's only stop. Present the shortlist in chat and wait. Do not write a draft before kvn picks.

Present, in this order:

1. **The Big One candidates, 3-4, ranked.** For each: a one-line statement of the angle (not the headline the source used), the strongest data point, and the caveat. Mark the top-ranked one as the recommendation and say in one sentence why it leads. Keep each candidate to about three lines; this is a menu, not a briefing.
2. **The Roundup lineup**, compact, one line per item under its group header. kvn can veto items, add one, or promote one to The Big One from here.
3. **Judgment calls worth surfacing**, only when there are any: a company or theme that ran as The Big One in a recent edition, a candidate whose sourcing is thin, a near-duplicate that was handled rather than cut, two candidates that are really the same story.

Then stop and wait for the pick.

Handling the response:

- **kvn picks a candidate:** run the full deep dive on it (see Step 1A), record the selection in the brief, and proceed to Step 3.
- **kvn picks a Roundup item:** promote it, run the full deep dive on it, and backfill its Roundup slot from the discarded pile or fresh research. Roundup drops to as few as 8 items rather than running a padded one.
- **kvn says "you pick", "go", or gives no steer:** use the top-ranked candidate and proceed. Note in the brief that it ran as the default rather than as an explicit pick.
- **kvn rejects the whole shortlist:** go back to Step 1 workstream A for more candidates. Do not force a weak story through because the shortlist is spent.
- **kvn picks a story and adds an angle:** the angle is the instruction. Research it, and if the reporting does not support it, say so plainly before drafting rather than writing around the gap.

Any Roundup edits kvn makes here are final. Do not reinstate a vetoed item at draft time.

---

## Step 3: Write the draft

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

The Big One gets the same organic inline citations as the Roundup, not fewer. Every factual claim, not just the ones in "By the numbers," needs a link embedded on its key phrase the first time it's stated: the announcement itself, the headline stat, the comparison figure, any named-source detail (an executive quote, a missing-detail complication, a competitive threat). Pull the links straight from the research brief's primary/secondary sources for that story. Don't link the same claim twice in one section, and don't force a citation onto a claim that's pure analysis or opinion (the "why it matters" connective tissue doesn't need one, the facts underneath it do). If a claim in the draft has no source behind it, either find one or cut the claim; never publish an uncited factual assertion just because it sounds plausible.

```
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
```

**🗞️ THE ROUNDUP (8-12 bullets).** Grouped under the earned themed sub-headers: ⚖️ Regulation and policy, 🏗️ Infrastructure and launches, 🤝 Adoption and partnerships, 💰 Money moves. Bullet formula: [what happened, link embedded on the key phrase] plus one clause of context or why it matters. One to two sentences, hard stop. No intro sentence before the bullets; the header does that job.

Example: "Stripe [expanded stablecoin payouts to 12 new markets](url), bringing its total coverage to 70 countries and putting more pressure on legacy cross-border rails."

**⏳ WORTH YOUR TIME (2-4 bullets).** Link plus one specific line on what the reader gets, duration for audio. Emoji prefixes fine here. Lighter tone allowed.

**Sign-off (1-2 lines, no header).** One line back to the reader with a point of view, a question, or a tease for next week. Not a summary. Check the sign-offs of the last 2 editions (tail of their draft.md) before writing this one, and don't reuse the same structural formula back to back (e.g. "[Company] just proved X. Next week: watch Y" two weeks running reads as a template, not a voice).

Save to `editions/[YYYY-MM-DD]-weekly/draft.md`.

---

## Step 4: Quality check

Run before publishing. Fix all failures first. Check each item against the actual draft text, paragraph by paragraph and link by link, not from memory of what was intended while writing: this edition shipped with three uncited Big One paragraphs, a dead link, a near-verbatim Roundup bullet, and a Worth Your Time pick that duplicated a Roundup source, all of which the checklist below would have caught on a literal re-read.

- [ ] No em dashes anywhere
- [ ] No filler phrases from the banned list
- [ ] Every specific number has an inline citation and comparison context
- [ ] The Big One has organic inline citations on its factual claims, same as the Roundup, not just in "By the numbers"
- [ ] All links embedded in natural anchor text, no floating source tags, no "per [Publication]" anchors
- [ ] 3 subject line options, ranked, first one carries a named entity, all start with 🪙
- [ ] SEO description present, 160 chars or under, includes a stablecoin keyword, does not repeat the subject
- [ ] Cold open is 50-80 words with a 3-item preview list
- [ ] Numbers table has all six standing metrics with as-of dates
- [ ] The Big One is 300-450 words with story-specific mini-headers and a point-of-view kicker
- [ ] Roundup bullets are 1-2 sentences each, grouped only under earned headers, no padded groups
- [ ] No story appears in both The Big One and The Roundup, and no source URL appears in both The Roundup and Worth Your Time
- [ ] Roundup and Worth Your Time bullets are written in the newsletter's own words, not close paraphrases of the source's headline or subhead
- [ ] Spot-check any aggregator/SEO-farm links actually resolve (no 404s) before publishing; swap to the primary source if one exists
- [ ] Every Big One, Roundup, and Worth Your Time item's underlying event date, confirmed via primary source, actually falls inside the Monday-Sunday window (not just its coverage)
- [ ] The archive-wide duplicate grep was run this edition and its result is logged in the research brief, not skipped or assumed clean
- [ ] The Big One is the story kvn picked at Step 2, any Roundup items kvn vetoed are gone, and the brief records the shortlist alongside the selection
- [ ] One joke per section maximum
- [ ] Sponsor Slot 1 above the cold open, Sponsor Slot 2 between The Big One and The Roundup, placeholders only, never write sponsor copy
- [ ] Sign-off is a point of view, not a summary, and doesn't repeat the last edition's closing structure
- [ ] Total body 900-1,400 words excluding sponsor slots and metadata

Print: "Weekly done. Research: [path]. Draft: [path]. Word count: [N]."

---

## Step 5: Publish to Notion

Run after Step 4 passes. No confirmation needed. Skip this step only if the user asked for a local draft or Notion is unavailable (note it and finish).

Stablecoin Brief page ID: `32b7f3d2-e709-80bf-b981-e69ae10cc902`

1. Create a new page directly under the Stablecoin Brief page.
2. Title: `DRAFT: [chosen theme] ([Mon D-D, YYYY])`, for example "DRAFT: Visa builds the plumbing (Jul 13-19, 2026)". Icon: 🪙
3. Content: the full draft including the metadata block, matching the draft exactly.
4. Notion stores tables in its own markup. If a post-publish edit to the table is ever needed, fetch the page first and match the stored format exactly rather than resending pipe-table markdown.
5. For any other post-publish edit, fetch the page first and match content_updates old_str to a single block at a time. Notion joins blocks with single newlines, not blank-line-separated paragraphs, so an old_str spanning multiple paragraphs with `\n\n` between them will silently fail to match (the tool can report success even when zero blocks changed). Verify by re-fetching the page after every edit rather than trusting the tool's response alone.

Print: "Notion: [URL of created page]"

---

## Error handling

- No strong Big One candidate: pick the best available and note the limitation at the top of the research brief
- Fewer than 8 roundup items: use what exists, note the gap; never pad
- A standing metric unavailable: leave the row with "n/a" and a note, do not guess
- Never fabricate sources, numbers, or quotes; unverifiable claim: omit it and note the gap in the brief
- Never duplicate a story between The Big One and The Roundup
