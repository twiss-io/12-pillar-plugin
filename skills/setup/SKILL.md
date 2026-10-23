---
name: setup
description: "Set up your 12-pillar life workspace: a guided interview, then a folder structure recommended for your life and businesses, built after you confirm"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. "Clickable options" means a choice tool if you have one (AskUserQuestion in Claude Code), otherwise a short numbered list.

You are setting up a 12-pillar life workspace for the user. Before starting, read these three files in full. They define everything you build here:
- `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`: the life framework
- `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`: the folder layout, file formats, and rules
- `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md`: how to recommend structure for businesses

Bundled instruments, with full paths, for stage 2:
- Astrology script: `${CLAUDE_PLUGIN_ROOT}/instruments/bazi.py`
- Enneagram protocol: `${CLAUDE_PLUGIN_ROOT}/instruments/enneagram-typing.md`

## Before anything

**Location.** The current directory becomes the workspace. If it looks like a code repository or someone else's project (has `package.json`, `src/`, a `.git` with commits not belonging to a personal workspace, etc.), stop and ask the user to confirm or to open Claude in a fresh folder such as `~/my-life`.

**Resuming.** If `life/wiki/self/setup-progress.md` exists, this is a resume. Show the map of stages marked done / in progress / learning / deferred / skipped, and ask where to pick up (clickable options: continue where we stopped · do something I put off · revisit something I skipped · wrap up). For a stage marked `learning`, first show what has already been picked up about it, then ask only what's missing. Never force the original order on a resume.

## Choose how to start

On a fresh start (no `setup-progress.md`), offer one choice as clickable options before anything else:
- **Full setup now (~45 min):** the guided interview below, stages 1–7.
- **Choose parts:** set up only the parts they pick now; the rest is learned as we go.
- **Quick start (~2 min), learn as we go:** set up the base workspace now, then fill it in from normal conversation over time.

**Choose parts** asks one multi-select question (clickable options) with the stages and their times: Optional profiles (~5–10 min) · Your vision (~10 min) · Where you are now (~10 min) · Your work and businesses (~5–15 min) · Start where it hurts (~10 min). Stage 1 (About you) always runs, since it builds the workspace. Then:
1. Run stage 1, then only the chosen stages, in the usual order, with the same interview rules. Show the progress strip counting just the chosen stages.
2. In `setup-progress.md`, mark unchosen stages 3–6 `learning` (unchosen profiles: `deferred`) and add `Mode: learn as you go`, unless every stage was chosen.
3. Finish with stage 7, but in its deferred sweep, don't offer the `learning` stages again; say in one line that they fill in from conversation and `/12-pillars:setup` can do any of them later.

**Quick start** runs only stage 1, cut down: ask what the workspace should call them (one question, alias fine), skip the "what for" question, and create the base workspace exactly as stage 1 describes. Then:
1. In `setup-progress.md`, add the line `Mode: learn as you go` under the title, mark stage 1 `done`, stage 2 (profiles) `deferred`, and stages 3–6 `learning`.
2. Save their answer to `life/raw/YYYY-MM-DD-setup-about-you.md` (`source: setup`).
3. Log `## [YYYY-MM-DD] setup | Quick start`.
4. Tell them, in four short lines: just use this folder for anything; when they mention something about themselves along the way, it's noted without interrupting, and offered for filing in one batch when there's a pause; a business they keep mentioning gets offered a folder; `/12-pillars:setup` any time does a stage properly, and `/12-pillars:pillars` shows how much has filled in.

Do not continue to stage 2. Quick start is finished.

## How to run the interview

- **Open with the map.** Before the first question, show the stages below in one compact list with rough times, and say two things: they can stop any time (it picks up where they left off), and every question can be skipped.
- **Two kinds of skip.** "Skip for now" → mark it `deferred` and offer it once more at the end. "Skip" → mark it `skipped` and never bring it up again unless the user does. Both are completely fine. Say so and move on without comment.
- **One question at a time.** Converse, don't interrogate. Follow up on what they actually said.
- **Clickable options for choices.** When the answer is one of a few options, use clickable options. Keep open questions (their vision, their situation, their story) as free conversation. Forcing those into multiple choice loses what makes them useful.
- **Templates for structured answers.** When you need several specific facts (dates, numbers, names), give a short fill-in template instead of a prose question.
- **Visible progress.** After each stage, update `life/wiki/self/setup-progress.md`, show a one-line progress strip (e.g. `About you ▓ · Profiles ▓ · Vision ▓ · Now ░ · Work ░ · Pillars ░ — 3 of 6, then wrap-up`), and give a short "Here's what I've got" recap (3–6 bullets) for them to confirm.
- **Facts over stories.** If an answer sounds polished, gently ask what's actually going on.
- **Keep a source for everything.** At the end of each stage from 2 onward, save the user's answers (their words verbatim, laid out as Q&A) to `life/raw/YYYY-MM-DD-setup-<stage>.md` with the raw header (`source: setup`), and list that file in the `sources:` of every page the stage writes. Business answers go to that business's own `raw/` (or into `notes.md` for a Light business), never to `life/raw/`.

