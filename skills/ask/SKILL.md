---
name: ask
description: "Ask your workspace anything — answers come from your wiki with links to the pages used"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, offer the common combinations as options (the skill lists them where it matters) and say any other mix can be typed in the text box. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Answer: `$ARGUMENTS`

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`.

1. **Find.** Read the relevant `wiki/index.md` first (`life/` for personal questions, the area's folder for a business, job, studies or investing, both if the question spans them; a Light area is just its `notes.md`). Open the pages that match, follow their links, and check the raw sources when the answer needs exact figures, dates, or wording.
2. **Answer.** Answer plainly and specifically, using what the wiki actually says. Link the pages you used. If the wiki doesn't cover it, say what's missing instead of filling the gap with guesses, and suggest what to capture.
3. **Think in pillars.** For life questions, use the flywheel from `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`: if the question is about a problem in one pillar, check the pillars upstream of it and say what you find.
4. **Prepping for a person or meeting?** Lead with what matters: last contact, open threads and promises, what they care about right now, any upcoming important dates, and 3–5 specific talking points.
5. **Keep good answers.** If the answer is a useful synthesis, decision, or comparison, offer to save it as a wiki page (e.g. `topics/decision-hire-vs-outsource.md`). If the user accepts, write it, add it to the index, and log it as `## [YYYY-MM-DD] ask | <title>`.

Never put workspace content into web searches or external tools. If the question needs outside information, ask before searching, and search using general terms only.
