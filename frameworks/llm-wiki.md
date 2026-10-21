# The Life Wiki — how memory works in this plugin

> Sources go into `raw/` and are never edited. The AI turns them into a cross-linked `wiki/` it maintains. A schema file (`CLAUDE.md`) holds the rules. Over time the wiki compounds into an accurate, navigable picture of a life or a business.

This follows the LLM wiki pattern described by Andrej Karpathy (gist: `karpathy/llm-wiki`), adapted for personal life and for businesses. Read this before writing any file in a user's workspace.

## 1. The three layers

| Layer | What it is | Who writes it |
|---|---|---|
| `raw/` | The source material: notes, voice-note transcripts, documents, screenshots, receipts, exported chats, CVs. This is the source of truth. | The user adds files; the AI saves captures here. **Once saved, a raw file is never edited or deleted.** |
| `wiki/` | Markdown pages the AI writes from the raw sources: summaries, people, topics, the twelve pillar hubs, the person's goals and current situation. Pages are cross-linked. | The AI maintains it. Meaningful changes are proposed to the user and confirmed first (see Capture). |
| `CLAUDE.md` | The schema: who this workspace belongs to, how it's organised, the routing and privacy rules. | Written at setup. The user and AI refine it together over time. |

The wiki is a **compiled view** of the raw material. If a wiki page and a raw source disagree, the raw source wins and the wiki gets fixed.

## 2. Workspace layout

```
<workspace>/
├── CLAUDE.md                      schema for the whole workspace
├── .gitignore                     keeps life/ and businesses/ out of git
├── life/                          the person — organised by the 12 pillars
│   ├── raw/                       immutable sources
│   │   └── assets/                images, PDFs, audio
│   └── wiki/
│       ├── index.md               catalog: Self, Pillars, People, Topics, Businesses
│       ├── log.md                 append-only history
│       ├── self/
│       │   ├── north-star.md      the vision, written as declarations
│       │   ├── now.md             current situation and season
│       │   └── instruments/       optional profiles (astrology, personality type)
│       ├── pillars/               one hub page per pillar, 01-faith.md … 12-legacy.md
│       ├── people/                one page per person who matters
│       └── topics/                everything else: projects, ideas, places, recurring themes
└── businesses/
    ├── <light-business>/
    │   └── notes.md               Light tier: one running page, no raw/wiki split
    └── <business>/                Standard/Deep tier
        ├── CLAUDE.md              schema for this business (incl. its routing tags)
        ├── raw/
        └── wiki/
            ├── index.md
            ├── log.md
            ├── overview.md        what it is, the person's role, current state
            └── <sections>/        chosen at setup, e.g. clients/, products/, team/
```

Businesses don't all get the same shape. `folder-design.md` explains how to choose the tier and the sections for each one.

## 3. File conventions

**Raw files:** `raw/YYYY-MM-DD-<short-slug>.<ext>` (for example `raw/2026-10-21-call-with-marcus.md`). For a text capture, save the user's words as given, with a small header:

```markdown
---
captured: 2026-10-21
source: voice-note | chat | manual | import | setup | <original filename>
---
<the user's words, unedited>
```

Binary files go in `raw/assets/` with the same date prefix.

**Files the user drops into `raw/` themselves** keep whatever name they have and are never renamed or edited. Instead of adding a header, capture records them by citing them from wiki pages and logging them.

**Mixed captures** (business and personal content in one item): the original goes to `life/raw/`, unedited. The business's `raw/` gets a separate file containing **only the business sentences**, with `source: excerpt of life/raw/<file>` in its header. This excerpt is the one allowed exception to "unedited", and it exists so personal content never enters a business folder. If the business is Light (no `raw/`), the business part becomes a dated bullet in its `notes.md` instead.

Setup answers are saved the same way, as the user's own words in a Q&A layout with `source: setup`.

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

**`index.md`** is grouped by section. In `life/` the sections are Self, Pillars, People, Topics, and Businesses (one line per business, linking its overview or `notes.md`). In a business wiki they are Overview, then one section per chosen folder (Decisions last). One line per page:
`- [Marcus Tan](people/marcus-tan.md) — friend from uni, now runs a bakery; rebrand prospect`

**`log.md`** is append-only, newest at the bottom, one heading per operation:
`## [2026-10-21] capture | Call with Marcus about the rebrand`
followed by 1–3 lines of what changed. Never rewrite past entries.

## 4. The three operations

### Capture (ingest) — `/12-pillars:capture`
1. Save the source to `raw/` (unchanged).
2. Read it and propose, in **one message**: a one-line title, up to 10 tags (pillar tags plus people and topics), the destination (`life/` or a business), and exactly which wiki pages will be created or updated.
   - **Deals and business facts** go into the business's folder when that business has one. The life wiki only gets a **link** (for example, `09-opportunities` links to the business's deal page). Without a business folder, they go in the life wiki.
   - **Light businesses** have no `raw/` or `wiki/`: append a dated bullet to `businesses/<name>/notes.md` and log it in `life/wiki/log.md`.
3. Wait for one confirm. Accept corrections in plain language.
4. Write the changes: update pillar hubs, people, and topic pages; add new pages if needed; update `index.md`; append to `log.md`.

One source often touches several pages. A single conversation note can update a person page, two pillar hubs, and a topic page. That's the point: capture once, and every relevant page stays current.

### Ask (query) — `/12-pillars:ask`
Read `index.md` first, then the relevant pages, following links and checking the raw sources when precision matters. Answer with links to the pages used. If the answer is worth keeping (a decision, a synthesis, a comparison), offer to save it as a new wiki page.

### Lint (health check) — `/12-pillars:lint`
Look for contradictions between pages, stale claims that newer sources supersede, pages not listed in the index, orphan pages, people mentioned in many places without their own page, broken links, and pillar hubs that haven't been updated in a long time. A page is an **orphan** when nothing links to it except `index.md`; pillar hubs and `self/` pages are never orphans. Report findings first and fix only what the user approves. Light businesses (`notes.md`) are checked too, for stale or contradictory notes.

## 5. Rules

- **Raw is read-only.** Never edit, rename, or delete anything in `raw/` once saved.
- **Confirm before meaningful writes.** Capture always shows the proposed changes first. Lint fixes are approved before applying.
- **Don't invent.** Wiki content comes from raw sources or from what the user said in conversation. An empty pillar or a thin page stays thin until real information arrives.
- **Keep boundaries.** Personal content from `life/` is never copied into a business wiki, and one business's content is never copied into another. Linking from a person's career or opportunities pillar to a business overview is fine. Copying content across is not.
- **Privacy.** Everything stays on this machine. Never put wiki or raw content into web searches, URLs, or external tool calls.
- **Write for humans.** Pages should read like clear notes a person would want to read, not machine-formatted dumps.
