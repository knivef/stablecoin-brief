# Wednesday Signal Skill
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
Lead with the most interesting fact or tension.
Not: "This week in stablecoins"
Yes: "The USDC flip nobody saw coming"
Yes: "Tether just lost its biggest market share
in four years"
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
- Bold headline: what happened, plain text, no link
- 2-4 sentences: what happened, the key number,
  why it matters
- Every snippet must have at least one inline link
  anchored to a meaningful phrase: a company doing
  something, an action verb, or a data point
- Never link a generic word like "here", "this",
  "report", or "announced"
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
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
QUICK HITS (2-3 smaller items)
Format: • [What happened] → [why it matters, 10 words max]
CLOSER (1 sentence)
Tease Monday's Big Read. Make it sound essential.
Do not reveal the full story. Create curiosity.
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
[ ] Closer teases Monday without giving it away
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
