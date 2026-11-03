---
name: capture
description: "The daily habit: save what happened as a source, propose which pages it updates, confirm once, then file it everywhere it belongs"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

You are capturing: `$ARGUMENTS` (text the user wrote, a file path, or empty, in which case process any files in `life/raw/` and every area's `raw/` (each folder in the Areas section of `life/wiki/index.md`, e.g. `study/`, `work/`, `businesses/*/`) that no wiki page cites yet, oldest first. Files the user dropped in themselves are left exactly as they are: no rename, no added header).

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md` for formats and rules (including which page each method's notes go on), and `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md` for which pillars a piece of information touches. If there is no workspace yet (no `life/wiki/index.md`), offer `/12-pillars:setup` instead.

## 1 · Read
Read the item. Images count too: a receipt → money figures (#finance), a meal or workout → #health, a screenshot of a chat → the people and what was agreed. If you can't read a file (audio, unreadable image), ask for a one-line summary rather than guessing.

## 2 · Propose (one message)
- **Title:** one line.
- **Tags:** up to 10: pillar tags (`#faith` … `#legacy`), people (`#<name>`), areas (businesses, `#study`, `#work`) and topics. Reuse existing tags (search the `tags:` frontmatter across the wiki) and existing page names (check `index.md`) before inventing new ones.
- **Where it goes:** `life/` by default. If it's about an area that has a folder (a business, `study/`, `work/`, `content/`, `investing/`, listed in the Areas section of `life/wiki/index.md`), it goes there. Match the folder name, or an alias listed in the area's `AGENTS.md` or the `Tags:` line of its `notes.md`. Route by what the item is, with aliases as hints: a post they published goes to `content/wiki/posts/` (created if missing) even when it mentions a client or their employer. If it's mixed, split it explicitly: the original stays in `life/raw/`, and an area-only excerpt goes to the area.
- **What changes:** list each page to create or update with a few words on what changes. Example: "people/marcus-tan.md: daughter started uni; owes you the revised timeline" · "businesses/acme-studio/wiki/proposals/marcus-rebrand.md: new, ~20K budget" · "pillars/09-opportunities.md: link to that proposal". Deal details live in the business folder. The life hub only links to them.
- **Deadlines and to-dos:** anything with a due date or a clear to-do goes in that folder's `wiki/actions.md` as `- [ ] <what> — due YYYY-MM-DD` (personal ones in `life/wiki/actions.md`, created if missing), so they're all in one place. If it shows an open action was done, propose ticking it off.
- **Worth noting:** if it records a win someone witnessed, suggest asking for a testimonial now. If it contradicts something in the wiki (a changed job: offer a folder for the new one and archiving the old; an ended plan; an ended relationship: ask which circle the person is in now), point it out.

Ask for one confirm. Accept corrections in plain language ("drop the last tag", "it's 25K not 20K").

## 3 · File (after confirm)
1. Save the source to the destination's `raw/` as `YYYY-MM-DD-<slug>.md` (or copy the given file there; binaries to `raw/assets/`), unchanged, with the capture header. If it was already in `raw/`, leave it as it is. For a mixed capture, also save the area-only excerpt to the area's `raw/` with `source: excerpt of life/raw/<file>`.
   - **Older notes-only area** (just `notes.md`, no `raw/` or `wiki/`): append a dated bullet to its `notes.md`, log it in `life/wiki/log.md`, and offer once to give it the full structure (`add-business <folder>`).
2. Make the confirmed page changes, keeping each page's frontmatter (`updated`, `sources`, `tags`) and `## Sources` list current.
3. Add any new pages to that folder's `wiki/index.md`.
4. Append to that folder's `wiki/log.md`: `## [YYYY-MM-DD] capture | <title>` plus 1–2 lines naming the pages touched.
5. For every pillar hub this capture touched, refresh its "Where this stands" summary. If it was `not yet running` and this source gives real detail about that pillar, set `**Status:** running`.

## 4 · Report
One short line per page changed. If the records show a real change from the person's normal (sleep well below what they usually get, spending above their base number, a pipeline that has gone empty), add one plain question about what might be driving it, per `12-pillars.md` section 3 ("That's two weeks well under your usual sleep. Anything changed in how your weeks are going?"). Nothing more.

**Rules:** never write before the confirm; never more than 10 tags; never edit an existing raw file; never copy personal content into an area folder or between areas; never put workspace content into web searches or external tools.
