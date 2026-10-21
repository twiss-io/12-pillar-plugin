---
description: "Add a business (or upgrade an existing one) — a short interview, a recommended structure, built after you confirm"
argument-hint: "[business name]"
---

Add or upgrade a business: `$ARGUMENTS` (ask for the name if empty).

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/folder-design.md` and `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`. Needs a workspace (`life/wiki/index.md` exists). If there isn't one, offer `/12-pillars:setup`.

1. **New or existing?** The folder name is the kebab-cased business name.
   - If `businesses/<name>/` doesn't exist, it's a new business.
   - If it exists as **Light** (just `notes.md`), offer to upgrade it to Standard or Deep. Keep `notes.md` by moving it into the new `raw/` as a source, then build wiki pages from it.
   - If it's already Standard or Deep, offer to add sections instead. Never overwrite existing files.
2. **Interview.** Ask the questions in `folder-design.md` section 1, one at a time, using clickable options where the answer is a choice. Also ask what short names they'll actually use for it (aliases such as `#acme` for `acme-studio`).
3. **Recommend.** Show the proposed folder tree with the tier, the sections, and one line on why. Get one confirm and accept changes in plain language.
4. **Build.** This is the single spec for creating a business folder, and setup uses it too.
   - **Standard/Deep:**
     - Write `CLAUDE.md`: what it is, the user's role, tier, the sections and what goes in each, the routing tags (folder name plus aliases), and the boundary rule.
     - Create `raw/` and save the interview answers there as `YYYY-MM-DD-setup-interview.md` (the user's words verbatim in a Q&A layout, header `source: setup`).
     - Create `wiki/index.md` with sections: Overview, then one per chosen folder (Decisions last).
     - Create `wiki/log.md` with first entry `## [YYYY-MM-DD] setup | Business folder created`.
     - Write `wiki/overview.md` from what they told you, with standard frontmatter citing the interview file and a `## Sources` section.
     - Create the chosen section folders.
   - **Light:** just `notes.md`: a one-paragraph summary, a `Tags:` line (folder name plus aliases), then a `## Notes` list for dated bullets.
5. **Connect.** Add the business to the **Businesses** section of `life/wiki/index.md`, linking its overview (or `notes.md`). Link it from `life/wiki/pillars/09-opportunities.md`, and from `07-career.md` if it's their main work. Do not copy any content between folders.
6. **Tell them how to use it** in one line: mention the business (`#<name>` or any of its aliases) when sharing something, and it'll be filed here.
