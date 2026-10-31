# The Life Wiki — how memory works in this plugin

> Sources go into `raw/` and are never edited. The AI turns them into a cross-linked `wiki/` it maintains. A schema file (`AGENTS.md`, imported by a one-line `CLAUDE.md`) holds the rules. Over time the wiki compounds into an accurate, navigable picture of a life or a business.

This follows the LLM wiki pattern described by Andrej Karpathy (gist: `karpathy/llm-wiki`), adapted for personal life and for the areas around it: work, studies, businesses. Read this before writing any file in a user's workspace.

## 1. The three layers

| Layer | What it is | Who writes it |
|---|---|---|
| `raw/` | The source material: notes, voice-note transcripts, documents, screenshots, receipts, exported chats, CVs. This is the source of truth. | The user adds files; the AI saves captures here. **Once saved, a raw file is never edited or deleted.** |
| `wiki/` | Markdown pages the AI writes from the raw sources: summaries, people, topics, the twelve pillar hubs, the person's goals and current situation. Pages are cross-linked. | The AI maintains it. Meaningful changes are proposed to the user and confirmed first (see Capture). |
| `AGENTS.md` | The schema (with a `CLAUDE.md` containing `@AGENTS.md`, so Claude Code and Codex read the same rules): who this workspace belongs to, how it's organised, the routing and privacy rules. | Written at setup from the plugin template. Your own rules go under `## My additions`, which survives `/12-pillars:lint rules` refreshes when the plugin updates its rules. |

The wiki is a **compiled view** of the raw material. If a wiki page and a raw source disagree, the raw source wins and the wiki gets fixed.

## 2. Workspace layout

```
<workspace>/
├── AGENTS.md                      schema for the whole workspace
├── CLAUDE.md                      @AGENTS.md
├── .gitignore                     keeps everything but the rules out of git
├── life/                          the person — organised by the 12 pillars
│   ├── raw/                       immutable sources
│   │   └── assets/                images, PDFs, audio
│   └── wiki/
│       ├── index.md               catalog: Self, Pillars, People, Topics, Areas
│       ├── log.md                 append-only history
│       ├── self/
│       │   ├── north-star.md      the vision, written as declarations
│       │   ├── now.md             current situation and season
│       │   └── instruments/       optional profiles (astrology, personality type)
│       ├── pillars/               one hub page per pillar, 01-faith.md … 12-legacy.md
│       ├── people/                one page per person who matters
│       └── topics/                everything else: projects, ideas, places, recurring themes
├── study/                         an area, only if they study
├── work/                          an area, only if they have a job
├── investing/                     an area, only if they invest
└── businesses/                    only if they run a business, practice or channel
    └── <business>/                every area has this same core; tiers differ only in sections
        ├── AGENTS.md              schema for this area (incl. its routing tags)
        ├── CLAUDE.md              @AGENTS.md
        ├── raw/
        └── wiki/
            ├── index.md
            ├── log.md
            ├── overview.md        what it is, the person's role, current state
            ├── decisions/         one page per decision (written by wrap)
            ├── ideas.md           parked ideas (written by wrap)
            ├── actions.md         open to-dos (written by wrap)
            └── <sections>/        chosen at setup, e.g. clients/, products/, team/
```

Only the areas the person chose exist, and they don't all get the same shape. `folder-design.md` explains which areas fit them, and how to choose the tier and sections for each.

## 3. File conventions

**Raw files:** `raw/YYYY-MM-DD-<short-slug>.<ext>` (for example `raw/2026-10-21-call-with-marcus.md`). For a text capture, save the user's words as given, with a small header:

```markdown
---
captured: 2026-10-21
source: voice-note | chat | manual | import | setup | session-summary | <original filename>
---
<the user's words, unedited>
```

Binary files go in `raw/assets/` with the same date prefix.

**Files the user drops into `raw/` themselves** keep whatever name they have and are never renamed or edited. Instead of adding a header, capture records them by citing them from wiki pages and logging them.