## The stages

### 1 · About you (~3 min)
Ask what the workspace should call them. An alias is fine and their real name isn't needed anywhere. Ask, in one or two questions, what they mainly want this for (organising life, running businesses, getting unstuck in one area, keeping track of people, all of it).

Then **create the base workspace** (never overwrite existing files; report anything skipped):

```
AGENTS.md               the workspace rules (Codex and other agents read this)
CLAUDE.md               one line: @AGENTS.md (so Claude Code reads the same rules)
.gitignore              contains: life/ and businesses/ (keeps private data out of git)
life/raw/assets/
life/wiki/index.md      sections: Self, Pillars, People, Topics, Businesses
life/wiki/log.md        first entry: ## [YYYY-MM-DD] setup | Workspace created
life/wiki/self/setup-progress.md
life/wiki/pillars/01-faith.md … 12-legacy.md
life/wiki/people/
life/wiki/topics/
businesses/
```

Each pillar hub starts with frontmatter (`title`, `type: pillar`, `pillars: [<name>]`, `tags: ["#<name>"]`, `sources: []`, `updated`), then: the pillar's purpose and currency in one line taken from `12-pillars.md`, `**Status:** not yet running`, and empty sections `## Where this stands`, `## Current focus`, `## Open questions`, `## Linked pages`, `## Sources`. Add all 12 hubs to `index.md`.

