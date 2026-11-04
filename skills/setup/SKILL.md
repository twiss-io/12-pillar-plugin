---
name: setup
description: "Set up your 12-pillar life workspace: twelve pillar folders that hold your whole second brain, starting with who you are, then your studies, job or businesses inside their pillars"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

You are setting up a 12-pillar life workspace for the user: twelve pillar folders that together are their whole second brain. Before starting, read these files in full. They define everything you build here:
- `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`: the life framework
- `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`: the folder layout, file formats, and rules
- `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md`: units (studies, job, businesses, investing) inside their pillars

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/pillar-playbook.md` only by section: the Identity section for stage 2, and the pillar you're working on in stage 5.

Bundled instruments, with full paths, for stage 2:
- Astrology script: `${CLAUDE_PLUGIN_ROOT}/instruments/bazi.py`
- Enneagram protocol: `${CLAUDE_PLUGIN_ROOT}/instruments/enneagram-typing.md`

## Before anything

**Location.** The current directory becomes the workspace. If it looks like a code repository or someone else's project (has `package.json`, `src/`, a `.git` with commits not belonging to a personal workspace, etc.), stop and ask the user to confirm or to open a new chat in a fresh folder such as `~/my-life`.

**Older layout.** If `life/wiki/index.md` exists, this workspace uses the layout from before 0.8.0 (a `life/` folder plus area folders). Don't set up again: offer the one-time move into the pillar folders, exactly as `/12-pillars:lint rules` does.

**Resuming.** If `setup-progress.md` exists, this is a resume. Show the map of stages marked done / in progress / learning / deferred / skipped, and ask where to pick up (clickable options: continue where we stopped · do something I put off · revisit something I skipped · wrap up). For a stage marked `learning`, first show what has already been picked up about it, then ask only what's missing. Never force the original order on a resume.

**Outdated rules.** If a workspace already exists here (`index.md` and `02-identity/` exist) and its `AGENTS.md` is missing, or its `12-pillars rules:` number is lower than the one in `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`, offer once to refresh it first, exactly as `/12-pillars:lint rules` does.

## Choose how to start

On a fresh start (no `setup-progress.md`), offer one choice as clickable options before anything else:
- **Full setup now (~30–40 min):** the guided interview below, stages 1–6.
- **Quick start (~5 min), learn as we go:** who you are and what fills your days now; everything else fills in from normal conversation.

**Quick start** runs stage 1, then a short stage 2 and stage 3, then stops:
1. Stage 1 as written (name, the twelve pillar folders).
2. **Identity, short:** ask the three starting questions from stage 2 ("Who are you, in a sentence or two?", "What matters most to you right now?", "Where do you want to be in three to five years?"), free text, one at a time, with at most one follow-up. Write `02-identity/README.md`'s "Where this stands" and a first `02-identity/north-star.md` from their answers (declarations in their words, only what they said), and mark Identity `running`.
3. **What fills your days**, as stage 3 describes, choosing each unit's sections from what they already said (no per-unit interview), and their current season into `02-identity/now.md` if they mention one.
4. In `setup-progress.md`, add `Mode: learn as you go` under the title, mark stages 1, 2 and 3 `done` (3 `learning` if they skipped it), stage 4 `learning`, stage 5 `learning`. Save their answers to `raw/YYYY-MM-DD-setup-about-you.md` (`source: setup`) and cite it from every page written.
5. Log `## [YYYY-MM-DD] setup | Quick start`, then tell them, in four short lines: just use this folder for anything, and whatever they share about themselves gets saved in the right pillar (they'll see a line saying where, and can say undo); each pillar folder is its own space (open a chat inside `04-health/` to work on health); `/12-pillars:setup` any time does a stage properly, and `/12-pillars:pillars` shows everything.

Do not continue past this. Quick start is finished.

## How to run the interview

