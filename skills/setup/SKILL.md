---
name: setup
description: "Set up your 12-pillar life workspace: a guided interview, then a folder structure recommended for your life, studies, job or businesses, built after you confirm"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

You are setting up a 12-pillar life workspace for the user. Before starting, read these three files in full. They define everything you build here:
- `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`: the life framework
- `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`: the folder layout, file formats, and rules
- `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md`: how to recommend folders for their studies, job, businesses and investing

Bundled instruments, with full paths, for stage 2:
- Astrology script: `${CLAUDE_PLUGIN_ROOT}/instruments/bazi.py`
- Enneagram protocol: `${CLAUDE_PLUGIN_ROOT}/instruments/enneagram-typing.md`

## Before anything

**Location.** The current directory becomes the workspace. If it looks like a code repository or someone else's project (has `package.json`, `src/`, a `.git` with commits not belonging to a personal workspace, etc.), stop and ask the user to confirm or to open a new chat in a fresh folder such as `~/my-life`.

**Resuming.** If `life/wiki/self/setup-progress.md` exists, this is a resume. Show the map of stages marked done / in progress / learning / deferred / skipped, and ask where to pick up (clickable options: continue where we stopped · do something I put off · revisit something I skipped · wrap up). For a stage marked `learning`, first show what has already been picked up about it, then ask only what's missing. Never force the original order on a resume.

**Outdated rules.** Only if a workspace already exists here (`life/wiki/index.md` exists): if its `AGENTS.md` is missing, or its `12-pillars rules:` number is lower than the one in `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`, offer once to refresh it first, exactly as `/12-pillars:lint rules` does.

## Choose how to start

On a fresh start (no `setup-progress.md`), offer one choice as clickable options before anything else:
- **Full setup now (~45 min):** the guided interview below, stages 1–7.
- **Choose parts:** set up only the parts they pick now; the rest is learned as we go.
- **Quick start (~2 min), learn as we go:** set up the base workspace now, then fill it in from normal conversation over time.

