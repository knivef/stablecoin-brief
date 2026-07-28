# Stablecoin Brief

Skill definitions for **Stablecoin Brief**, a weekly newsletter covering stablecoins and payments for financially literate, crypto-aware readers.

This repo holds no newsletter content. It holds the instructions that produce it. Clone it, open Claude Code in the folder, type `/weekly`, and a full issue gets researched, written, quality checked, and published to Notion.

## Repo layout

```
.
├── CLAUDE.md                  # Master context: audience, voice, style rules, pillars, sources
├── skills/
│   └── weekly/
│       └── SKILL.md           # The weekly issue pipeline
├── .claude/
│   └── commands/
│       └── weekly.md          # /weekly slash command, invokes the skill
└── .gitignore                 # editions/ stays local
```

`CLAUDE.md` loads automatically in every session. It sets the standing rules: no em dashes, no filler phrases, every number carries comparison context, every claim carries an inline citation, and every edition ends with a point of view rather than a summary.

`skills/weekly/SKILL.md` is the operational spec. It only loads when the skill triggers.

## How the skill works

The skill fires on `/weekly` or on natural phrasing like "run the weekly", "write this week's issue", or "newsletter time". Once triggered it runs four steps end to end without asking for confirmation between them.

### Step 0: setup

Detects today's date, sets the coverage window to the most recent complete Monday through Sunday, and creates `editions/[YYYY-MM-DD]-weekly/` dated to the send day. A user-supplied date range overrides the default window.

### Step 1: research

Four parallel workstreams, all completed before a word gets written:

| Workstream | Output |
| --- | --- |
| **A. The Big One** | One highlight story, chosen for a non-obvious angle, a reframing data point, a named character, and stakes beyond crypto. Gathers the primary source, 3+ secondary sources, THE NUMBER, THE CHARACTER, THE COMPLICATION, THE STAKES, and the unique position. |
| **B. The Roundup** | 8 to 12 distinct news items, ranked by newsworthiness and grouped into regulation, infrastructure, adoption, or money moves. |
| **C. The Numbers** | Six standing metrics: total stablecoin market cap, USDT supply, USDC supply, BTC, Nasdaq, CRCL. Each with an as-of date and source. |
| **D. Worth Your Time** | 2 to 4 longer-form reads published that week. |

Everything lands in `research-brief.md`, including discarded items and any aggregator links flagged for swapping to primary sources.

### Step 2: draft

Writes the publish-ready issue to `draft.md` in a fixed structure:

- Metadata block: 3 ranked subject line options (all prefixed 🪙, the first carrying a searchable named entity) plus an SEO description under 160 characters
- Cold open, 50 to 80 words, one surprising stat and a light joke, followed by a 3-item preview list
- 📊 The Numbers table
- 💥 The Big One, 300 to 450 words, story-specific mini-headers, a "By the numbers" block, and a point-of-view kicker
- 🗞️ The Roundup, grouped only under headers that earned items
- ⏳ Worth Your Time
- Sign-off with a point of view, not a recap

Two sponsor placeholders sit at fixed positions: Slot 1 above the cold open, Slot 2 between The Big One and The Roundup. The skill never writes sponsor copy, only placeholders.

### Step 3: quality check

A 16-item checklist runs against the draft and every failure gets fixed before publishing. It covers em dashes, banned filler phrases, citation anchor quality, section word counts, subject line format, sponsor slot placement, joke density (one per section maximum), and total body length of 900 to 1,400 words.

### Step 4: publish

Creates a new Notion page under the Stablecoin Brief parent page, titled `DRAFT: [theme] ([Mon D-D, YYYY])` with a 🪙 icon, containing the full draft. Skipped if the user asked for a local draft or Notion is unavailable.

## Voice in one line

Morning Brew tone applied to serious research. Casual and conversational, written to one reader, with every claim sourced and every number given context. Humor seasons the news; it is not the meal.

## Output

Drafts are written to `editions/[YYYY-MM-DD]-weekly/` and gitignored. This repo tracks the instructions, not the issues.

## Editing the skill

Change the standing voice, style rules, content pillars, or trusted sources in `CLAUDE.md`. Change the pipeline, section structure, word counts, or quality gates in `skills/weekly/SKILL.md`. The two are meant to stay consistent, so a change to one usually wants a look at the other.

## Error handling

The skill degrades rather than fabricates. A weak Big One candidate gets picked with the limitation noted in the brief. Fewer than 8 roundup items ships short instead of padded. An unavailable metric shows `n/a` with a note. Unverifiable claims are dropped and flagged. Nothing appears in both The Big One and The Roundup.
