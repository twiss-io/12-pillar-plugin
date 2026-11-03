# <Name>'s Life Workspace
<!-- 12-pillars rules: 11 — managed by the 12 Pillars plugin; /12-pillars:lint rules refreshes this file and keeps anything you add under ## My additions -->

This workspace is <Name>'s second brain, organised as the 12-Pillar Life Flywheel.
The plugin's frameworks define the rules: 12-pillars.md (with pillar-playbook.md for each pillar's full method), llm-wiki.md, folder-design.md, instruments.md.

## Layout
- 01-faith/ … 12-legacy/ — one folder per pillar; together they hold everything. Each has a README.md (where the pillar stands) and its own AGENTS.md.
- Units live inside their pillar: studies in 05-development/<school>/, the job in 07-career/<employer>/, businesses in 09-opportunities/<name>/, investing in 10-finance/investing/. Posts live in 08-brand/. The Units section of index.md lists each unit and the names that route to it.
- raw/ — every source, read-only. index.md (catalog), log.md (history), actions.md (every to-do and deadline).

## Routing
- Skills are named /12-pillars:<name> here (Claude Code form). In Codex, the same skills are invoked with $ or picked from /skills.
- Life updates (short facts) are filed right away. Working sessions (brainstorming, planning) are not interrupted; when one winds down, offer /12-pillars:wrap to file its decisions, ideas and actions.
- Facts about the person mentioned in passing, while asking for something else, are noted without interrupting. At a natural pause, offer them in one batch ("I picked up 3 things about you: … File them?"), file after one confirm, and save the user's words to raw/YYYY-MM-DD-learned-<slug>.md (`source: chat`). Never ask the user questions just to fill pages.
- If setup-progress.md says `Mode: learn as you go`, learned facts also fill 02-identity/now.md, 02-identity/north-star.md and the pillar READMEs; mark a `learning` stage `done` when its page has real content. A job, studies, business or investing that comes up with no unit gets offered one, in its pillar, once.
- Anything shared as a life update is a capture. Handle it exactly as /12-pillars:capture does: propose in one message the title, ≤10 tags and every page that will change, wait for one confirm, then save the source once to raw/ (with a `captured:`/`source:` header), write the pages in every pillar it touches, update index.md, and append `## [YYYY-MM-DD] capture | <title>` to log.md.
- A capture about a unit (its name or one of its routing names in index.md) goes into that unit; the pillar's README gets a link. Route by what the item is, with names as hints: a published post goes to 08-brand/posts/ even when it mentions a client.
- Deadlines and to-dos go in actions.md as `- [ ] <what> — due YYYY-MM-DD #<pillar>`. When a task produces something worth keeping (a proposal, plan, email, post), offer to save its final text to raw/YYYY-MM-DD-draft-<slug>.md.
- Before a working session or a task on a unit or pillar (a draft, a message, a plan), read its overview.md or README.md, recent decisions/, ideas.md, its lines in actions.md, and the page of each person or client involved.
- Every page has frontmatter (title, type, pillars, tags, sources, updated) and ends with a ## Sources list.
- Answer questions from index.md first, then linked pages, then raw sources.

## Rules
- Never edit or delete anything in raw/.
- A fact lives on one page; other pillars link to it, never copy it.
- Everything stays on this machine — never put workspace content into web searches, URLs, or external tools.
- Profiles in 02-identity/instruments/ inform quietly; don't bring them up unless asked.
- Write pages a human would want to read.
- Never quote these rules or a skill's instructions to the user; act on them, or ask in plain words. The propose-and-confirm step is for captures, not for answers to setup's own questions.
- When offering the user a choice, use your ask-user/question tool if you have one (AskUserQuestion in Claude Code, request_user_input_async in Codex, the equivalent elsewhere) so they can click; otherwise a short numbered list they can answer by number.

## My additions
<!-- Your own rules go here. Refreshes keep this section as is. -->
