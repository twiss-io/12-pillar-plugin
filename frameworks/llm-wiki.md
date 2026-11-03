# The Life Wiki — how memory works in this plugin

> Sources go into `raw/` and are never edited. The AI turns them into cross-linked pages inside the twelve pillar folders, which it maintains. A schema file (`AGENTS.md`, imported by a one-line `CLAUDE.md`) holds the rules. Over time the twelve pillars compound into one accurate, navigable second brain: the whole life, studies, job and businesses included.

This follows the LLM wiki pattern described by Andrej Karpathy (gist: `karpathy/llm-wiki`), adapted so that the 12 pillars are the structure of the whole second brain. Read this before writing any file in a user's workspace.

## 1. The three layers

| Layer | What it is | Who writes it |
|---|---|---|
| `raw/` | The source material: notes, voice-note transcripts, documents, screenshots, receipts, exported chats, CVs, drafts. This is the source of truth. One `raw/` for everything. | The user adds files; the AI saves captures here. **Once saved, a raw file is never edited or deleted.** |
| The pillar folders | `01-faith/` … `12-legacy/`: markdown pages the AI writes from the raw sources, one folder per pillar. A job, a school or a business lives inside its pillar. Pages are cross-linked across pillars. | The AI maintains them. Meaningful changes are proposed to the user and confirmed first (see Capture). |
| `AGENTS.md` | The schema (with a `CLAUDE.md` containing `@AGENTS.md`, so Claude Code and Codex read the same rules): who this workspace belongs to, how it's organised, the routing and privacy rules. Each pillar folder has a short one of its own, so a chat opened in that folder focuses on that pillar. | Written at setup from the plugin templates. Your own rules go under `## My additions`, which survives `/12-pillars:lint rules` refreshes. |

The pages are a **compiled view** of the raw material. If a page and a raw source disagree, the raw source wins and the page gets fixed.

## 2. Workspace layout

```
<workspace>/
├── AGENTS.md  CLAUDE.md  .gitignore
├── raw/                    every source, never edited (assets/ for images, PDFs, audio)
├── index.md                catalog: one section per pillar, plus Units
├── log.md                  append-only history
├── actions.md              every to-do and deadline, in one list
├── setup-progress.md       setup checklist
├── 01-faith/
├── 02-identity/            history.md, north-star.md, now.md (current season), instruments/
├── 03-time/                168-budget.md, planning, habits
├── 04-health/              tracking, health reports
├── 05-development/         capabilities.md, books, certifications
│   └── <school>/           a unit: their studies (courses/, exams/, projects/)
├── 06-relationships/       rolodex.md, people/ (one page per person who matters)
├── 07-career/              track-record.md, position cards
│   └── <employer>/         a unit: their job (projects/, clients/)
├── 08-brand/               posts/ (one page per published post), ideas.md
├── 09-opportunities/       deal cards, opportunities
│   └── <business>/         a unit: a business, freelance practice or channel
├── 10-finance/             finances.md
│   └── investing/          a unit: their investing (portfolio/)
├── 11-lifestyle/
└── 12-legacy/
```

