---
name: add-business
description: "Add a business, your job, your studies or investing as its own folder (or upgrade one) — a short interview, a recommended structure, built after you confirm"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Add or upgrade an area: `$ARGUMENTS`. An area is a business, freelance practice or channel (`businesses/<name>/`), their studies (`study/`), their job (`work/`), or investing (`investing/`). If empty, ask which, as clickable options; for a business, ask its name.

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md` and `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. Needs a workspace (`life/wiki/index.md` exists). If there isn't one, offer `/12-pillars:setup`.

1. **New or existing?** The folder is `study/`, `work/` or `investing/` (or the name the user prefers for it), or `businesses/<kebab-cased name>/` for a business. Check the Areas section of `life/wiki/index.md` (older workspaces: Businesses) for folders already in use.
   - If the folder doesn't exist, it's a new area.
   - If it exists as **Light** (just `notes.md`), offer to upgrade it to Standard or Deep. Keep `notes.md` by moving it into the new `raw/` as a source, then build wiki pages from it.
   - If it's already Standard or Deep, offer to add sections instead. Never overwrite existing files.
2. **Interview.** Ask the questions for this kind of area in `folder-design.md` section 2, one at a time, using clickable options where the answer is a choice. Also ask what short names they'll actually use for it (aliases such as `#acme` for `acme-studio`).
3. **Recommend.** Show the proposed folder tree with the tier, the sections, and one line on why. Get one confirm and accept changes in plain language.
4. **Build.** This is the single spec for creating an area folder, and setup uses it too.
   - **Standard/Deep:**
     - Write `AGENTS.md` (plus a `CLAUDE.md` containing only `@AGENTS.md`): what it is, the user's role, tier, the sections and what goes in each, the routing tags (folder name plus aliases), and the boundary rule.
     - Create `raw/` and save the interview answers there as `YYYY-MM-DD-setup-interview.md` (the user's words verbatim in a Q&A layout, header `source: setup`).
     - Create `wiki/index.md` with sections: Overview (lines for overview, ideas, actions), one per chosen folder, then Decisions.
     - Create `wiki/ideas.md` (parked ideas) and `wiki/actions.md` (sections `## Open actions` and `## Open questions`), both with standard frontmatter.
     - Always create `wiki/decisions/`, even if it wasn't one of the chosen sections.
     - Create `wiki/log.md` with first entry `## [YYYY-MM-DD] setup | Area folder created`.
     - Write `wiki/overview.md` from what they told you, with standard frontmatter citing the interview file and a `## Sources` section. It links to `ideas.md`, `actions.md` and `decisions/`.
     - Create the chosen section folders.
   - **Light:** just `notes.md`: a one-paragraph summary (from the interview answers), a `Tags:` line (folder name plus aliases), then a `## Notes` list for dated bullets (prefixed `Decided:`, `Idea:`, `To do:` or `Open:` where it helps).
5. **Connect.** Add the area to the **Areas** section of `life/wiki/index.md` (rename an older `Businesses` section to Areas), one line with its folder and what it is, linking its overview (or `notes.md`). Link a business or investing area from `life/wiki/pillars/09-opportunities.md`; link `work/`, `study/`, and a business that is their main work from `07-career.md`. Do not copy any content between folders.
6. **Tell them how to use it** in one line: mention it (`#<folder>` or any of its aliases) when sharing something, and it'll be filed here.
