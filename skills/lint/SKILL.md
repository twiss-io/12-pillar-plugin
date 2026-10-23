---
name: lint
description: "Health check for your wiki — finds contradictions, stale info, broken links and gaps, then fixes what you approve"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. "Clickable options" means a choice tool if you have one (AskUserQuestion in Claude Code), otherwise a short numbered list.

Run a health check on: `$ARGUMENTS` (default `all`: the `life/` wiki and every business wiki). If it is `rules`, skip the checks and go straight to **Refresh the rules** below.

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. **Report first, change nothing yet.**

## Check for
1. **Contradictions:** two pages saying different things (a person's job, a deal's status, a number).
2. **Stale claims:** something a newer raw source supersedes but the wiki still states.
3. **Index gaps:** pages missing from `index.md`, and index lines pointing at missing pages.
4. **Orphans:** pages nothing links to except `index.md`. Pillar hubs and `self/` pages are never orphans.
5. **Missing pages:** a person or topic mentioned across several pages without a page of its own.
6. **Broken links**, and pages missing frontmatter or a `## Sources` list. Skip `index.md`, `log.md`, and `self/setup-progress.md`, which are structural.
7. **Unprocessed sources:** raw files that no wiki page cites.
8. **Quiet pillars:** pillar hubs not updated in over 60 days, and people pages for close contacts with no contact in a long time or with an important date coming up in the next 14 days.
9. **Boundary leaks:** personal content copied into a business folder, content copied between businesses, or deal details sitting in the life wiki when that business has its own folder.
10. **Stale actions:** open `- [ ]` items in any `actions.md` (or `To do:` bullets in a `notes.md`) past their due date, or more than 30 days old with no date. Suggest ticking them off, re-dating them, or dropping them.
11. **Light businesses:** stale or contradictory bullets in `businesses/*/notes.md`, and Light businesses whose notes have grown big enough to suggest an upgrade (`/12-pillars:add-business <name>`).
12. **Outdated rules:** the workspace `AGENTS.md` is missing, has no `12-pillars rules:` stamp, or its number is lower than the one in `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`. The fix is **Refresh the rules**.

## Report
Group findings by type, most important first, each with the file and a proposed fix in one line. Then ask which to apply (all · pick · none) using clickable options.

## Apply (only what's approved)
Edit wiki pages only (plus `AGENTS.md`/`CLAUDE.md` for an approved rules refresh). Never touch `raw/`. Append to each affected `log.md`: `## [YYYY-MM-DD] lint | <n> fixes` with a one-line summary.

## Refresh the rules
Bring the workspace `AGENTS.md` up to the plugin's current template, `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`. This touches only `AGENTS.md` and `CLAUDE.md`, never `life/`, `businesses/` or anything in `raw/`.
1. Build the new file from the template: keep the name from the current title, and keep the current `## My additions` section word for word. Any other line that is clearly the user's own (a personal preference or rule, not an older wording of a plugin rule) moves into `## My additions` rather than being dropped.
2. If there is no `AGENTS.md` (workspaces from before v0.4.0 kept the rules in `CLAUDE.md`), build it from `CLAUDE.md` the same way.
3. Show what changes in a few plain-language bullets (new rules, changed rules, what moved to My additions) and get one confirm.
4. Write `AGENTS.md`, make `CLAUDE.md` contain only `@AGENTS.md`, and append `## [YYYY-MM-DD] lint | Rules refreshed to v<n>` to `life/wiki/log.md`.
