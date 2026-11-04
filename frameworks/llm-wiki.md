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

**`actions.md`** holds every to-do and deadline in one list, under `## Open actions` and `## Open questions`: `- [ ] <what> — due YYYY-MM-DD #<pillar>` (the due part only if there is a date; a reminder at a set time adds it in 24-hour form, `due 2026-11-07 15:00`; add the unit's name when it belongs to one, e.g. `#career #twiss`). Done items are ticked `- [x]` with the date, never deleted.

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
| Weekly reviews | `03-time/reviews/YYYY-MM-DD-week.md`, linked from `03-time/README.md` |
| Lifestyle goals with budgets and timing | `11-lifestyle/lifestyle-goals.md` |
| Legacy declarations | `02-identity/north-star.md`, linked from `12-legacy/README.md` |

**`index.md`** has one section per pillar (its README first, then its pages), then **Units** (one line per unit: folder, what it is, the names that route to it, `(archived)` once it has ended). One line per page:
`- [Marcus Tan](06-relationships/people/marcus-tan.md) — friend from uni, now runs a bakery; rebrand prospect`
`- [Twiss](07-career/twiss/overview.md) — tech lead (current job) · names: twiss, supercane, esperanza, axcel`

**`log.md`** is append-only, newest at the bottom, one heading per operation:
`## [2026-10-21] capture | Call with Marcus about the rebrand`
followed by 1–3 lines of what changed. Never rewrite past entries.

## 4. How it runs

Nothing here needs a command. In a workspace, the AI files what the user shares, answers from the pages, and keeps units current on its own. Only setup, wrap, pillars and lint are skills.

### Filing (automatic, no confirm)
What's worth keeping about the user's life is filed **straight away, without asking first**. Then the AI reports what it did.

**Worth saving:** people (who they are, what was said or agreed, what's owed), deadlines and to-dos, decisions, numbers (money, sleep, weight, hours), events and wins, goals and plans, changes (a new job, a move, something that ended), and files they send about their life.
**Not saved:** small talk, a passing mood with nothing behind it, their questions, help with a task (fix this email, explain X; the finished result may become a draft), anything already saved, and the AI's own answers. When it's borderline, skip it: if it matters, it comes up again, and "save that" files it.

1. **Read it.** Images count too: a receipt → money figures (#finance), a meal or workout → #health, a screenshot of a chat → the people and what was agreed. If a file can't be read (audio, an unreadable image), ask for a one-line summary rather than guessing.
2. **Work out where it goes:** a one-line title, up to 10 tags (pillar tags `#faith` … `#legacy`, people `#<name>`, units and topics; reuse existing tags and page names before inventing new ones), and every page it touches, in every pillar.
   - **Job, study and business facts** go into their unit, matched by the names in the Units section of `index.md`. The pillar's README only gets a link and a line in "Where this stands". Route by what the item is, with names as hints: a post they published goes to `08-brand/posts/` even when it mentions a client.
   - **Deadlines, to-dos and reminders** go into `actions.md` as `- [ ] <what> — due YYYY-MM-DD #<pillar> #<unit>`; "remind me Fri 3pm to …" adds the time (`due 2026-11-07 15:00`). When it shows an open action was done, tick it (`- [x]`, with the date).
   - **A new job, school, business or investing** that is clearly theirs and has real detail gets a unit in its pillar now, per `folder-design.md` section 6. If it's unclear whether they own a business or work for it, that is the one question to ask first.
   - **A change** (a new job, an ended plan or relationship): update the pages, archive a finished unit (`folder-design.md` section 5), and say so in the report.
3. **File:**
   1. Save the source once to `raw/YYYY-MM-DD-<slug>.md` with the capture header (or copy the given file there; binaries to `raw/assets/`). A file already in `raw/` stays as it is.
   2. Write the changes in every pillar it touches, keeping each page's frontmatter (`updated`, `sources`, `tags`) and `## Sources` list current. Every page changed cites the raw file.
   3. Add new pages to `index.md`. Append `## [YYYY-MM-DD] capture | <title>` to `log.md`, plus 1–2 lines naming the pages touched.
   4. For each pillar README touched, refresh "Where this stands". If it was `not yet running` and this source gives real detail about that pillar, set `**Status:** running`.
4. **Report in one or two short lines:** what was saved where, in plain words ("Saved: Marcus's rebrand (~20K) under Acme Studio, his page updated, follow-up due Fri in your to-dos"). Add at most one line when it matters: a real change from their normal (sleep well under their usual, spending above their base number) as one plain question about what might be driving it, per `12-pillars.md` section 3; or a win someone witnessed, as a nudge to ask for a testimonial now.
5. **Corrections and undo.** The user fixes things in plain language. A wrong place ("no, that's for the shop"): move the pages and log `## [YYYY-MM-DD] correct | <title>`. A wrong fact ("it's 25K not 20K"): that is new information, so file it like any other (their words to `raw/`, cited by the pages it fixes). "Undo" reverses the last filing: delete the raw file it created (the one exception to raw being read-only, and only for a file saved by mistake in this chat), restore the pages it changed, remove its index lines, and append `## [YYYY-MM-DD] undo | <title>` to `log.md`.

❌ "Here's what I'd file: … Shall I save this?"
✅ "Saved: back pain all week → Health; physio booked Thu → to-dos. (Say undo, or correct me.)"

One source often touches several pages. A single conversation note can update a person page, two pillar hubs, and a unit's client page. That's the point: saved once, every relevant page stays current.

### Three kinds of conversation

- **Life updates** (short facts: an event, health, money, a person, a plan, a deadline) are filed **right away**, so nothing is waiting when a long session gets compacted.
- **Working sessions** (brainstorming, planning, strategy) are **not interrupted**. Most of what's said is exploration. When the session winds down, the AI runs a **Wrap**, which files only the outcome.
- **Other tasks** (writing an email, a proposal, a plan, a post) where the person mentions something about themselves **in passing**. Don't interrupt the task. Note the fact, and at a natural pause file everything noted, with the user's words saved to `raw/YYYY-MM-DD-learned-<slug>.md` (`source: chat`), and report it in one line. Only file what the user actually said. Never ask questions just to fill pages, and never file guesses about them. Before drafting for a person or client, read their page first. When the task produced a finished piece the user is actually using (a proposal, plan, email or post they're sending), save its final text as a draft in `raw/YYYY-MM-DD-draft-<slug>.md` (`source: draft`), linked from the page it concerns and logged as `## [YYYY-MM-DD] draft | <title>`.

❌ Mid-task: "Before I fix that email — you mentioned your sister's wedding. Want me to file that?"
✅ After the email is done: "Done. I also saved 2 things you mentioned: your sister's wedding is 14 Dec (to-dos), and you're cutting caffeine (Health)."

**Learn as you go.** If the user chose the quick start, `setup-progress.md` contains `Mode: learn as you go`, and the setup stages fill in from filing instead of an interview: a mentioned season fills `02-identity/now.md`, stated goals feed `02-identity/north-star.md`, and a job, school, business or investing that comes up gets its unit. A stage is marked `done` once its page has real content.

**Files dropped into `raw/`.** The session start lists raw files no page cites yet. When the user says to file them (or asks what they are), file each one as above, oldest first. Files the user dropped in themselves are left exactly as they are: no rename, no added header.

A plugin hook re-states this convention on every message, so it holds through long sessions and compaction. A second hook re-orients each new or compacted session: it surfaces the current season, deadlines due within a week, and any unfiled sources.

### Wrap (end of a working session) — `/12-pillars:wrap`
1. Extract the outcome: decisions (with reasoning and rejected alternatives), parked ideas, actions, open questions, facts learned, finished deliverables.
2. Route each item to its pillar, or to its unit inside the pillar: decisions to `decisions/`, ideas to `ideas.md`, actions and open questions to `actions.md`, facts to the matching page, deliverables to `raw/` as drafts. Items already filed during the session are skipped.
3. Save a session note to `raw/`, write the pages, link them from the relevant pillar hubs, update index and log (`## [YYYY-MM-DD] wrap | <title>`), then show what was filed as one card. Corrections and undo work as in Filing.

**Starting a working session on a unit or pillar:** read its `overview.md` or `README.md`, recent `decisions/`, `ideas.md`, and its lines in `actions.md` first, so the session builds on what was already decided instead of starting from zero.

### Answering (automatic)
Any question about their life is answered from the workspace.
1. **Find.** Read `index.md` first. A question about their studies, job, a business or investing starts from that unit's `overview.md`; about one pillar, from its `README.md`; about deadlines, from `actions.md`. Follow links, and check the raw sources when the answer needs exact figures, dates or wording.
2. **Answer** plainly, from what the pages actually say, with links to the pages used. If they don't cover it, say what's missing instead of guessing.
3. **Stuck?** Look for what's driving it as `12-pillars.md` section 3 describes, and answer in plain language, without pillar names unless they ask. For how a pillar works or what to do about it, use that pillar's section in `pillar-playbook.md`.
4. **Prepping for a person or meeting:** lead with last contact, open threads and promises, what they care about now, upcoming important dates, and 3–5 talking points.
5. **Keep good answers.** A useful synthesis, decision or comparison is saved as a page in its pillar or unit (e.g. `09-opportunities/acme-studio/decisions/2026-11-03-hire-vs-outsource.md`) and logged as `## [YYYY-MM-DD] ask | <title>`, reported in one line.

If a question needs outside information, ask before searching, and search in general terms only.

### Lint (health check) — `/12-pillars:lint`
Look for contradictions between pages, stale claims that newer sources supersede, pages not listed in the index, orphan pages, people mentioned in many places without their own page, broken links, and pillar hubs that haven't been updated in a long time. A page is an **orphan** when nothing links to it except `index.md`; pillar READMEs, unit overviews, `02-identity/` pages and pages inside a unit's sections are never orphans. Report findings first and fix only what the user approves.

## 5. Rules

- **Raw is read-only.** Never edit, rename, or delete anything in `raw/` once saved. (Two exceptions: the one-time move into this layout, which moves raw files without changing them, and an undo of a file saved by mistake in the same chat.)
- **File, then report.** Filing and wraps write straight away and say what they did, so the user can correct or undo. Lint fixes, moving the workspace, and refreshing the rules are approved before applying.
- **Don't invent.** Content comes from raw sources or from what the user said in conversation. An empty pillar or a thin page stays thin until real information arrives.
- **One brain, linked, not copied.** A fact lives on one page; other pillars link to it. Never paste the same content into two pillars.
- **Privacy.** Everything stays on this machine. Never put page or raw content into web searches, URLs, or external tool calls.
- **Write for humans.** Pages should read like clear notes a person would want to read, not machine-formatted dumps.