- **Open with the map.** Before the first question, show the stages below in one compact list with rough times, and say two things: they can stop any time (it picks up where they left off), and every question can be skipped.
- **Two kinds of skip.** "Skip for now" → mark it `deferred` and offer it once more at the end. "Skip" → mark it `skipped` and never bring it up again unless the user does. Both are completely fine. Say so and move on without comment.
- **One question at a time.** Converse, don't interrogate. Follow up on what they actually said.
- **Clickable options for choices.** When the answer is one of a few options, use clickable options. Keep open questions (who they are, their vision, their situation, their story) as free conversation.
- **Templates for structured answers.** When you need several specific facts (dates, numbers, names), give a short fill-in template instead of a prose question.
- **Save as you go.** Setup answers are the user answering your own questions, so they need no save confirm: write them as each stage goes. After each stage, update `setup-progress.md`, show a one-line progress strip (e.g. `About you ▓ · Identity ▓ · Your days ░ · Now ░ · Pillars ░ — 2 of 5, then wrap-up`), and give a short "Here's what I've got" recap (3–6 bullets) they can correct. Only the proposed tree in stage 3 waits for a confirm before folders are created.
- **Stopping early.** "I'll answer the rest later" (or similar): save what they've said, mark the rest `deferred`, and say in one line what was kept and how to pick up ("continue setup"). No buttons.
- **Facts over stories.** If an answer sounds polished, gently ask what's actually going on.
- **Keep a source for everything.** At the end of each stage, save the user's answers (their words verbatim, laid out as Q&A) to `raw/YYYY-MM-DD-setup-<stage>.md` with the raw header (`source: setup`), and list that file in the `sources:` of every page the stage writes (if it writes none, on the `Sources:` line of `setup-progress.md`).

## The stages

### 1 · About you (~2 min)
Ask what the workspace should call them. An alias is fine and their real name isn't needed anywhere. Ask, in one question, what they mainly want this for (organising life, studies, work or a business, getting unstuck in one area, keeping track of people, all of it).

Then **create the base workspace** (never overwrite existing files; report anything skipped):

```
AGENTS.md            the workspace rules (Codex and other agents read this)
CLAUDE.md            one line: @AGENTS.md (so Claude Code reads the same rules)
.gitignore           ignores everything except AGENTS.md, CLAUDE.md and itself
raw/assets/
index.md             one section per pillar, then Units
log.md               first entry: ## [YYYY-MM-DD] setup | Workspace created
actions.md           ## Open actions, ## Open questions
setup-progress.md
01-faith/ … 12-legacy/   each with AGENTS.md, CLAUDE.md and README.md
```

The `.gitignore` is four lines: `/*`, `!/AGENTS.md`, `!/CLAUDE.md`, `!/.gitignore`, so every folder stays out of git.

Write the workspace `AGENTS.md` by copying `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md` exactly, with `<Name>` replaced by what they want to be called. Keep the `12-pillars rules:` stamp line; it is how later plugin versions notice the rules need a refresh. Write `CLAUDE.md` containing only `@AGENTS.md`.