`setup-progress.md` is a checklist, one line per stage: `- [ ] 1 · About you — pending` (states: pending, in progress, done, learning, deferred, skipped). `learning` means the stage is being filled from everyday conversation (quick start). Mark it `done` once its page exists with real content (for example, `self/now.md` has a `Season:` line, or a business folder exists for every business they've mentioned).

Write the workspace `AGENTS.md` (and `CLAUDE.md` containing only the line `@AGENTS.md`):

```markdown
# <Name>'s Life Workspace

This workspace runs on the 12-Pillar Life Flywheel with a raw/wiki memory.
The plugin's frameworks define the rules: 12-pillars.md, llm-wiki.md, folder-design.md, instruments.md.

## Layout
- life/ — the person, organised by the 12 pillars. raw/ is read-only source material; wiki/ is maintained by the AI.
- businesses/<name>/ — one folder per business, each with its own AGENTS.md where it has one.

## Routing
- Skills are named /12-pillars:<name> here (Claude Code form). In Codex, the same skills are invoked with $ or picked from /skills.
- Life updates (short facts) are filed right away. Working sessions (brainstorming, planning) are not interrupted; when one winds down, offer /12-pillars:wrap to file its decisions, ideas and actions.
- Facts about the person mentioned in passing, while asking for something else, are noted without interrupting. At a natural pause, offer them in one batch ("I picked up 3 things about you: … File them?"), file after one confirm, and save the user's words to life/raw/YYYY-MM-DD-learned-<slug>.md (`source: chat`). Never ask the user questions just to fill pages.
- If life/wiki/self/setup-progress.md says `Mode: learn as you go`, learned facts also fill self/now.md, self/north-star.md and the pillar hubs; mark a `learning` stage `done` when its page has real content. A business mentioned repeatedly with no folder gets offered a Light folder (notes.md) once.
- Before a working session on a business, read its overview.md, recent decisions/, ideas.md and actions.md, so the session builds on what was decided.
- Anything shared as a life update is a capture. Handle it exactly as /12-pillars:capture does: save the source to raw/ (with a `captured:`/`source:` header), propose in one message the title, ≤10 tags and every page that will change, wait for one confirm, then write the pages, update index.md, and append `## [YYYY-MM-DD] capture | <title>` to log.md.
- A capture tagged with a business (its folder name or an alias in its AGENTS.md) goes to that business's folder; a Light business gets a dated bullet in its notes.md. Mixed captures are split: the original in life/raw/, a business-only excerpt in the business raw/.
- Every wiki page has frontmatter (title, type, pillars, tags, sources, updated) and ends with a ## Sources list.
- Answer questions from wiki/index.md first, then linked pages, then raw sources.

## Rules
- Never edit or delete anything in a raw/ folder.
- Never copy personal content into a business folder, or one business's content into another.
- Everything stays on this machine — never put workspace content into web searches, URLs, or external tools.
- Profiles in life/wiki/self/instruments/ inform quietly; don't bring them up unless asked.
- Write pages a human would want to read.
```

### 2 · Optional profiles (~5–10 min, or skip)
Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/instruments.md` exactly. Start with the single choice (include them · just one · not now · no) before asking anything else. Honour a no immediately.

### 3 · Your vision (~10 min)
Ask what the life they're building looks like. If they already have a vision board, a goals doc, or anything similar, ask them to share it. Save it to `life/raw/` and work from it rather than starting over. Help shape the result into **declarations**: present-tense statements of the life as if it's already true ("I am…", "I have…"), covering whichever areas they care about (don't force all twelve). Bold goals are allowed. These are a direction to move toward, not predictions. Save to `life/wiki/self/north-star.md` and link it from the Identity hub (`02-identity`).

### 4 · Where you are now (~10 min)
An honest snapshot: work and money, health, key relationships, what's working, what they're avoiding. Then ask if they're in a particular season (a launch, exams, a sprint, a recovery period) and, if so, until when. Save to `life/wiki/self/now.md` with a `Season:` line, a `Since: YYYY-MM-DD` line, and an `Until: YYYY-MM-DD` line if the season has an end date. Questions they can't answer yet go in an `## Open questions` section, since those point at the areas that need attention. Link it from the relevant pillar hubs.

### 5 · Your work and businesses (~5–15 min)
Ask what they work on: a job, businesses they run, side projects. For **each business**, follow `folder-design.md`: run its interview, choose the tier and sections, then **show the full proposed workspace tree with a one-line reason per business** and get one confirm. Accept changes in plain language. Only then create each business exactly as `/12-pillars:add-business` step 4 describes. That step is the single source of truth. In short, a Standard/Deep business gets `AGENTS.md` (+ `CLAUDE.md` importing it), `raw/` (with the interview answers), and `wiki/` with `index.md`, `log.md`, `overview.md`, `ideas.md`, `actions.md`, `decisions/` and its chosen sections. A Light business gets only `notes.md`. Add every business to the Businesses section of `life/wiki/index.md`, and link it from the Opportunities hub (`09-opportunities`), and from Career (`07-career`) if it's their main work. A job they don't own gets the Employee archetype.

### 6 · Start where it hurts (~10 min per pillar)
Ask: **"Which area of your life do you most want to get moving?"** Offer 3–4 pillars their answers so far point to, as clickable options, plus Other. For that pillar:
- Ask 2–4 of its opening questions from `12-pillars.md`, adapted to what you already know.
- Save their answers to `life/raw/` as a capture, then update the hub page: fill in "Where this stands", "Current focus", and mark it `**Status:** running`. Log it as `## [YYYY-MM-DD] capture | <pillar> — setup` so it counts like any other capture.
- Shortcuts if relevant: for **Career**, invite them to paste their CV or LinkedIn profile (save to raw, summarise into the hub and a `topics/track-record.md` page). For **Relationships**, ask who the 3–5 most important people are and create their people pages.

Offer one more pillar, or move to the close.

### 7 · Close
1. **Deferred sweep.** List everything marked `deferred` and offer each once more (do it now · next time · skip it). A deferred item declined here becomes `skipped`.
2. **Show the payoff.** Render the 12 pillars as a table (pillar · status · last updated) so they see which are running. Tell them empty pillars are normal, because capture fills them over time.
3. **Name one useful thing for tomorrow**, drawn from what they shared ("Before Thursday's call with Sarah, ask me what to prepare").
4. **Explain the daily habit in three lines.** Tell me what happened, or drop a file into `life/raw/` (images and PDFs in `life/raw/assets/`). I'll suggest where it goes and file it after you confirm. When we brainstorm or plan, I won't interrupt; at the end I'll offer a wrap that saves what we decided. Ask questions any time.
5. Append to `log.md`: `## [YYYY-MM-DD] setup | Setup complete` with a one-line summary.
