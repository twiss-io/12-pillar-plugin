---
name: pillars
description: "See your 12 pillars at a glance: opens your dashboard (the flywheel, deadlines, season, people, units; click a pillar to see everything in it), lets you score them, and names the one to work on next. Also the morning brief (`brief`) and the weekly review (`week`), which can run on a schedule"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Asked for: `$ARGUMENTS`. Empty → the overview below (sections 1–3). `brief` (or "morning brief") → **Morning brief** only. `week` (or "weekly review") → **Weekly review** only. Both can run unattended as a scheduled automation: then never ask questions or wait for answers, just do it and finish.

Show the user where their 12 pillars stand. Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`. Needs a workspace. If the pillar folders (`01-faith/` … `12-legacy/`) don't exist, offer `/12-pillars:setup`.

## 1 · The dashboard (read-only)
1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.py" "<workspace folder>"`. It reads the workspace's markdown and writes `dashboard.html` in the workspace folder, changes nothing else, and loads nothing from the internet. Open it for them (`open` on a Mac, `xdg-open` on Linux, `start` on Windows); if you can't open files, give the path. It refreshes itself at the start of each session.
2. In the chat, render one compact table from the 12 pillar READMEs (`NN-<name>/README.md`):

| # | Pillar | Status | Last updated | One-line state |
|---|---|---|---|---|

Status comes from each hub's `**Status:**` line (not yet running / running). "One-line state" comes from its "Where this stands" section, or "—" if it's empty. Add one line below it: how many pillars are running, the nearest or overdue deadline from `actions.md`, and how many captures and wraps were logged this month (count `capture` and `wrap` headings in `log.md`). If `setup-progress.md` says `Mode: learn as you go`, add one more line: which setup stages are still `learning`, and that `/12-pillars:setup` can do any of them properly in a few minutes. If `python3` is missing, say so in one line and show only the table.

## 2 · Optional self-score
Offer (clickable: score them now · skip): the user rates **all 12** pillars 1–10 (or "don't know" for one they haven't thought about), as a fill-in template. Save them in a `## Scores` section of `02-identity/now.md`, placed just above `## Sources`, as a `### YYYY-MM-DD` heading with one line per pillar (`- Faith: 7`, `- Health: don't know`). The dashboard reads the latest block; re-run the script after saving. Keep earlier scores, since the trend is useful.

## 3 · One recommendation
Name exactly **one** pillar to work on next and why, using the flywheel:
- Prefer the weakest pillar that is **upstream** of other weak ones. Fixing it lifts the ones after it.
- If nothing is scored, pick the running pillar with the oldest update, or a not-yet-running pillar the user's `02-identity/north-star.md` or `now.md` says matters.
- Say which pillar upstream or downstream it affects, in one sentence.

Then offer to start on it now: read that pillar's section in `${CLAUDE_PLUGIN_ROOT}/frameworks/pillar-playbook.md`, ask its questions, offer the one method that fits (not one they already have a page for), and file the answers as `llm-wiki.md` section 4 describes.

In the overview, change nothing except the scores the user chooses to save.

## Morning brief (`brief`)
Read `actions.md`, the people pages in `06-relationships/people/`, `02-identity/now.md` (season and latest scores) and the end of `log.md`. Write nothing except a refreshed dashboard (run the script in step 1 if `dashboard.html` exists). Reply in at most 12 short lines, skipping any heading with nothing under it:

```
Morning, <name> · <weekday> <date> · <season, if any>
⏰ Today: <reminders and items due today, with times, earliest first>
🔴 Overdue: <what — due date>
📅 Coming up: <the next 3–5 dated items in the next 7 days>
👥 Reach out: <people past their check-in cadence, or with a birthday or important date in the next 7 days>
→ <one nudge: the single most useful thing to do today, from the above or the weakest upstream pillar>
```

If nothing is due and nobody needs a check-in, say so in one line and give only the nudge. Plain words, no pillar jargon, no lecture.

## Weekly review (`week`)
Covers the last 7 days. Read `log.md` (this week's entries), `actions.md`, the pillar READMEs touched this week, `02-identity/now.md` and `02-identity/north-star.md`.
1. **What moved:** one line for each pillar that had activity this week (what was captured, decided, done). Pillars with none are listed together on one line.
2. **What's slipping:** overdue actions, items open more than 30 days, close people past their cadence, a running pillar with no activity for over a month, or a real change from their normal (sleep, spending, hours) in the pages.
3. **Worth revisiting:** one or two older ideas (`ideas.md`) or decisions (`decisions/`) from more than a month ago that relate to what they're working on now, each with one line on why it's relevant. Skip this if nothing truly fits.
4. **Next week:** one focus, chosen by the flywheel (the weakest upstream pillar, or what the season calls for), plus the 3 most important actions already in `actions.md`.

Save it as `03-time/reviews/YYYY-MM-DD-week.md` (standard frontmatter, `type: review`; its `## Sources` lists `log.md` and the pages it drew from), link it from `03-time/README.md`, add it to `index.md`, and append `## [YYYY-MM-DD] review | Week of <date>` to `log.md`. Then show it, at most 20 lines. Don't change other pages or actions: suggestions stay suggestions until the user acts on them.

## Running them on a schedule
In the Codex app, create two automations on the workspace folder: one daily at the time they choose with the prompt `$12-pillars:pillars brief`, one weekly (e.g. Sunday evening) with `$12-pillars:pillars week`. They run only while the computer is awake and Codex is open. If the user asks how to set this up, give these two prompts and that limit in a few lines.