In each pillar folder, write `AGENTS.md` from `${CLAUDE_PLUGIN_ROOT}/templates/pillar-AGENTS.md` (with the pillar's number, name and currency filled in), a `CLAUDE.md` containing only `@AGENTS.md`, and `README.md`: frontmatter (`title`, `type: pillar`, `pillars: [<name>]`, `tags: ["#<name>"]`, `sources: []`, `updated`), the pillar's purpose and currency in one line from `12-pillars.md`, `**Status:** not yet running`, and empty sections `## Where this stands`, `## Current focus`, `## Open questions`, `## Linked pages`, `## Sources`. Add all 12 READMEs to `index.md`.

`setup-progress.md` is a checklist, one line per stage: `- [ ] 1 · About you — pending` (states: pending, in progress, done, learning, deferred, skipped). `learning` means the stage is being filled from everyday conversation (quick start).

### 2 · Who you are (~10–15 min)
Identity is the core, so it comes first. Read the Identity section of `pillar-playbook.md` (where it puts instruments first, this setup asks these questions first and offers the profiles after). Ask, one at a time, free text:
1. **"Who are you, in a sentence or two?"** (what they do, what they care about, how they'd describe themselves to a friend)
2. **"What's your story so far? Where you grew up, and two or three turning points."** (skippable)
3. **"What matters most to you right now?"**
4. **"Where do you want to be in three to five years?"** If they already have a vision board, a goals doc or anything similar, ask them to share it; save it to `raw/` and work from it.

Write `02-identity/history.md` (their story, if shared) and `02-identity/north-star.md`: their vision as **declarations**, present-tense statements of the life as if it's already true ("I am…", "I have…"), covering whichever areas they care about (don't force all twelve). Bold goals are allowed. Fill `02-identity/README.md` ("Where this stands", "Current focus") and mark it `**Status:** running`. Link `north-star.md` from `12-legacy/README.md` if it holds legacy declarations. People who clearly matter in their story or vision (a partner, a parent) get a page in `06-relationships/people/`, with only what was said.

Then offer the optional profiles (clickable: include them · just one · not now · no), following `${CLAUDE_PLUGIN_ROOT}/frameworks/instruments.md` exactly. Honour a no immediately. Results go in `02-identity/instruments/`.

### 3 · What fills your days (~2–10 min)
Follow `folder-design.md`. Ask its open "What fills your days?" question (free text). It gives the units: their studies in `05-development/<school>/`, their job in `07-career/<employer>/`, each business in `09-opportunities/<name>/`, investing in `10-finance/investing/`, and a personal brand as a line in `08-brand/README.md`'s "Current focus" (its `posts/` folder starts with the first post); or none if they're between things. For each unit, ask in one or two questions what it runs on and the names they'll use (clients, projects, courses), so its sections and routing names fit. Then **show the proposed tree** as `folder-design.md` section 4 shows, and get one confirm. Accept changes in plain language. Then create each unit as `folder-design.md` section 6 describes (the single spec for building a unit). Save the whole answer once to `raw/YYYY-MM-DD-setup-your-days.md` and cite it from every unit overview. If they chose nothing, say in one line that the pillars cover it for now and a unit gets made when something comes up.

### 4 · Where you are now (~10 min)
An honest snapshot: work and money (one line per unit, since the detail belongs in the unit), health, key relationships, what's working, what they're avoiding. Then ask if they're in a particular season (a launch, exams, a sprint, a recovery period) and, if so, since when and until when. Save to `02-identity/now.md` with a `Season:` line, plus `Since: YYYY-MM-DD` and `Until: YYYY-MM-DD` lines for the dates they know. Questions they can't answer yet go in an `## Open questions` section. Link `now.md` from the pillar READMEs it touches (links only; this stage doesn't mark pillars running). Any deadline they mention goes in `actions.md`.

### 5 · Start where it hurts (~10 min per pillar)
Ask: **"Which area of your life do you most want to get moving?"** Offer 3–4 pillars their answers so far point to, as clickable options, plus Other. For that pillar:
- Read that pillar's section in `pillar-playbook.md`. Ask 2–4 of its questions, adapted to what you already know, and offer the one method from it that fits their answers (e.g. a first 168-hour budget for Time, the base number for Finance, the wedding-and-funeral test for Relationships). Fill it only from what they tell you, in the page `llm-wiki.md` names for that method.
- Save their answers to `raw/` (`setup-<pillar>`), then update the pillar's README: fill in "Where this stands", "Current focus", and mark it `**Status:** running`. Log it as `## [YYYY-MM-DD] capture | <pillar> — setup` so it counts like any other capture.
- Shortcuts if relevant: for **Career**, invite them to paste their CV or LinkedIn profile (save to raw, summarise into the README and `07-career/track-record.md`). For **Relationships**, ask who the 3–5 most important people are and create their pages in `06-relationships/people/` (format in `llm-wiki.md`, only what they know).

Offer one more pillar, or move to the close.

### 6 · Close
1. **Deferred sweep.** List everything marked `deferred` and offer each once more (do it now · next time · skip it). A deferred item declined here becomes `skipped`.
2. **Show the payoff.** Build the dashboard (`/12-pillars:pillars` step 1) and open it, or render the 12 pillars as a table (pillar · status · last updated) if you can't run it. Tell them empty pillars are normal, because they fill in as they share their life.
3. **Name one useful thing for tomorrow**, drawn from what they shared ("Before Thursday's call with Sarah, ask me what to prepare").
4. **Explain the daily habit in three lines.** Tell me what happened, or drop a file into `raw/`. I'll save it in the right pillars straight away and tell you where (say undo or correct me any time). When we brainstorm or plan, I won't interrupt; at the end I'll wrap up what we decided. Each pillar folder is its own space: open a chat inside one to work on just that pillar. In Codex, offer the morning brief and weekly review as automations (`/12-pillars:pillars` "Running them on a schedule").
5. Append to `log.md`: `## [YYYY-MM-DD] setup | Setup complete` with a one-line summary.
