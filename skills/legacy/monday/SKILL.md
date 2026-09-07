# Monday Big Read Skill

> **DEPRECATED. Not part of the current workflow.**
>
> This skill ran the Monday Big Read edition when Stablecoin Brief published three issues a
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
> 2. It writes to `editions/[YYYY-MM-DD]-monday/`, a folder naming convention no longer
>    used by the weekly pipeline.

## Trigger
Activated when user types: monday
On activation:
1. Read CLAUDE.md in full
2. Detect today's date
3. Create folder: editions/[YYYY-MM-DD]-monday/
4. Begin Step 1 immediately. No prompts. No confirmations.
---
## Step 1: Auto-Pick the Story
Search for stablecoin news and developments from
the past 7 days across all trusted sources in CLAUDE.md.
Evaluate all candidate stories against these criteria:
- Non-obvious angle that most coverage has missed
- Strong data point that reframes the narrative
- Real character or company whose decision drives the story
- Stakes that matter beyond crypto-native audiences
- Has a unique position: something this piece can say
  that other coverage has not said this week
Pick the single strongest story. Do not surface options.
Do not ask for input. Commit to the best story and
proceed immediately to research.
If two stories are genuinely equal, pick the one with
the stronger data point.
---
## Step 2: Deep Research
Research the chosen story thoroughly before writing a
single word of the draft.
Required outputs:
PRIMARY SOURCE
The original source: official announcement, regulatory
filing, earnings transcript, or on-chain data from
Artemis, DeFiLlama, Nansen, or Dune Analytics.
SECONDARY SOURCES (minimum 3)
From trusted sources in CLAUDE.md.
Note what each adds that the primary source does not.
THE NUMBER
The single data point that makes the story real.
Must include comparison context: vs last month, last year,
or a legacy finance equivalent (Visa, ACH, PayPal, SWIFT).
If no strong number exists, note this and find the
closest available proxy.
THE CHARACTER
The specific company, founder, regulator, or institution
whose decision is at the center of the story.
Name them. Describe the decision they made or are facing.
THE COMPLICATION
The fact, counterargument, or nuance that makes the
obvious take on this story incomplete or wrong.
This is what separates a Big Read from a recap.
THE INSIGHT
What does this story actually mean that the headlines
are not saying? Answer in 2-3 sentences.
THE STAKES
Who wins and who loses if this plays out as expected?
Be specific. Name companies or categories.
UNIQUE POSITION
State explicitly in one sentence: what will this piece
say that no other coverage of this story has said?
If this cannot be answered after deep research, note:
"UNIQUE POSITION UNCLEAR" in the brief and proceed
with the strongest available angle.
INLINE HYPERLINKS
Every citation is embedded into natural anchor text
within the sentence. Never append a floating source
tag at the end of a sentence.
Wrong: "...scraped 73,000 pages per visitor. [Cloudflare](url)"
Right: "[Cloudflare's own data](url) showed that AI
crawlers scraped 73,000 pages per visitor."
Wrong: "...on March 18. [Fortune](url) Day-one partners..."
Right: "...and [launched Tempo's mainnet and MPP](url)
on March 18."
The hyperlink anchor should be the most specific
meaningful phrase in the sentence: an action verb,
a company name doing something, a data point, or
the name of the source as a subject. Never link
a generic word like "here" or "this."
ALL SOURCE URLS
List every URL used.
Save to: editions/[YYYY-MM-DD]-monday/research-brief.md
Format:
---
# Research Brief: [Working Headline]
Date: [DATE]
## Story Selected and Why
## Primary Source
## Secondary Sources
## The Number
## The Character
## The Complication
## The Insight
## The Stakes
## Unique Position
## All Source URLs
---
Proceed immediately to Step 3. No confirmation needed.
---
## Step 3: Write the Draft
Write the complete Monday Big Read using the
research brief. Do not summarize. Do not recap.
Write the full publish-ready piece.
STRUCTURE:
SUBJECT LINE OPTIONS
Provide 3, ranked best to worst.
This is the Substack post title and the email subject
line — they are the same field. It is also what Google
indexes when the post is published. Optimize for both:
carry the primary keyword AND earn the email open.
Target 60-70 characters. Lead with the primary keyword
(product name, company name, or core topic), then layer
in the tension, counterintuitive angle, or complication.
Both signals matter equally.
Wrong: "The stablecoin that hides itself"
(punchy but no searchable keywords)
Wrong: "Circle Payments Network Managed Payments Launch 2026"
(keywords but no hook)
Right: "Circle Payments Network Is Hiding Stablecoins Inside Bank Wires"
(primary keyword front-loaded, tension intact)
The chosen subject line sits above the sponsor slot
as the post title. It is not repeated inside the body.
SEO DESCRIPTION (up to 160 characters)
One sentence, 160 characters maximum.
This is the Substack post subtitle and the email
preview text — the line readers see under the subject
line before they open. Make it earn the click.
Tease the counterintuitive angle or the complication.
Do not summarize. Do not repeat the subject line.
Not: "A look at Cloudflare's new stablecoin, NET Dollar."
Yes: "Everyone wrote 'Cloudflare launches stablecoin.'
Six months later, the token doesn't exist.
The strategy behind it is worth understanding."
Always confirm character count is 160 or under.
OUTPUT FORMAT FOR SUBJECT OPTIONS + SEO DESCRIPTION
These must appear as a dedicated metadata block at the
very top of the Notion page and draft, before the H1
headline and all sponsor slots. Format exactly as:
---
**Subject Line Options**
1. [Best option]
2. [Second option]
3. [Third option]
**SEO Description**
[Description text] ([N] chars)
---
This block is not part of the published body. It is
production metadata for the editor to select from
before scheduling the post.
---
[SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
---
HOOK (100-150 words)
No section header. The piece starts here immediately
after the sponsor slot.
Drop into the most interesting thing immediately.
No scene-setting. No "the stablecoin industry has
been growing." Start with the tension, the number,
the moment, or the absurdity.
Make the reader need to keep reading.
WHAT HAPPENED (200-250 words)
Give this section a witty, story-specific subheading.
Not the generic label. Make it reflect the specific
angle of this week's piece.
Wrong: ## What Happened
Right: ## How to Build a Tollbooth in Four Moves
The facts, clearly and completely.
Specific numbers, specific actors, specific timeline.
Every number cited inline. No padding. No passive voice.
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
WHY IT ACTUALLY MATTERS (250-300 words)
Give this section a witty, story-specific subheading.
Wrong: ## Why It Actually Matters
Right: ## Why This Is Not Actually a Stablecoin Story
The analytical core. What changes? Who benefits,
who is threatened? The non-obvious implication
most coverage is missing. Use legacy finance
comparisons where they add clarity.
This is where the unique position lives.
This is where the reader earns their insight moment.
THE THING NOBODY IS TALKING ABOUT (150-200 words)
Give this section a witty, story-specific subheading.
Wrong: ## The Thing Nobody Is Talking About
Right: ## The Token Is the Least Interesting Part
The complication. The counterargument.
The angle that makes readers feel they got something
extra. Dry wit or a sharp observation welcome here
if it fits naturally. Do not force it. If it does
not fit, do not use it.
WHAT TO WATCH (4-5 bullets, ~100 words total)
Give this section a witty, story-specific subheading.
Wrong: ## What to Watch
Right: ## Four Things Worth Watching
Specific, forward-looking signals. Never generic.
Wrong: "Watch for regulatory developments"
Right: "Whether the OCC grants Circle's national
trust bank charter before Q3, which would change
how USDC reserves are regulated and audited"
THE CLOSER (1-2 sentences)
No section header. The piece ends here.
A point of view. Not a summary. Memorable.
Should feel like the writer has a perspective,
not like the piece ran out of words.
---
## Step 4: Quality Check
Run before saving. Fix all failures before proceeding.
[ ] No em dashes anywhere
[ ] No filler phrases from CLAUDE.md banned list
[ ] Every specific number has an inline citation
[ ] Every claim about a company or person is cited
[ ] No floating source tags at sentence ends —
    all links embedded in natural anchor text
[ ] THE NUMBER has comparison context
[ ] Unique position is expressed clearly in the draft
[ ] 3 subject line options provided, ranked
[ ] Subject line options are 60-70 characters
[ ] Subject line #1 contains the primary keyword
    (product name, company name, or core topic)
[ ] SEO Description present and 160 characters or under
[ ] SEO Description does not repeat the subject line
[ ] Subject options + SEO Description appear as a
    dedicated metadata block at top of Notion page
    and draft, before the H1 headline
[ ] Opener is not a definition or rhetorical question
[ ] Closer is a point of view, not a summary
[ ] All four body sections have witty, story-specific
    subheadings (not the generic template labels)
[ ] HOOK and THE CLOSER have no section headers
[ ] Slot 1 placeholder: between subject line and hook
[ ] Slot 2 placeholder: between What Happened and
    Why It Actually Matters
[ ] Word count: 800-1500 words
Save to: editions/[YYYY-MM-DD]-monday/draft.md
Print to terminal:
"Monday done.
Research: editions/[YYYY-MM-DD]-monday/research-brief.md
Draft: editions/[YYYY-MM-DD]-monday/draft.md
Word count: [N] words"
---
## Step 5: Publish to Notion
Run after Step 4 passes. No confirmation needed.

NOTION STRUCTURE
Stablecoin Brief > Monday > [Month YYYY] > [YYYY-MM-DD]

Monday page ID: 32b7f3d2-e709-80fa-916b-c571ee4728fb

1. Fetch the Monday page using the ID above.
2. Find the subpage matching the current month name
   (e.g. "April 2026"). If it does not exist, create it
   as a child of the Monday page before proceeding.
3. Create a new page under the month page:
   - Title: [YYYY-MM-DD] (the upcoming Monday's date)
   - Content: the full draft in Notion Markdown

CONTENT FORMAT
Match the structure of existing Monday editions exactly:
- Metadata block (Subject Line Options + SEO Description)
  as bold text, no heading, at the very top
- ## [SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
- Hook text (no section header)
- ## [Story-specific What Happened subheading]
- ## [SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
- ## [Story-specific Why It Matters subheading]
- ## [Story-specific The Thing Nobody Is Talking About subheading]
- ## [Story-specific What to Watch subheading]
- Closer (no section header)

Print to terminal:
"Notion: [URL of created page]"
---
## Error Handling
- No strong story found: pick the best available,
  note the limitation at the top of the research brief
- Primary source not found: note what was used instead
- Unique position unclear: flag in brief, proceed with
  strongest available angle, note the gap
- Never fabricate sources, numbers, or quotes
- Unverifiable claim: omit and note the gap in the brief