**Choose parts** asks one multi-select question (clickable options; with Claude's 4-option limit, split it into two questions in one call: profiles · vision · where you are now, then work and businesses · start where it hurts) with the stages and their times: Optional profiles (~5–10 min) · Your vision (~10 min) · Where you are now (~10 min) · Your work, studies and businesses (~2–15 min) · Start where it hurts (~10 min). Stage 1 (About you) always runs, since it builds the workspace. Then:
1. Run stage 1, then only the chosen stages, in the usual order, with the same interview rules. Show the progress strip counting just the chosen stages.
2. In `setup-progress.md`, mark unchosen stages 3–6 `learning` (unchosen profiles: `skipped`, so the close doesn't offer them again) and add `Mode: learn as you go`, unless every stage was chosen.
3. Finish with stage 7, but in its deferred sweep, don't offer the `learning` stages again; say in one line that they fill in from conversation and `/12-pillars:setup` can do any of them later.

**Quick start** runs only stage 1, cut down: ask what the workspace should call them (one question, alias fine), skip the "what for" question, and create the base workspace exactly as stage 1 describes. Then ask the open "What fills your days?" question from `folder-design.md` section 1 (free text, not buttons), with at most one follow-up if something is unclear. Choose each area's tier from what they already said, with no interview (`folder-design.md` section 3, "Tier from a quick-start answer"). Then show the **full proposed tree as a code block** in your message: `AGENTS.md`, `life/` with its `raw/` and `wiki/`, and every area with its own `raw/` + `wiki/` and its sections (none yet for Light), each with one line on why. Never ask for the confirm with only a list of folder names. Get one confirm, accept changes in plain language, and create those areas as `add-business` step 4 describes for their tier, adding each to the Areas section of the index. If they're between things, it adds nothing beyond `life/`. Then:
1. In `setup-progress.md`, add the line `Mode: learn as you go` under the title, mark stage 1 `done`, stage 2 (profiles) `deferred`, stages 3, 4 and 6 `learning`, and stage 5 `done` once they answered (even "between things"), `learning` if they skipped.
2. Save their answers (what to call them, what fills their days) to `life/raw/YYYY-MM-DD-setup-about-you.md` (`source: setup`), and add a `Sources: YYYY-MM-DD-setup-about-you.md` line to `setup-progress.md` so it counts as filed.
3. Log `## [YYYY-MM-DD] setup | Quick start`.
4. Tell them, in four short lines: just use this folder for anything; when they mention something about themselves along the way, it's noted without interrupting, and offered for filing in one batch when there's a pause; their areas start as one notes page each and get offered a fuller structure once they grow, and anything new they keep mentioning gets offered a folder; `/12-pillars:setup` any time does a stage properly, and `/12-pillars:pillars` shows how much has filled in.

Do not continue to stage 2. Quick start is finished.

## How to run the interview

- **Open with the map.** Before the first question, show the stages below in one compact list with rough times, and say two things: they can stop any time (it picks up where they left off), and every question can be skipped.
- **Two kinds of skip.** "Skip for now" → mark it `deferred` and offer it once more at the end. "Skip" → mark it `skipped` and never bring it up again unless the user does. Both are completely fine. Say so and move on without comment.
- **One question at a time.** Converse, don't interrogate. Follow up on what they actually said.
- **Clickable options for choices.** When the answer is one of a few options, use clickable options. Keep open questions (their vision, their situation, their story) as free conversation. Forcing those into multiple choice loses what makes them useful.
- **Templates for structured answers.** When you need several specific facts (dates, numbers, names), give a short fill-in template instead of a prose question.
- **Visible progress.** After each stage, update `life/wiki/self/setup-progress.md`, show a one-line progress strip (e.g. `About you ▓ · Profiles ▓ · Vision ▓ · Now ░ · Work ░ · Pillars ░ — 3 of 6, then wrap-up`), and give a short "Here's what I've got" recap (3–6 bullets) for them to confirm.
- **Facts over stories.** If an answer sounds polished, gently ask what's actually going on.
- **Keep a source for everything.** At the end of each stage from 2 onward, save the user's answers (their words verbatim, laid out as Q&A) to `life/raw/YYYY-MM-DD-setup-<stage>.md` with the raw header (`source: setup`), and list that file in the `sources:` of every page the stage writes. An area's answers go to that area's own `raw/`, never to `life/raw/`.

## The stages

### 1 · About you (~3 min)
Ask what the workspace should call them. An alias is fine and their real name isn't needed anywhere. Ask, in one or two questions, what they mainly want this for (organising life, studies, work or a business, getting unstuck in one area, keeping track of people, all of it).

Then **create the base workspace** (never overwrite existing files; report anything skipped):

```
AGENTS.md               the workspace rules (Codex and other agents read this)
CLAUDE.md               one line: @AGENTS.md (so Claude Code reads the same rules)
.gitignore              ignores everything except AGENTS.md, CLAUDE.md and itself (keeps private data out of git)
life/raw/assets/
life/wiki/index.md      sections: Self, Pillars, People, Topics, Areas
life/wiki/log.md        first entry: ## [YYYY-MM-DD] setup | Workspace created
life/wiki/self/setup-progress.md
life/wiki/pillars/01-faith.md … 12-legacy.md
life/wiki/people/
life/wiki/topics/
```

The `.gitignore` is four lines: `/*`, `!/AGENTS.md`, `!/CLAUDE.md`, `!/.gitignore`, so every folder, whatever it's called, stays out of git.

No area folders yet (`study/`, `work/`, `businesses/`…). Those come only from what the user chooses in stage 5, or the quick start question.

Each pillar hub starts with frontmatter (`title`, `type: pillar`, `pillars: [<name>]`, `tags: ["#<name>"]`, `sources: []`, `updated`), then: the pillar's purpose and currency in one line taken from `12-pillars.md`, `**Status:** not yet running`, and empty sections `## Where this stands`, `## Current focus`, `## Open questions`, `## Linked pages`, `## Sources`. Add all 12 hubs to `index.md`.

`setup-progress.md` is a checklist, one line per stage: `- [ ] 1 · About you — pending` (states: pending, in progress, done, learning, deferred, skipped). `learning` means the stage is being filled from everyday conversation (quick start). Mark it `done` once its page exists with real content (for example, `self/now.md` has a `Season:` line, or an area folder exists for every business, job or studies they've mentioned).

Write the workspace `AGENTS.md` by copying `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md` exactly, with `<Name>` replaced by what they want to be called. Keep the `12-pillars rules:` stamp line; it is how later plugin versions notice the rules need a refresh. Write `CLAUDE.md` containing only the line `@AGENTS.md`.

### 2 · Optional profiles (~5–10 min, or skip)
Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/instruments.md` exactly. Start with the single choice (include them · just one · not now · no) before asking anything else. Honour a no immediately.

### 3 · Your vision (~10 min)
Ask what the life they're building looks like. If they already have a vision board, a goals doc, or anything similar, ask them to share it. Save it to `life/raw/` and work from it rather than starting over. Help shape the result into **declarations**: present-tense statements of the life as if it's already true ("I am…", "I have…"), covering whichever areas they care about (don't force all twelve). Bold goals are allowed. These are a direction to move toward, not predictions. Save to `life/wiki/self/north-star.md` and link it from the Identity hub (`02-identity`).

### 4 · Where you are now (~10 min)
An honest snapshot: work and money (one line per job, studies or business here, since the detail belongs in its own folder from stage 5), health, key relationships, what's working, what they're avoiding. Then ask if they're in a particular season (a launch, exams, a sprint, a recovery period) and, if so, until when. Save to `life/wiki/self/now.md` with a `Season:` line, a `Since: YYYY-MM-DD` line, and an `Until: YYYY-MM-DD` line if the season has an end date. Questions they can't answer yet go in an `## Open questions` section, since those point at the areas that need attention. Link it from the relevant pillar hubs.

### 5 · Your work, studies and businesses (~2–15 min)
Follow `folder-design.md`. Ask its open "What fills your days?" question (free text), which gives the areas: `study/`, `work/`, one `businesses/<name>/` per business, practice or channel, `investing/`, or none if they're between things. For **each area**, run its short interview from section 2 and choose the tier and sections. Then **show the full proposed workspace tree with a one-line reason per area** and get one confirm. Accept changes in plain language, including their own folder names ("call it uni"). Only then create each area exactly as `/12-pillars:add-business` step 4 describes; that step is the single source of truth. In short, a Standard/Deep area gets `AGENTS.md` (+ `CLAUDE.md` importing it), `raw/` (with the interview answers), and `wiki/` with `index.md`, `log.md`, `overview.md`, `ideas.md`, `actions.md`, `decisions/` and its chosen sections. A Light area gets only `notes.md`. Add every area to the Areas section of `life/wiki/index.md` and link it from the pillar hubs as `add-business` step 5 describes. If they chose nothing, say in one line that `life/` covers it for now and a folder gets offered when something grows.

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
