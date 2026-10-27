---
name: wrap
description: "End-of-session wrap-up: pull the decisions, ideas and actions out of a brainstorm or working session and file them where they belong"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, offer the common combinations as options (the skill lists them where it matters) and say any other mix can be typed in the text box. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Wrap up the working session in this conversation: `$ARGUMENTS` (an optional area, such as a business, `work` or `study`, or a topic to focus on. If empty, work out what the session was about).

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md` for formats and boundaries. Needs a workspace (`life/wiki/index.md`). If there isn't one, offer `/12-pillars:setup`.

## Why this exists
Brainstorms and planning sessions aren't filed message by message, because most of what's said is exploration. What's worth keeping is the **outcome**. Wrap turns a session into a few durable pages so the next session starts from what was decided, not from zero.

## 1 · Scope
Cover the conversation since the last **wrap** in this session, or since the start. Captures made during the session don't reset the scope. List those items as "already filed" and skip them, so nothing is filed twice. If the context was compacted during the session, say so: you're working from the summary, so ask the user to add anything important that may have been lost.

## 2 · Extract
Pull out only what's worth keeping:
- **Decisions:** what was decided, why, and what was rejected. These are the most valuable part.
- **Ideas parked:** ideas worth revisiting, each with one line on why.
- **Actions:** what needs doing, by whom, and by when if it was said.
- **Open questions:** things raised but not resolved.
- **Facts learned:** new information about a client, person, market or numbers.
- **Personal parts:** anything about the user's own life (stress, time, money, health) goes to `life/`, not to the business, job or studies.

Drop dead ends and back-and-forth. If nothing was decided, say so rather than inventing a decision.

## 3 · Route
Work out where each item belongs: which area folder (a business, `study/`, `work/`, `investing/`: match the folder name or the aliases in its `AGENTS.md` or `notes.md`), or `life/`. A session can touch several. Split items and keep boundaries: personal content never goes into an area folder, and areas never get each other's content.

Destinations inside a **Standard or Deep area**:
- Decisions: `wiki/decisions/YYYY-MM-DD-<slug>.md`, one page per real decision, each with decision, reasoning, alternatives rejected, date, and sources. Create `decisions/` if it's missing and add a Decisions section to the index.
- Ideas: append to `wiki/ideas.md`.
- Actions: append to `wiki/actions.md` under `## Open actions` as `- [ ] <action> — <owner>, <due date if said>`.
- Open questions: append to `wiki/actions.md` under `## Open questions`.
- Facts: update the matching section page (a client in `clients/`, a product in `product/`, and so on).
- If `ideas.md` or `actions.md` is missing (an older folder), create it and link it from `overview.md`.

**Light area:** dated bullets in the `## Notes` list of its `notes.md`, each prefixed `Decided:`, `Idea:`, `To do:` or `Open:`.
**Personal (`life/`):** decisions and ideas go in `topics/`, and open questions go in the relevant pillar hub's `## Open questions`. Updates go to the relevant pillar hubs and people pages, as a normal capture would.

## 4 · Propose (one message)
Show the wrap as a compact card, then ask for one confirm:

```
Wrap-up: <session title>
✅ Decided: <decision> → <page>
💡 Ideas parked: <idea>, <idea> → <page>
📋 Actions: <action, owner, date> → <page>
❓ Open: <question>
🔗 Pillars: <which life pillar hubs get a link>
📄 Session note saved to: <folder>/raw/YYYY-MM-DD-session-<slug>.md
```

Accept corrections in plain language ("that wasn't decided, park it", "move the pricing bit to the other business", "that's for work, not the shop").

## 5 · File (after confirm)
1. **Session note:** save to each Standard/Deep destination's `raw/` with the header `source: session-summary`. Contents: a short summary of the discussion plus the user's key statements quoted verbatim, and an area's note holds only that area's part. Names: `YYYY-MM-DD-session-<slug>.md` in an area, and `YYYY-MM-DD-session-<slug>-personal.md` in `life/raw/`. If the name is taken, add `-2`, `-3`, and so on. A Light area gets no session note; its bullets are the record.
2. Write the decision, idea, action and fact pages with standard frontmatter, citing the session note in `sources:` and `## Sources`.
3. Link from the relevant life pillar hubs (usually Opportunities, Finance, Career). Links only: a hub's "Where this stands" may say that a decision exists and link to it ("pricing decided, see link"), but never repeats business details.
4. Update each touched `index.md`. Append `## [YYYY-MM-DD] wrap | <session title>` to each touched area `log.md`, and to `life/wiki/log.md` for anything filed in `life/` or in a Light area.

## 6 · Report
One line per page written. Then one line on where the next session picks up (for example, "Next session on this area starts from 2 open questions and 3 actions").
