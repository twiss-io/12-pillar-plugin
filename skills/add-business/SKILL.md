---
name: add-business
description: "Add a unit inside its pillar: your studies, your job, a business or your investing, with sections that fit; or grow an existing one"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Add or grow a unit: `$ARGUMENTS`. A unit is a part of their world with its own stream of information, inside the pillar it belongs to: their studies (`05-development/<school>/`), their job (`07-career/<employer>/`), a business, freelance practice or channel (`09-opportunities/<name>/`), or investing (`10-finance/investing/`). Their own posts and personal brand need no unit: they live in `08-brand/`. If empty, ask which, as clickable options, and its name.

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md` and `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. Needs a workspace (`index.md` and the pillar folders). If there isn't one, offer `/12-pillars:setup`.

1. **New or existing?** Check the Units section of `index.md`.
   - Not there: it's a new unit, named in kebab case from what they call it (`nus`, `twiss`, `kopi-kode`).
   - Already there: offer to add sections instead (or to archive it, if it has ended). Never overwrite existing files.
2. **A few questions,** one at a time, with clickable options where the answer is a choice: what it is in one line, their role, what it runs on (clients · customers · products · projects · courses · exams · deals · a team · holdings), and the names they'll actually type for it (the unit, its clients, projects or school). Never use a pillar tag (`#brand`, `#health`, …) as a routing name.
3. **Recommend.** Show where it goes and its sections in the short style of `folder-design.md` section 4, then one line on why. Get one confirm and accept changes in plain language.
4. **Build.** This is the single spec for creating a unit, and setup uses it too.
   - Save their answers to `raw/YYYY-MM-DD-unit-<name>.md` (the user's words verbatim in a Q&A layout, header `source: setup`), unless setup already saved them.
   - Write `overview.md` with standard frontmatter: what it is, their role, the stage or current state, a `**Names:**` line with the routing names, and links to its sections. It cites the raw file in `sources:` and `## Sources`.
   - Name its sections in the overview, but create each section folder (and `ideas.md`, `decisions/`) only when its first page goes in, so no empty folders are left lying around.
   - People it involves (colleagues, managers, client contacts) get pages in `06-relationships/people/` with their role and a link to this overview, never pages inside the unit.
5. **Connect.** Add one line to the Units section of `index.md`: folder, what it is, `names: …`. Link it from its pillar's README under `## Linked pages`, and from `09-opportunities/README.md` too when it makes money (a business, investing). Log `## [YYYY-MM-DD] setup | Unit <name> created` in `log.md`.
6. **Tell them how to use it** in one line: mention it by any of its names when sharing something, and it'll be filed there.
