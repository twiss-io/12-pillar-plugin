---
name: add-business
description: "Add a business, your job, your studies or investing as its own folder (or upgrade one) — a short interview, a recommended structure, built after you confirm"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Add or upgrade an area: `$ARGUMENTS`. An area is a business, freelance practice or channel (`businesses/<name>/`), their studies (`study/`), their job (`work/`), their own content and personal brand (`content/`), or investing (`investing/`). If empty, ask which, as clickable options; for a business, ask its name.

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md` and `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. Needs a workspace (`life/wiki/index.md` exists). If there isn't one, offer `/12-pillars:setup`.

1. **New or existing?** The folder is `study/`, `work/`, `content/` or `investing/` (or the name the user prefers for it), or `businesses/<kebab-cased name>/` for a business. Check the Areas section of `life/wiki/index.md` (older workspaces: Businesses) for folders already in use.
   - If the folder doesn't exist, it's a new area.
   - If it exists as an **older notes-only area** (just `notes.md`, from plugin versions before 0.5.8), offer to give it the full structure: build it as step 4 describes, move `notes.md` into the new `raw/` as a source, and file its bullets into the wiki.
   - If it already has `raw/` and `wiki/`, offer to add sections instead (that is how Light becomes Standard or Deep). Never overwrite existing files.
2. **Interview.** Ask the questions for this kind of area in `folder-design.md` section 2, one at a time, using clickable options where the answer is a choice. Also ask what short names they'll actually use for it (aliases such as `#acme` for `acme-studio`). Never use a pillar tag (`#brand`, `#health`, …) as an alias.
3. **Recommend.** Show the proposed folder tree in the short style of setup's example (no tier labels or plumbing files), then one line on why. Get one confirm and accept changes in plain language.
4. **Build.** This is the single spec for creating an area folder, and setup uses it too.
   - **Every tier** gets the same core structure; tiers differ only in how many section folders it has (none for Light, a few for Standard (only those it already has things for), all that fit for Deep):
     - Write `AGENTS.md` (plus a `CLAUDE.md` containing only `@AGENTS.md`): what it is, the user's role, tier, the sections and what goes in each, the routing tags (folder name plus aliases), and the boundary rule.
     - Create `raw/` and save the interview answers there as `YYYY-MM-DD-setup-interview.md` (the user's words verbatim in a Q&A layout, header `source: setup`).
     - Create `wiki/index.md` with sections: Overview (lines for overview, ideas, actions), one per chosen folder, then Decisions.
     - Create `wiki/ideas.md` (parked ideas) and `wiki/actions.md` (sections `## Open actions` and `## Open questions`), both with standard frontmatter.
     - Always create `wiki/decisions/`, even if it wasn't one of the chosen sections.
     - Create `wiki/log.md` with first entry `## [YYYY-MM-DD] setup | Area folder created`.
     - Write `wiki/overview.md` from what they told you, with standard frontmatter citing the interview file and a `## Sources` section. It links to `ideas.md`, `actions.md` and `decisions/`.
     - Create the chosen section folders (none for Light).
5. **Connect.** Add the area to the **Areas** section of `life/wiki/index.md` (rename an older `Businesses` section to Areas), one line with its folder and what it is, linking its overview. Link a business or investing area from `life/wiki/pillars/09-opportunities.md`; link `work/`, `study/`, and a business that is their main work from `07-career.md`; link `content/` from `08-brand.md`. Do not copy any content between folders.
6. **Tell them how to use it** in one line: mention it (`#<folder>` or any of its aliases) when sharing something, and it'll be filed here.
