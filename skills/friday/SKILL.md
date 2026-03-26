# Friday Stat + Snippet Skill
## Trigger
Activated when user types: friday
On activation:
1. Read CLAUDE.md in full
2. Detect today's date
3. Create folder: editions/[YYYY-MM-DD]-friday/
4. Begin Step 1 immediately. No prompts. No confirmations.
---
## Step 1: Research
Gather all three parts before writing anything.
PART 1 — THE STAT
Find the single most striking stablecoin data point
published or updated this week.
Candidate categories:
- Market cap movement (total stablecoin or per issuer)
- Transaction or settlement volume (Artemis, DeFiLlama)
- USDC or USDT supply change
- B2B vs retail payments share shift
- Chain-level stablecoin activity (Solana, Ethereum, BNB)
- RWA tokenization TVL
- On-chain active addresses or unique wallets
- Stablecoin yield rates
Selection criteria:
- Most surprising or significant number of the week
- Has strong comparison context available
- Tells a story on its own, not just a routine update
For the chosen stat gather:
- The number itself
- Primary source verification (Artemis, DeFiLlama,
  Nansen, Dune, or official report)
- Context: this week vs last week, last month, last year
- Legacy finance comparison where applicable
- One sharp observation if the number lends itself
  to wit. If not, skip it. Never force it.
PART 2 — SNIPPETS
Find 4-6 stablecoin news items from the past 48 hours.
Check editions/ folder and exclude any stories already
covered in Monday or Wednesday editions this week.
For each:
HEADLINE: What happened, one sentence
KEY FACT: Most important number or detail
WHY IT MATTERS: One sentence
SOURCE NAME and URL
Rank by newsworthiness.
PART 3 — WEEKEND READ
Find one longer-form piece published this week:
research report, deep analysis, essay, or policy paper.
Must be genuinely worth a reader's Saturday morning.
Not a news recap. Something with depth and shelf life.
If nothing strong was published this week, say so
rather than recommending a weak piece.
Provide:
TITLE:
AUTHOR:
PUBLICATION:
URL:
WHY READ IT: One specific sentence. Not "it covers
important topics." Tell the reader exactly what they
will get from it.
Save to: editions/[YYYY-MM-DD]-friday/research-brief.md
Format:
---
# Stat + Snippet Research Brief
Date: [DATE]
## Part 1: The Stat
### Number and Source
### Comparison Context
### Legacy Finance Equivalent (if applicable)
### Observation (if earned, else leave blank)
## Part 2: Snippets (ranked)
[same format as Wednesday]
## Part 3: Weekend Read
### Title, Author, Publication, URL
### Why Read It
## Stories Excluded (already covered this week)
---
Proceed immediately to Step 2.
---
## Step 2: Write the Draft
STRUCTURE:
SUBJECT LINE OPTIONS (3, ranked)
At least one must lead with the stat.
Example: "Stablecoins just crossed $300B.
Here is what that number actually means."
---
[SPONSOR SLOT 1 — $150 rack / $75 floor — Primary, top of email]
---
THE STAT (section header)
THE NUMBER
Display it prominently. Bold it.
2-3 sentences of context immediately after:
- What it is measuring
- Why this week specifically
- Comparison to prior period or legacy finance
- One dry observation if earned. Skip if not.
---
[SPONSOR SLOT 2 — $100 rack / $50 floor — Mid-content native]
---
THE SNIPPETS (3-4 items from ranked list)
Same format as Wednesday snippets:
- Bold hyperlinked headline
- 2-4 sentences: what happened, key number,
  why it matters
- Source linked inline
WEEKEND READ
One short paragraph.
What it is, who wrote it, why this specific reader
should spend their Saturday morning on it.
Link the title. Be specific, not generic.
CLOSER (1 sentence)
Tease Monday's Big Read. Create curiosity.
Do not reveal the full story.
---
## Step 3: Quality Check
[ ] No em dashes
[ ] No filler phrases
[ ] Stat verified from primary source
[ ] Stat has comparison context and legacy finance
    equivalent where applicable
[ ] Observation in stat section is earned, not forced
[ ] No snippets duplicated from Monday or Wednesday
[ ] All snippets have source links
[ ] Each snippet is 2-4 sentences only
[ ] Weekend Read is substantive, not a recap
[ ] Weekend Read has a specific "why read it" reason
[ ] 3 subject line options provided, ranked
[ ] Slot 1: between subject lines and The Stat
[ ] Slot 2: between The Stat and The Snippets
[ ] Closer teases Monday
[ ] Stat section: 100-150 words
[ ] Total body: 350-550 words excluding sponsor slots
Save to: editions/[YYYY-MM-DD]-friday/draft.md
Print to terminal:
"Friday done.
Research: editions/[YYYY-MM-DD]-friday/research-brief.md
Draft: editions/[YYYY-MM-DD]-friday/draft.md
Stat: [THE NUMBER in one line]
Snippets used: [N] of [N] researched"
---
## Error Handling
- Stat cannot be verified from primary source: flag it,
  use next best verified alternative, note the switch
- Fewer than 3 non-duplicate snippets available: note
  the gap, use what exists
- No strong Weekend Read found: state this honestly,
  leave the section blank with a note rather than
  recommending a weak piece
- Never fabricate numbers, sources, or quotes
