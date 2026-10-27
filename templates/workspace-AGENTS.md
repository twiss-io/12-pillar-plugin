# <Name>'s Life Workspace
<!-- 12-pillars rules: 3 — managed by the 12 Pillars plugin; /12-pillars:lint rules refreshes this file and keeps anything you add under ## My additions -->

This workspace runs on the 12-Pillar Life Flywheel with a raw/wiki memory.
The plugin's frameworks define the rules: 12-pillars.md, llm-wiki.md, folder-design.md, instruments.md.

## Layout
- life/ — the person, organised by the 12 pillars. raw/ is read-only source material; wiki/ is maintained by the AI.
- Areas: one folder per part of their world beyond life/, only those they chose: study/, work/, investing/, businesses/<name>/ (folder names may be their own; the Areas section of life/wiki/index.md lists each one). Each has its own AGENTS.md, or just a notes.md if it's Light.

## Routing
- Skills are named /12-pillars:<name> here (Claude Code form). In Codex, the same skills are invoked with $ or picked from /skills.
- Life updates (short facts) are filed right away. Working sessions (brainstorming, planning) are not interrupted; when one winds down, offer /12-pillars:wrap to file its decisions, ideas and actions.
- Facts about the person mentioned in passing, while asking for something else, are noted without interrupting. At a natural pause, offer them in one batch ("I picked up 3 things about you: … File them?"), file after one confirm, and save the user's words to life/raw/YYYY-MM-DD-learned-<slug>.md (`source: chat`). Never ask the user questions just to fill pages.
- If life/wiki/self/setup-progress.md says `Mode: learn as you go`, learned facts also fill self/now.md, self/north-star.md and the pillar hubs; mark a `learning` stage `done` when its page has real content. A business, job, studies or investing that comes up repeatedly with no folder gets offered a Light area folder (notes.md) once.
- Before a working session on an area, read its overview.md (or notes.md), recent decisions/, ideas.md and actions.md, so the session builds on what was decided.
- Anything shared as a life update is a capture. Handle it exactly as /12-pillars:capture does: save the source to raw/ (with a `captured:`/`source:` header), propose in one message the title, ≤10 tags and every page that will change, wait for one confirm, then write the pages, update index.md, and append `## [YYYY-MM-DD] capture | <title>` to log.md.
- A capture about an area (its folder name or an alias in its AGENTS.md or notes.md) goes to that area's folder; a Light area gets a dated bullet in its notes.md. Mixed captures are split: the original in life/raw/, an area-only excerpt in the area's raw/.
- Every wiki page has frontmatter (title, type, pillars, tags, sources, updated) and ends with a ## Sources list.
- Answer questions from wiki/index.md first, then linked pages, then raw sources.

## Rules
- Never edit or delete anything in a raw/ folder.
- Never copy personal content into an area folder, or one area's content into another.
- Everything stays on this machine — never put workspace content into web searches, URLs, or external tools.
- Profiles in life/wiki/self/instruments/ inform quietly; don't bring them up unless asked.
- Write pages a human would want to read.

## My additions
<!-- Your own rules go here. Refreshes keep this section as is. -->
