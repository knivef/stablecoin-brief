# Wednesday Signal Skill

> **DEPRECATED. Not part of the current workflow.**
>
> This skill ran the Wednesday Signal edition when Stablecoin Brief published three issues a
> week. On 2026-07-21 the newsletter moved to a single weekly issue, and this skill was
> retired. The active pipeline is `skills/weekly/SKILL.md`, invoked with `/weekly`.
>
> Kept for reference and for the rare case of resurrecting the old cadence. Two things to
> know before running it:
>
> 1. It instructs "Read CLAUDE.md in full" and expects the Monday/Wednesday/Friday-era master context,
>    including the old sponsor slot placement and the 48-72 hour or 7-day story windows.
>    If `CLAUDE.md` has since been rewritten for the weekly cadence, this skill will not
>    behave as written.
> 2. It writes to `editions/[YYYY-MM-DD]-wednesday/`, a folder naming convention no longer
>    used by the weekly pipeline.

## Trigger
Activated when user types: wednesday
On activation:
1. Read CLAUDE.md in full
2. Detect today's date
3. Create folder: editions/[YYYY-MM-DD]-wednesday/
4. Begin Step 1 immediately. No prompts. No confirmations.
---
## Step 1: Research
Search for stablecoin news from the past 48-72 hours
across all trusted sources in CLAUDE.md.
Find 6-8 distinct news items. For each:
HEADLINE: What happened, one sentence
KEY FACT: The single most important number or detail
WHY IT MATTERS: Why a stablecoin reader should care,
one sentence
SOURCE NAME: Publication or platform
SOURCE URL: Direct link
Rank all items by:
1. Recency and newsworthiness
2. Relevance specifically to stablecoin readers
3. Availability of a concrete number or fact
Identify the week's dominant theme or signal from
the top stories. Name it in one sentence.
This becomes the framing for the intro.
Save to: editions/[YYYY-MM-DD]-wednesday/research-brief.md
Format:
---
# Signal Research Brief
Date: [DATE]
Week's Dominant Theme: [ONE SENTENCE]
## Ranked Story List
RANK 1
HEADLINE:
KEY FACT:
WHY IT MATTERS:
SOURCE:
URL:
[repeat for all items]
## Discarded Items
[list with one-line reason for each]
---
Proceed immediately to Step 2.
---
## Step 2: Write the Draft
Use the top 4-6 items from the ranked research list.
STRUCTURE:
SUBJECT LINE OPTIONS
Provide 3, ranked best to worst.
Each subject line must work as both an email open hook
AND an SEO-friendly article title for the Substack
web version (which gets indexed by Google).
SEO RULES FOR SUBJECT LINES:
- 55-70 characters
- Lead with a primary keyword: the most searchable
  entity or development (company name, regulation,
  stablecoin name, market stat)
- Include at least one named entity (USDC, USDT,
  GENIUS Act, Circle, Tether, MiCA, BIS, etc.)
- Specific beats clever: "FDIC Sets GENIUS Act
  Stablecoin Rules" outranks "Washington Finally
  Did Something" for search
- Numbers and proper nouns improve ranking signal
Not: "This week in stablecoins"
Not: "The USDC flip nobody saw coming" (no keyword signal)
Yes: "USDC Gains Ground: Pornhub, FDIC Rules, 12-Bank Euro Token"
Yes: "BIS Flags $320B Stablecoin Market as Systemic Risk"
Yes: "Tether Loses Market Share as GENIUS Act Moves to Markup"
META DESCRIPTION
One line, 140-160 characters. Appears in Google search
results for the Substack web version. Write it after
locking the subject lines.
- Must include the word "stablecoin" or a stablecoin
  name (USDC, USDT, GENIUS Act, MiCA, etc.)
- Summarize 2-3 of the top stories in plain language
- No clickbait. No filler. Reads like a search snippet.
- End with a period.
Not: "This week's stablecoin signal has everything."
Yes: "BIS flags $320B stablecoin market as systemic risk,
     12 banks launch a MiCA euro token, and FDIC sets
     GENIUS Act redemption rules." (155 chars)