**Mixed captures** (area and personal content in one item, e.g. a business, the job, or studies): the original goes to `life/raw/`, unedited. The area's `raw/` gets a separate file containing **only the area's sentences**, with `source: excerpt of life/raw/<file>` in its header. This excerpt is one of **two exceptions** to "unedited" (the other is session notes, below), and it exists so personal content never enters an area folder. If the area is Light (no `raw/`), the area's part becomes a dated bullet in its `notes.md` instead.

Setup answers are saved the same way, as the user's own words in a Q&A layout with `source: setup`.

**Session notes** (written by Wrap) are the second exception, a raw file the AI writes as a summary: `raw/YYYY-MM-DD-session-<slug>.md` with `source: session-summary`, holding a short summary of the discussion plus the user's key statements quoted verbatim.

**Wiki pages:** lowercase kebab-case filenames. Every page starts with frontmatter:

```markdown
---
title: Marcus Tan
type: person | pillar | topic | self | overview | <section type>
pillars: [relationships, opportunities]
tags: ["#marcus", "#bakery"]
sources: [../../raw/2026-10-21-call-with-marcus.md]
updated: 2026-10-21
---
```

Tags live in each page's frontmatter (`tags:`). To reuse existing tags, search the frontmatter across the wiki.

`index.md`, `log.md`, and `self/setup-progress.md` are structural files. They don't need frontmatter or a Sources section.

The body is written in plain sentences that another human could read. Link with relative markdown links: `[Marcus](../people/marcus-tan.md)`. End each page with a `## Sources` list of the raw files it draws on, so every claim can be traced.

**Pillar hub pages** (`wiki/pillars/NN-<name>.md`) have the standard frontmatter (`sources: []` and `tags: ["#<pillar>"]` to start), a `**Status:**` line, and these sections: `## Where this stands` (2–4 sentences), `## Current focus`, `## Open questions`, `## Linked pages` (dated lines), `## Sources`. Keep them short. Detail lives in the linked pages.

A pillar is **running** once "Where this stands" has been filled from at least one real source. Whenever a capture adds a link to a hub, it also refreshes "Where this stands" and, the first time, flips the status from `not yet running` to `running`.

**People pages** contain: who they are and how the person knows them, family, work, interests, what they're working toward, health if relevant, important dates (birthdays, anniversaries), how often to stay in touch, last contact, and open threads (promises either way).

**`index.md`** is grouped by section. In `life/` the sections are Self, Pillars, People, Topics, and Areas (one line per area folder, saying what it is and linking its overview; older workspaces call it Businesses). In an area wiki they are: Overview (with lines for `overview.md`, `ideas.md` and `actions.md`), then one section per chosen folder, then Decisions, always last. One line per page:
`- [Marcus Tan](people/marcus-tan.md) — friend from uni, now runs a bakery; rebrand prospect`

**`log.md`** is append-only, newest at the bottom, one heading per operation:
`## [2026-10-21] capture | Call with Marcus about the rebrand`
followed by 1–3 lines of what changed. Never rewrite past entries.

## 4. The three operations

### Capture (ingest) — `/12-pillars:capture`
1. Save the source to `raw/` (unchanged).
2. Read it and propose, in **one message**: a one-line title, up to 10 tags (pillar tags plus people and topics), the destination (`life/` or an area), and exactly which wiki pages will be created or updated.
   - **Deals and business facts** go into the business's folder when that business has one. The life wiki only gets a **link** (for example, `09-opportunities` links to the business's deal page). Without a business folder, they go in the life wiki.
   - **Job, study and investing facts** follow the same rule: into `work/`, `study/` or `investing/` when that area exists, otherwise the life wiki (Career, Growth, Finance).
   - **Older notes-only areas** (just `notes.md`) get a dated bullet in `notes.md`, logged in `life/wiki/log.md`, with a one-time offer to give the area the full structure.
3. Wait for one confirm. Accept corrections in plain language.
4. Write the changes: update pillar hubs, people, and topic pages; add new pages if needed; update `index.md`; append to `log.md`.

One source often touches several pages. A single conversation note can update a person page, two pillar hubs, and a topic page. That's the point: capture once, and every relevant page stays current.

### Three kinds of conversation

