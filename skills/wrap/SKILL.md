---
name: wrap
description: "End-of-session wrap-up: pull the decisions, ideas and actions out of a brainstorm or working session and file them where they belong"
---

> **Works in Claude Code and Codex.** Plugin folder: `${CLAUDE_PLUGIN_ROOT}`. If that shows a variable name rather than a real path, the plugin folder is two levels above this SKILL.md; plugin paths below resolve from it. If a dollar-sign ARGUMENTS placeholder shows up unreplaced, use what the user wrote when asking for this. **"Clickable options" means: if you have any tool for asking the user a question with choices, use it** (Claude Code: AskUserQuestion. Codex: request_user_input_async, or request_user_input in Plan mode. Other assistants: their ask-user or question tool). After asking, wait for the answer before going on; with an async tool, end your turn. **Pick-several questions with a one-choice tool** (Codex's lets the user click only one option): for up to 5 items, ask one Yes / No question per item, all in the same call; for more, group related items so there are at most 5 Yes / No questions (the skill groups them where it matters). Never collapse a pick-several question into one single-choice list of combinations. Only if you have no such tool, write a short numbered list, one option per line, and say they can reply with the number. **Limits:** Claude's tool takes 2–4 options per question and up to 4 questions per call, so split a longer list across questions in the same call (each saying other answers can be typed). **Naming skills to the user:** this text writes them as `/12-pillars:<name>` (Claude Code); in Codex, say `$12-pillars:<name>` instead.

Wrap up the working session in this conversation: `$ARGUMENTS` (an optional unit, pillar or topic to focus on. If empty, work out what the session was about).

Follow `${CLAUDE_PLUGIN_ROOT}/frameworks/llm-wiki.md` for formats. Needs a workspace (`index.md` and the pillar folders). If there isn't one, offer `/12-pillars:setup`.

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
- **Facts learned:** new information about a client, person, market, numbers, or the user themselves (stress, time, money, health).
- **Deliverables:** anything finished in the session (a proposal, plan, email, post): its final text is saved as is to `raw/YYYY-MM-DD-draft-<slug>.md` (`source: draft`) and linked from the page it concerns.

Drop dead ends and back-and-forth. If nothing was decided, say so rather than inventing a decision.

## 3 · Route
Each item goes to the pillar it belongs to, or to the unit inside it (match the unit's name or routing names in the Units section of `index.md`). A session can touch several pillars.
- Decisions: `decisions/YYYY-MM-DD-<slug>.md` in the unit or pillar folder, one page per real decision, each with decision, reasoning, alternatives rejected, date, and sources. Create `decisions/` if it's missing.
- Ideas: append to that unit's or pillar's `ideas.md` (created if missing).
- Actions: `actions.md` under `## Open actions` as `- [ ] <action> — <owner>, due YYYY-MM-DD #<pillar>` (the due part only if said).
- Open questions: `actions.md` under `## Open questions`, and the relevant pillar README's `## Open questions` when it's about the person's own life.
- Facts: update the matching page (a client in the unit's `clients/`, a person in `06-relationships/people/`, the user's own state in the pillar README it touches).

## 4 · Propose (one message)
Show the wrap as a compact card, then ask for one confirm:

```
Wrap-up: <session title>
✅ Decided: <decision> → <page>
💡 Ideas parked: <idea>, <idea> → <page>
📋 Actions: <action, owner, date> → actions.md
❓ Open: <question>
📝 Saved draft: <deliverable> → raw/…-draft-<slug>.md
🔗 Pillars: <which pillar READMEs get a link>
📄 Session note: raw/YYYY-MM-DD-session-<slug>.md
```

Accept corrections in plain language ("that wasn't decided, park it", "move the pricing bit to the other business", "that's for work, not the shop").

## 5 · File (after confirm)
1. **Session note:** save to `raw/YYYY-MM-DD-session-<slug>.md` with the header `source: session-summary`: a short summary of the discussion plus the user's key statements quoted verbatim. If the name is taken, add `-2`, `-3`, and so on. Save any deliverables as drafts.
2. Write the decision, idea and fact pages with standard frontmatter, citing the session note in `sources:` and `## Sources`, and add the actions.
3. Link from the relevant pillar READMEs. A README's "Where this stands" may say that a decision exists and link to it ("pricing decided, see link"), but never repeats its details.
4. Update `index.md` for new pages. Append `## [YYYY-MM-DD] wrap | <session title>` to `log.md`.

## 6 · Report
One line per page written. Then one line on where the next session picks up (for example, "Next session on Twiss starts from 2 open questions and 3 actions").
