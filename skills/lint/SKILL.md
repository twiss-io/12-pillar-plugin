---
name: lint
description: "Health check for your wiki — finds contradictions, stale info, broken links and gaps, then fixes what you approve"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. "Clickable options" means a choice tool if you have one (AskUserQuestion in Claude Code), otherwise a short numbered list.

Run a health check on: `$ARGUMENTS` (default `all`: the `life/` wiki and every business wiki).

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

## Report
Group findings by type, most important first, each with the file and a proposed fix in one line. Then ask which to apply (all · pick · none) using clickable options.

## Apply (only what's approved)
Edit wiki pages only. Never touch `raw/`. Append to each affected `log.md`: `## [YYYY-MM-DD] lint | <n> fixes` with a one-line summary.