- **Life updates** (short facts: an event, health, money, a person, a plan) are filed **right away** via Capture, so nothing is waiting when a long session gets compacted.
- **Working sessions** (brainstorming, planning, strategy) are **not interrupted**. Most of what's said is exploration. When the session winds down, the AI offers a **Wrap**, which files only the outcome.
- **Other tasks** (writing an email, fixing code, planning a trip) where the person mentions something about themselves **in passing**. Don't interrupt the task. Note the fact, and at a natural pause offer everything noted in one batch: "I picked up 3 things about you: … File them?" One confirm files them like a capture, with the user's words saved to `life/raw/YYYY-MM-DD-learned-<slug>.md` (`source: chat`). Only file what the user actually said. Never ask questions just to fill pages, and never file guesses about them.

❌ Mid-task: "Before I fix that email — you mentioned your sister's wedding. Want me to file that?"
✅ After the email is done: "Done. I also picked up 2 things about you along the way: your sister's wedding is 14 Dec, and you're cutting caffeine. File them?"

**Learn as you go.** If the user chose the quick start, `life/wiki/self/setup-progress.md` contains `Mode: learn as you go`, and the setup stages are filled from these batches instead of an interview: a mentioned season fills `self/now.md`, stated goals feed `self/north-star.md`, and a business, job, studies or investing that comes up repeatedly with no folder gets offered a Light area folder once.

A plugin hook re-states this convention on every message, so it holds through long sessions and compaction. A second hook re-orients each new or compacted session: it surfaces the current season and any unfiled sources, and offers a Wrap after compaction.

### Wrap (end of a working session) — `/12-pillars:wrap`
1. Extract the outcome: decisions (with reasoning and rejected alternatives), parked ideas, actions, open questions, facts learned, and any personal parts.
2. Route each item: an area's decisions go to `wiki/decisions/`, ideas to `wiki/ideas.md`, actions and open questions to `wiki/actions.md`, facts to the matching section. Older notes-only areas get prefixed `notes.md` bullets. Personal parts go to `life/`, with open questions in the relevant pillar hub. Captures already made during the session are skipped.
3. Propose it as one card, confirm once, then save a session note to each destination's `raw/`, write the pages, link them from the relevant pillar hubs, and update index and log (`## [YYYY-MM-DD] wrap | <title>`).

**Actions get closed, not just added.** When a capture shows an action happened, propose ticking it (`- [x]`, with the date). Lint reports open actions past their due date.

**Starting a working session on an area:** read its `overview.md`, recent `decisions/`, `ideas.md`, and `actions.md` first, so the session builds on what was already decided instead of starting from zero.

### Ask (query) — `/12-pillars:ask`
Read `index.md` first, then the relevant pages, following links and checking the raw sources when precision matters. Answer with links to the pages used. If the answer is worth keeping (a decision, a synthesis, a comparison), offer to save it as a new wiki page.

### Lint (health check) — `/12-pillars:lint`
Look for contradictions between pages, stale claims that newer sources supersede, pages not listed in the index, orphan pages, people mentioned in many places without their own page, broken links, and pillar hubs that haven't been updated in a long time. A page is an **orphan** when nothing links to it except `index.md`; pillar hubs and `self/` pages are never orphans. Report findings first and fix only what the user approves. Light areas (`notes.md`) are checked too, for stale or contradictory notes.

## 5. Rules

- **Raw is read-only.** Never edit, rename, or delete anything in `raw/` once saved.
- **Confirm before meaningful writes.** Capture always shows the proposed changes first. Lint fixes are approved before applying.
- **Don't invent.** Wiki content comes from raw sources or from what the user said in conversation. An empty pillar or a thin page stays thin until real information arrives.
- **Work contacts live in their area.** Clients, colleagues and team members get pages in the area (`clients/`, `people/`, `team/`); `life/wiki/people/` is for personal relationships, and may link to an area page when someone is both.
- **Keep boundaries.** Personal content from `life/` is never copied into an area (a business, `work/`, `study/`, `investing/`), and one area's content is never copied into another. Linking from a person's career or opportunities pillar to an area's overview is fine. Copying content across is not.
- **Privacy.** Everything stays on this machine. Never put wiki or raw content into web searches, URLs, or external tool calls.
- **Write for humans.** Pages should read like clear notes a person would want to read, not machine-formatted dumps.
