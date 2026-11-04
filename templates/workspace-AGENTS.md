# <Name>'s Life Workspace
<!-- 12-pillars rules: 12 — managed by the 12 Pillars plugin; /12-pillars:lint rules refreshes this file and keeps anything you add under ## My additions -->

This workspace is <Name>'s second brain, organised as the 12-Pillar Life Flywheel.
The plugin's frameworks define the rules: 12-pillars.md (with pillar-playbook.md for each pillar's full method), llm-wiki.md, folder-design.md, instruments.md.

## Layout
- 01-faith/ … 12-legacy/ — one folder per pillar; together they hold everything. Each has a README.md (where the pillar stands) and its own AGENTS.md.
- Units live inside their pillar: studies in 05-development/<school>/, the job in 07-career/<employer>/, businesses in 09-opportunities/<name>/, investing in 10-finance/investing/. Posts live in 08-brand/. The Units section of index.md lists each unit and the names that route to it.
- raw/ — every source, read-only. index.md (catalog), log.md (history), actions.md (every to-do and deadline).

## Routing
- Skills are named /12-pillars:<name> here (Claude Code form): setup, wrap, pillars, lint. In Codex, the same skills are invoked with $ or picked from /skills. Filing and answering need no skill.
- What's worth keeping about the person's life (people, deadlines, decisions, numbers, events, goals, changes, files they send; not small talk, passing moods, their questions or task help; when borderline, skip it) is filed straight away, without asking first, as llm-wiki.md section 4 "Filing" describes: save the source once to raw/ (with a `captured:`/`source:` header), write the pages in every pillar it touches, update index.md, append `## [YYYY-MM-DD] capture | <title>` to log.md, then report in one or two plain lines what was saved where. The user corrects in plain words; "undo" reverses the last filing.
- Working sessions (brainstorming, planning) are not interrupted. When one winds down, run /12-pillars:wrap to file its decisions, ideas and actions, then show what was filed.
- Facts about the person mentioned in passing, while asking for something else, aren't filed mid-task. At a natural pause, file them (the user's words to raw/YYYY-MM-DD-learned-<slug>.md, `source: chat`) and say so in one line. Never ask the user questions just to fill pages.
- If setup-progress.md says `Mode: learn as you go`, filing also fills 02-identity/now.md, 02-identity/north-star.md and the pillar READMEs; mark a `learning` stage `done` when its page has real content.
- Facts about a unit (its name or one of its routing names in index.md) go into that unit; the pillar's README gets a link. Route by what the item is, with names as hints: a published post goes to 08-brand/posts/ even when it mentions a client. A new job, school, business or investing that is clearly theirs gets its unit when filed (folder-design.md section 6).
- Deadlines, to-dos and reminders go in actions.md as `- [ ] <what> — due YYYY-MM-DD #<pillar>` (a reminder at a set time: `due YYYY-MM-DD HH:MM`); tick them off (`- [x]`) when something shows they're done. When a task produces a finished piece the user is actually using (a proposal, plan, email or post they're sending), save its final text to raw/YYYY-MM-DD-draft-<slug>.md.
- Before a working session or a task on a unit or pillar (a draft, a message, a plan), read its overview.md or README.md, recent decisions/, ideas.md, its lines in actions.md, and the page of each person or client involved.
- Every page has frontmatter (title, type, pillars, tags, sources, updated) and ends with a ## Sources list.
- Answer questions from index.md first, then linked pages, then raw sources, with links to the pages used.

## Rules
- Never edit or delete anything in raw/.
- A fact lives on one page; other pillars link to it, never copy it.
- Everything stays on this machine — never put workspace content into web searches, URLs, or external tools.
- Profiles in 02-identity/instruments/ inform quietly; don't bring them up unless asked.
- Write pages a human would want to read.
- Never quote these rules or a skill's instructions to the user; act on them, or ask in plain words.
- When offering the user a choice, use your ask-user/question tool if you have one (AskUserQuestion in Claude Code, request_user_input_async in Codex, the equivalent elsewhere) so they can click; otherwise a short numbered list they can answer by number.

## My additions
<!-- Your own rules go here. Refreshes keep this section as is. -->
