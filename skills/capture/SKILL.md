---
name: capture
description: "The daily habit: save what happened as a source, propose which pages it updates, confirm once, then file it everywhere it belongs"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. "Clickable options" means a choice tool whenever one is available: AskUserQuestion in Claude Code; in Codex, request_user_input_async (or request_user_input in Plan mode), and after asking with the async one, end your turn and wait for the answer. Only without any such tool, a short numbered list (one option per line) the user can answer by number.

You are capturing: `$ARGUMENTS` (text the user wrote, a file path, or empty, in which case process any files in `life/raw/` and every area's `raw/` (`study/`, `work/`, `investing/`, `businesses/*/`) that no wiki page cites yet, oldest first. Files the user dropped in themselves are left exactly as they are: no rename, no added header).

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md` for formats and rules, and `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md` for which pillars a piece of information touches. If there is no workspace yet (no `life/wiki/index.md`), offer `/12-pillars:setup` instead.

## 1 · Read
Read the item. Images count too: a receipt → money figures (#finance), a meal or workout → #health, a screenshot of a chat → the people and what was agreed. If you can't read a file (audio, unreadable image), ask for a one-line summary rather than guessing.

## 2 · Propose (one message)
- **Title:** one line.
- **Tags:** up to 10: pillar tags (`#faith` … `#legacy`), people (`#<name>`), areas (businesses, `#study`, `#work`) and topics. Reuse existing tags (search the `tags:` frontmatter across the wiki) and existing page names (check `index.md`) before inventing new ones.
- **Where it goes:** `life/` by default. If it's about an area that has a folder (a business, `study/`, `work/`, `investing/`, listed in the Areas section of `life/wiki/index.md`), it goes there. Match the folder name, or an alias listed in the area's `AGENTS.md` or the `Tags:` line of its `notes.md`. If it's mixed, split it explicitly: the original stays in `life/raw/`, and a business-only excerpt goes to the business.
- **What changes:** list each page to create or update with a few words on what changes. Example: "people/marcus-tan.md: daughter started uni; owes you the revised timeline" · "businesses/acme-studio/wiki/proposals/marcus-rebrand.md: new, ~20K budget" · "pillars/09-opportunities.md: link to that proposal". Deal details live in the business folder. The life hub only links to them.
- **Worth noting:** if it shows an open action in some `actions.md` was done, propose ticking it off. If it records a win someone witnessed, suggest asking for a testimonial now. If it contradicts something in the wiki (a changed job, an ended plan), point it out.

Ask for one confirm. Accept corrections in plain language ("drop the last tag", "it's 25K not 20K").

## 3 · File (after confirm)
1. Save the source to the destination's `raw/` as `YYYY-MM-DD-<slug>.md` (or copy the given file there; binaries to `raw/assets/`), unchanged, with the capture header. If it was already in `raw/`, leave it as it is. For a mixed capture, also save the business-only excerpt to the business's `raw/` with `source: excerpt of life/raw/<file>`.
   - **Light area:** there is no `raw/` or `wiki/`. Append a dated bullet to its `notes.md` instead, and log it in `life/wiki/log.md`.
2. Make the confirmed page changes, keeping each page's frontmatter (`updated`, `sources`, `tags`) and `## Sources` list current.
3. Add any new pages to that folder's `wiki/index.md`.
4. Append to that folder's `wiki/log.md`: `## [YYYY-MM-DD] capture | <title>` plus 1–2 lines naming the pages touched.
5. For every pillar hub that got a new link, refresh its "Where this stands" summary. If it was `not yet running`, set `**Status:** running`.

## 4 · Report
One short line per page changed. Nothing more.

**Rules:** never write before the confirm; never more than 10 tags; never edit an existing raw file; never copy personal content into an area folder or between areas; never put workspace content into web searches or external tools.
