---
name: pillars
description: "See your 12 pillars at a glance, score them, and find the one to work on next"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Show the user where their 12 pillars stand. Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`. Needs a workspace. If `life/wiki/pillars/` doesn't exist, offer `/12-pillars:setup`.

## 1 · The dashboard (read-only)
Read the 12 hub pages in `life/wiki/pillars/` and render one compact table:

| # | Pillar | Status | Last updated | Linked pages | One-line state |
|---|---|---|---|---|---|

Status comes from each hub's `**Status:**` line (not yet running / running). "One-line state" comes from its "Where this stands" section, or "—" if it's empty. Add one line below the table: how many pillars are running, and how many captures and wraps were logged this month (count `capture` and `wrap` headings in `life/wiki/log.md` and every area's `wiki/log.md`, the areas being those in the Areas section of `life/wiki/index.md`; count a wrap logged in several places once). If `life/wiki/self/setup-progress.md` says `Mode: learn as you go`, add one more line: which setup stages are still `learning`, and that `/12-pillars:setup` can do any of them properly in a few minutes.

## 2 · Optional self-score
Offer (clickable: score them now · skip): the user rates **all 12** pillars 1–10 (or "don't know" for one they haven't thought about), as a fill-in template. Save the scores with today's date in a `## Scores` section of `life/wiki/self/now.md`, placed just above `## Sources`. Keep earlier scores, since the trend is useful.

## 3 · One recommendation
Name exactly **one** pillar to work on next and why, using the flywheel:
- Prefer the weakest pillar that is **upstream** of other weak ones. Fixing it lifts the ones after it.
- If nothing is scored, pick the running pillar with the oldest update, or a not-yet-running pillar the user's `north-star.md` or `now.md` says matters.
- Say which pillar upstream or downstream it affects, in one sentence.

Then offer to start on it now: ask that pillar's opening questions from the framework and file the answers as a capture.

Change nothing except the scores the user chooses to save.
