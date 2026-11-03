---
name: dashboard
description: "Open a local dashboard of your second brain: the 12 pillars (click one to see everything in it), deadlines, season, people, units and recent activity, as a page in your browser"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Build the user's dashboard. Needs a workspace (`index.md` and the pillar folders). If there isn't one, offer `/12-pillars:setup`.

1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.py" "<workspace folder>"`. It reads the workspace's markdown and writes `dashboard.html` in the workspace folder. It changes nothing else and loads nothing from the internet. If `python3` is missing, say so in one line and stop.
2. Open it for them (`open dashboard.html` on a Mac, `xdg-open` on Linux, `start` on Windows). If you can't open files, give the path.
3. Reply in at most three lines: where the file is, the one thing that most needs attention (the nearest deadline or an overdue one; otherwise the pillar `/12-pillars:pillars` would recommend), and that it refreshes itself at the start of each session (or ask again any time).

Never edit wiki or raw files here.