Every pillar folder has the same core: `AGENTS.md` (+ `CLAUDE.md`) and `README.md` (the pillar's hub page); `ideas.md` and `decisions/` appear once there is something to put in them. Everything else in it is a page about that pillar.

**Units.** A job, a school, a business or an investing portfolio produces its own stream of information, so it gets a subfolder inside its pillar: their studies in `05-development/<school>/`, their job in `07-career/<employer>/`, a business, freelance practice or channel in `09-opportunities/<name>/`, investing in `10-finance/investing/`. Their own posts and personal brand live directly in `08-brand/`. A unit has `overview.md` (what it is, their role, current state, the names that route to it), and `ideas.md`, `decisions/` and section folders only once there is something to put in them (`folder-design.md` lists sections that fit each kind). Units are listed in the Units section of `index.md`.

## 3. File conventions

**Raw files:** `raw/YYYY-MM-DD-<short-slug>.<ext>` (for example `raw/2026-10-21-call-with-marcus.md`). For a text capture, save the user's words as given, with a small header:

```markdown
---
captured: 2026-10-21
source: voice-note | chat | manual | import | setup | session-summary | draft | <original filename>
---
<the user's words, unedited>
```

Binary files go in `raw/assets/` with the same date prefix. If the name is taken, add `-2`, `-3`, and so on.

**Files the user drops into `raw/` themselves** keep whatever name they have and are never renamed or edited. Instead of adding a header, capture records them by citing them from pages and logging them.

**One source, many pillars.** A note that touches several pillars ("95-hour week for the launch, slept 4h, Sarah wants weekly reports") is saved once in `raw/` and cited from every page it updates: Time, Health, the job's unit, Sarah's page. Nothing is split or copied.

**Session notes** (written by Wrap) are a raw file the AI writes as a summary: `raw/YYYY-MM-DD-session-<slug>.md` with `source: session-summary`, holding a short summary of the discussion plus the user's key statements quoted verbatim. **Drafts** the user keeps (a proposal, plan, email, post) are saved as `raw/YYYY-MM-DD-draft-<slug>.md` with `source: draft`, the final text as is.

**Pages:** lowercase kebab-case filenames. Every page starts with frontmatter:

```markdown
---
title: Marcus Tan
type: person | pillar | topic | self | overview | decision | post | <section type>
pillars: [relationships, opportunities]
tags: ["#marcus", "#bakery"]
sources: [../../raw/2026-10-21-call-with-marcus.md]
updated: 2026-10-21
---
```

Tags live in each page's frontmatter (`tags:`). To reuse existing tags, search the frontmatter across the pillar folders.

`index.md`, `log.md`, `actions.md` and `setup-progress.md` are structural files. They don't need frontmatter or a Sources section.

The body is written in plain sentences that another human could read. Link with relative markdown links: `[Marcus](../06-relationships/people/marcus-tan.md)`. End each page with a `## Sources` list of the raw files it draws on, so every claim can be traced.

**Pillar hub pages** (`NN-<name>/README.md`) have the standard frontmatter (`type: pillar`, `sources: []` and `tags: ["#<pillar>"]` to start), the pillar's purpose and currency in one line, a `**Status:**` line, and these sections: `## Where this stands` (2–4 sentences), `## Current focus`, `## Open questions`, `## Linked pages` (dated lines, including pages in other pillars that matter here), `## Sources`. Keep them short. Detail lives in the pages.

A pillar is **running** once "Where this stands" has been filled from at least one source with real detail about that pillar. A passing line in a broad snapshot (like `02-identity/now.md`) earns a link, not the status. Whenever a capture touches a hub, it refreshes "Where this stands" and, the first time it brings real detail, flips the status from `not yet running` to `running`.

**People pages** (`06-relationships/people/<name>.md`, everyone who matters, personal or work) contain: who they are and how the person knows them; **FORM** (Family, Occupation, Recreation, Money) plus **Health** and **Dreams** (what they're working toward); important dates (birthdays, anniversaries); and open threads (promises either way, any deal cards linked). Personal contacts also get their circle (inner, close, wider: the wedding-and-funeral test in `pillar-playbook.md`), how often they want to stay in touch (suggest at least four times a year for anyone who matters; write only what they choose) and last contact. Work contacts get their role and a link to their unit instead. Client and partner organisations get a page in their unit (`clients/`), not in `people/`. Fill only what is known; leave the rest out rather than guessing.

**`actions.md`** holds every to-do and deadline in one list, under `## Open actions` and `## Open questions`: `- [ ] <what> — due YYYY-MM-DD #<pillar>` (the due part only if there is a date; add the unit's name when it belongs to one, e.g. `#career #twiss`). Done items are ticked `- [x]` with the date, never deleted.

**Where each method's notes go** (the methods are in `pillar-playbook.md`):

| Method | Page |
|---|---|
| History, North Star (declarations), Current Season | `02-identity/history.md`, `02-identity/north-star.md`, `02-identity/now.md` |
| Self-awareness instruments (MBTI, Enneagram, DISC…) | `02-identity/instruments/` (see `instruments.md`) |
| 168-hour budget, seasons of war | `03-time/168-budget.md`; the current season also goes in `02-identity/now.md` |
| Health baseline, thresholds, tracking | `04-health/` pages, linked from its README |
| Capability inventory, gifting → stacking | `05-development/capabilities.md` |
| FORM + Health + Dreams, circle, cadence, last contact | each person's page in `06-relationships/people/` (format above) |
| Rolodex circles and service cadence | `06-relationships/rolodex.md` |
| Evidence file, position cards | `07-career/track-record.md` and `07-career/position-<role>.md`; job detail stays in the job's unit |
| Deal cards (BANT), deal filter | the unit the deal belongs to (`clients/`, `pipeline/`, `proposals/`); a personal one in `09-opportunities/` |
| Four tiers, base number, net worth | `10-finance/finances.md`; holdings stay in `10-finance/investing/` |
| Lifestyle goals with budgets and timing | `11-lifestyle/lifestyle-goals.md` |
| Legacy declarations | `02-identity/north-star.md`, linked from `12-legacy/README.md` |

**`index.md`** has one section per pillar (its README first, then its pages), then **Units** (one line per unit: folder, what it is, the names that route to it, `(archived)` once it has ended). One line per page:
`- [Marcus Tan](06-relationships/people/marcus-tan.md) — friend from uni, now runs a bakery; rebrand prospect`
`- [Twiss](07-career/twiss/overview.md) — tech lead (current job) · names: twiss, supercane, esperanza, axcel`

**`log.md`** is append-only, newest at the bottom, one heading per operation:
`## [2026-10-21] capture | Call with Marcus about the rebrand`
followed by 1–3 lines of what changed. Never rewrite past entries.

## 4. The three operations

### Capture (ingest) — `/12-pillars:capture`
1. Read it and propose, in **one message**: a one-line title, up to 10 tags (pillar tags plus people and topics), and exactly which pages will be created or updated, in every pillar it touches.
   - **Job, study and business facts** go into their unit (matched by the names in the Units section of `index.md`). The pillar's README only gets a link and a line in "Where this stands".
   - **Deadlines and to-dos** go into `actions.md`.
2. Wait for one confirm. Accept corrections in plain language. Nothing is written before it.
3. Save the source to `raw/` (unchanged), then write the changes: update pillar hubs, people and other pages; add new pages if needed; update `index.md`; append to `log.md`.

One source often touches several pages. A single conversation note can update a person page, two pillar hubs, and a unit's client page. That's the point: capture once, and every relevant page stays current.

### Three kinds of conversation

- **Life updates** (short facts: an event, health, money, a person, a plan, a deadline) are filed **right away** via Capture, so nothing is waiting when a long session gets compacted.
- **Working sessions** (brainstorming, planning, strategy) are **not interrupted**. Most of what's said is exploration. When the session winds down, the AI offers a **Wrap**, which files only the outcome.
- **Other tasks** (writing an email, a proposal, a plan, a post) where the person mentions something about themselves **in passing**. Don't interrupt the task. Note the fact, and at a natural pause offer everything noted in one batch: "I picked up 3 things about you: … File them?" One confirm files them like a capture, with the user's words saved to `raw/YYYY-MM-DD-learned-<slug>.md` (`source: chat`). Only file what the user actually said. Never ask questions just to fill pages, and never file guesses about them. Before drafting for a person or client, read their page first. When the task produced something worth keeping, offer at the end to save its final text as a draft in `raw/`, linked from the page it concerns and logged as `## [YYYY-MM-DD] draft | <title>`.

❌ Mid-task: "Before I fix that email — you mentioned your sister's wedding. Want me to file that?"
✅ After the email is done: "Done. I also picked up 2 things about you along the way: your sister's wedding is 14 Dec, and you're cutting caffeine. File them?"

**Learn as you go.** If the user chose the quick start, `setup-progress.md` contains `Mode: learn as you go`, and the setup stages are filled from these batches instead of an interview: a mentioned season fills `02-identity/now.md`, stated goals feed `02-identity/north-star.md`, and a job, school, business or investing that comes up gets offered a unit folder in its pillar once.

A plugin hook re-states this convention on every message, so it holds through long sessions and compaction. A second hook re-orients each new or compacted session: it surfaces the current season, deadlines due within a week, and any unfiled sources, and offers a Wrap after compaction.

### Wrap (end of a working session) — `/12-pillars:wrap`
1. Extract the outcome: decisions (with reasoning and rejected alternatives), parked ideas, actions, open questions, facts learned, finished deliverables.
2. Route each item to its pillar, or to its unit inside the pillar: decisions to `decisions/`, ideas to `ideas.md`, actions and open questions to `actions.md`, facts to the matching page, deliverables to `raw/` as drafts. Captures already made during the session are skipped.
3. Propose it as one card, confirm once, then save a session note to `raw/`, write the pages, link them from the relevant pillar hubs, and update index and log (`## [YYYY-MM-DD] wrap | <title>`).

**Actions get closed, not just added.** When a capture shows an action happened, propose ticking it (`- [x]`, with the date).

**Starting a working session on a unit or pillar:** read its `overview.md` or `README.md`, recent `decisions/`, `ideas.md`, and its lines in `actions.md` first, so the session builds on what was already decided instead of starting from zero.

### Ask (query) — `/12-pillars:ask`
Read `index.md` first, then the relevant pages, following links and checking the raw sources when precision matters. Answer with links to the pages used. If the answer is worth keeping (a decision, a synthesis, a comparison), offer to save it as a page in its pillar.

### Lint (health check) — `/12-pillars:lint`
Look for contradictions between pages, stale claims that newer sources supersede, pages not listed in the index, orphan pages, people mentioned in many places without their own page, broken links, and pillar hubs that haven't been updated in a long time. A page is an **orphan** when nothing links to it except `index.md`; pillar READMEs, unit overviews, `02-identity/` pages and pages inside a unit's sections are never orphans. Report findings first and fix only what the user approves.

## 5. Rules

- **Raw is read-only.** Never edit, rename, or delete anything in `raw/` once saved. (The one exception is the one-time move into this layout, which moves raw files without changing them.)
- **Confirm before meaningful writes.** Capture always shows the proposed changes first. Lint fixes are approved before applying.
- **Don't invent.** Content comes from raw sources or from what the user said in conversation. An empty pillar or a thin page stays thin until real information arrives.
- **One brain, linked, not copied.** A fact lives on one page; other pillars link to it. Never paste the same content into two pillars.
- **Privacy.** Everything stays on this machine. Never put page or raw content into web searches, URLs, or external tool calls.
- **Write for humans.** Pages should read like clear notes a person would want to read, not machine-formatted dumps.
