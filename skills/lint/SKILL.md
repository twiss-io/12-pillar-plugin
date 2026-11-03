---
name: lint
description: "Health check for your wiki — finds contradictions, stale info, broken links and gaps, then fixes what you approve"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Run a health check on: `$ARGUMENTS` (default `all`: every pillar folder and unit). If it is `rules`, skip the checks and go straight to **Refresh the rules** below.

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. **Report first, change nothing yet.**

## Check for
1. **Contradictions:** two pages saying different things (a person's job, a deal's status, a number).
2. **Stale claims:** something a newer raw source supersedes but a page still states.
3. **Index gaps:** pages missing from `index.md`, and index lines pointing at missing pages.
4. **Orphans:** pages nothing links to except `index.md`. Pillar READMEs, unit overviews, `02-identity/` pages, and pages inside a unit's sections are never orphans.
5. **Missing pages:** a person or topic mentioned across several pages without a page of its own.
6. **Broken links**, and pages missing frontmatter or a `## Sources` list. Skip `index.md`, `log.md`, `actions.md` and `setup-progress.md`, which are structural.
7. **Unprocessed sources:** raw files that no page cites.
8. **Quiet pillars:** running pillar READMEs not updated in over 60 days whose linked pages haven't changed either, and people pages for close contacts with no contact in a long time or with an important date coming up in the next 14 days.
9. **Copies:** the same content pasted into two pillars instead of linked, or unit details (a deal, a client, a course) sitting in a pillar README instead of its unit.
10. **Stale actions:** open `- [ ]` items in `actions.md` past their due date, or more than 30 days old with no date: suggest ticking them off, re-dating them, or dropping them. List those due in the next 14 days separately as coming up.
11. **Units:** empty units (an overview and nothing else for months: suggest keeping or archiving), units whose pages have grown big enough to suggest a section (`/12-pillars:add-business <unit>`), and finished units (graduated, left the job, closed the business): offer to mark them `(archived)` in the Units section and remove their routing names, so new captures stop going there.
12. **Outdated rules:** the workspace `AGENTS.md` is missing, has no `12-pillars rules:` stamp, or its number is lower than the one in `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`; or a pillar folder is missing its `AGENTS.md`. The fix is **Refresh the rules**.

## Report
Group findings by type, most important first, each with the file and a proposed fix in one line. Then ask which to apply (all · pick · none) using clickable options.

## Apply (only what's approved)
Edit pages, `index.md` and `actions.md` only (plus `AGENTS.md`/`CLAUDE.md` files for an approved rules refresh). Never touch `raw/`. Append to `log.md`: `## [YYYY-MM-DD] lint | <n> fixes` with a one-line summary.

## Refresh the rules
Bring the workspace `AGENTS.md` up to the plugin's current template, `${CLAUDE_PLUGIN_ROOT}/templates/workspace-AGENTS.md`. If the workspace still has the older layout (`life/wiki/index.md` exists), do **Move to the pillar folders** below first.
1. Build the new file from the template: keep the name from the current title, and keep the current `## My additions` section word for word. Any other line that is clearly the user's own (a personal preference or rule, not an older wording of a plugin rule) moves into `## My additions` rather than being dropped.
2. If there is no `AGENTS.md` (workspaces from before v0.4.0 kept the rules in `CLAUDE.md`), build it from `CLAUDE.md` the same way.
3. Give every pillar folder an `AGENTS.md` from `${CLAUDE_PLUGIN_ROOT}/templates/pillar-AGENTS.md` and a `CLAUDE.md` containing `@AGENTS.md`, where missing.
4. Show what changes in a few plain-language bullets (new rules, changed rules, what moved to My additions) and get one confirm.
5. Write the files, make the root `CLAUDE.md` contain only `@AGENTS.md`, and append `## [YYYY-MM-DD] lint | Rules refreshed to v<n>` to `log.md`.

## Move to the pillar folders (one time, for workspaces from before 0.8.0)
Older workspaces have `life/` (with `raw/` and `wiki/`) plus area folders (`study/`, `work/`, `content/`, `investing/`, `businesses/<name>/`). Move them into the pillar layout in `llm-wiki.md` section 2. Show the plan first as a short before → after list and get one confirm; it touches every file, so also suggest they copy the folder somewhere first.
1. **Raw:** move every file from `life/raw/` and each area's `raw/` into `raw/` (assets into `raw/assets/`), contents unchanged. On a name clash, the `life/raw/` file keeps its name and the area's file gets the area name as a prefix (`work-2026-10-21-…`). This is the one time raw files are moved.
2. **Pillars:** `life/wiki/pillars/NN-<name>.md` → `NN-<name>/README.md`. `life/wiki/self/*` → `02-identity/` (`setup-progress.md` → the workspace root). `life/wiki/people/` → `06-relationships/people/`. Each `life/wiki/topics/` page → the folder of the first pillar in its `pillars:` frontmatter (or the method table in `llm-wiki.md`); a topic page about something that becomes a unit merges into that unit's `overview.md`. `life/wiki/log.md` → the root (kept as is). Old `index.md` files are dropped; the root one is rebuilt in step 5.
3. **Areas → units:** `study/` → `05-development/<school>/`, `work/` → `07-career/<employer>/`, each `businesses/<name>/` → `09-opportunities/<name>/`, `investing/` → `10-finance/investing/`, `content/` → `08-brand/`. An area's `wiki/` contents move up one level into the unit (its `overview.md`, sections, `decisions/`, `ideas.md`); its people pages go to `06-relationships/people/` (merged with any existing page of the same person); its `log.md` entries not already in the life log (same date and kind) are appended to the root `log.md`; its routing aliases go into the unit's `**Names:**` line and the Units section (`content/`'s go on a `**Names:**` line in `08-brand/README.md`). An older notes-only area (just `notes.md`) moves to the unit as a raw file, and its bullets are filed as a capture.
4. **Actions:** every `actions.md` (and `To do:` bullets) merges into the root `actions.md`, each line tagged with its pillar (and unit), with any date rewritten as `due YYYY-MM-DD`.
5. **Links:** rewrite every relative link and `sources:` path to the new locations (links to a merged `actions.md` point to the root one, and old folder names in link text are updated), rebuild `index.md` (one section per pillar, then Units), then remove the emptied old folders and their old `AGENTS.md`/`CLAUDE.md` files.
6. Report what moved in a few lines, log `## [YYYY-MM-DD] lint | Moved to the pillar folders`, then run the checks above once, so finished units can be archived and anything left over is caught.