Add to quality check: [ ] Meta description is 140-160
characters and includes a primary stablecoin keyword
---
[SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
---
SIGNAL (section header)
INTRO (2 sentences max)
Name the week's dominant theme.
No throat-clearing. Get to the news immediately after.
NEWS SNIPPETS (4-6 items)
Each snippet has a bold headline (not hyperlinked),
followed by 2-4 sentences with inline source links.
SEO RULES FOR SNIPPET HEADLINES:
Snippet headlines are indexed on the Substack web
version. Write them to rank, not just to hook.
- Format: [Entity] + [Action] + [Key Detail/Number]
- Include the company name, regulation name, or
  stablecoin name — not a pronoun or vague noun
- Include a specific number or outcome where possible
- 55-70 characters is the target range
Not: "The Banks Are Moving" (no entities, no specifics)
Not: "FDIC Drops Rules" (too vague, no keyword value)
Yes: "FDIC Proposes GENIUS Act Stablecoin Rules: 2-Day Redemption Window"
Yes: "12 European Banks Launch MiCA-Compliant Euro Stablecoin via Fireblocks"
Yes: "Pornhub Switches Stablecoin Payouts from USDT to USDC"
- Bold headline: what happened, plain text, no link
- 2-4 sentences: what happened, the key number,
  why it matters
- Every snippet must have at least one inline link
  anchored to a meaningful phrase: a company doing
  something, an action verb, or a data point
- Never link a generic word like "here", "this",
  "report", or "announced"
- Never use "per [Publication]" or "according to
  [Source]" as the link anchor — link the claim,
  not the attribution
- No floating source tags at sentence ends
- No padding. No filler. Get in, deliver the fact,
  get out.
Wrong: **[Nium Launches Stablecoin Card Platform](url)**
       Nium launched a platform on March 30...
Right: **Nium Launches Stablecoin Card Platform**
       Nium [launched a stablecoin card issuance
       platform](url) on March 30, letting businesses...
Wrong: ...cutting time-to-market from months to days. [Nium](url)
Right: ...the company says the platform [cuts time-to-market
       from months to days](url).
Wrong: ...the language is "overly narrow," per [CoinDesk](url).
Right: ...the industry [called the language "overly
       narrow"](url) within hours of the draft's release.
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
QUICK HITS (2-3 smaller items)
Format: • [What happened, link anchored to the key
  action or data point] → [why it matters, 10 words max]
No trailing source tags. Link lives inside the hit itself.
Wrong: ...comment period extended to May 18. ([FDIC](url))
Right: FDIC [extends comment period to May 18](url) →
       banks get 90 more days on stablecoin rules
CLOSER (1-2 sentences)
A point of view. Not a summary. Not a tease for
the next edition. The reader should finish with a
clear sense of what this week's signal actually means.
Wrong: "Monday's piece goes inside the Clarity Act..."
Right: "A deal nobody loves has a better chance of
       surviving markup than one side's perfect draft."
---
## Step 3: Quality Check
[ ] No em dashes
[ ] No filler phrases
[ ] 3 subject line options provided, ranked
[ ] Each snippet is 2-4 sentences only, no exceptions
[ ] Every snippet headline is plain bold (not hyperlinked)
[ ] Every snippet has at least one inline source link anchored to a meaningful phrase
[ ] Slot 1: between subject lines and intro
[ ] Slot 2: between 3rd and 4th snippet
[ ] Quick Hits are genuinely short (10 words max each)
[ ] Closer is a point of view, not a summary or next-edition tease
[ ] Total body: 300-500 words excluding sponsor slots
Save to: editions/[YYYY-MM-DD]-wednesday/draft.md
Print to terminal:
"Wednesday done.
Research: editions/[YYYY-MM-DD]-wednesday/research-brief.md
Draft: editions/[YYYY-MM-DD]-wednesday/draft.md
Snippets used: [N] of [N] researched"
---
## Error Handling
- Fewer than 4 strong items: use what exists, note
  the gap at the top of the research brief
- Never pad a snippet to hit a sentence count
- Unverifiable item: drop it, note it in discarded list
- Never duplicate stories covered in Monday's edition
  this week. Check editions/ folder for the Monday
  draft before finalising the snippet list.
