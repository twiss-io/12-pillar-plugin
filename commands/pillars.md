---
description: "See your 12 pillars at a glance, score them, and find the one to work on next"
---

Show the user where their 12 pillars stand. Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`. Needs a workspace. If `life/wiki/pillars/` doesn't exist, offer `/12-pillars:setup`.

## 1 · The dashboard (read-only)
Read the 12 hub pages in `life/wiki/pillars/` and render one compact table:

| # | Pillar | Status | Last updated | Linked pages | One-line state |
|---|---|---|---|---|---|

Status comes from each hub's `**Status:**` line (not yet running / running). "One-line state" comes from its "Where this stands" section, or "—" if it's empty. Add one line below the table: how many pillars are running, and how many captures and wraps were logged this month (count `capture` and `wrap` headings in `life/wiki/log.md` and every `businesses/*/wiki/log.md`). If `life/wiki/self/setup-progress.md` says `Mode: learn as you go`, add one more line: which setup stages are still `learning`, and that `/12-pillars:setup` can do any of them properly in a few minutes.

## 2 · Optional self-score
Offer (clickable: score them now · skip): the user rates **all 12** pillars 1–10 (or "don't know" for one they haven't thought about), as a fill-in template. Save the scores with today's date in a `## Scores` section of `life/wiki/self/now.md`, placed just above `## Sources`. Keep earlier scores, since the trend is useful.

## 3 · One recommendation
Name exactly **one** pillar to work on next and why, using the flywheel:
- Prefer the weakest pillar that is **upstream** of other weak ones. Fixing it lifts the ones after it.
- If nothing is scored, pick the running pillar with the oldest update, or a not-yet-running pillar the user's `north-star.md` or `now.md` says matters.
- Say which pillar upstream or downstream it affects, in one sentence.

Then offer to start on it now: ask that pillar's opening questions from the framework and file the answers as a capture.

Change nothing except the scores the user chooses to save.
