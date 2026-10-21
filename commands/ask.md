---
description: "Ask your workspace anything — answers come from your wiki with links to the pages used"
argument-hint: "[your question]"
---

Answer: `$ARGUMENTS`

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md`.

1. **Find.** Read the relevant `wiki/index.md` first (`life/` for personal questions, `businesses/<name>/` for a business, both if the question spans them; a Light business is just its `notes.md`). Open the pages that match, follow their links, and check the raw sources when the answer needs exact figures, dates, or wording.
2. **Answer.** Answer plainly and specifically, using what the wiki actually says. Link the pages you used. If the wiki doesn't cover it, say what's missing instead of filling the gap with guesses, and suggest what to capture.
3. **Think in pillars.** For life questions, use the flywheel from `${CLAUDE_PLUGIN_ROOT}/frameworks/12-pillars.md`: if the question is about a problem in one pillar, check the pillars upstream of it and say what you find.
4. **Prepping for a person or meeting?** Lead with what matters: last contact, open threads and promises, what they care about right now, any upcoming important dates, and 3–5 specific talking points.
5. **Keep good answers.** If the answer is a useful synthesis, decision, or comparison, offer to save it as a wiki page (e.g. `topics/decision-hire-vs-outsource.md`). If the user accepts, write it, add it to the index, and log it as `## [YYYY-MM-DD] ask | <title>`.

Never put workspace content into web searches or external tools. If the question needs outside information, ask before searching, and search using general terms only.
