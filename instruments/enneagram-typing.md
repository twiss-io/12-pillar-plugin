# Enneagram Typing Protocol

A structured typing conversation used by `/12-pillars:setup`. To retype later, the user reruns setup and asks to redo the profile, so the skill supplies this file's path. Grounded in standard public Enneagram theory (nine types, three centers, core fear/desire, stress behavior). ~5 minutes.

**Posture:** a type is a working hypothesis, never a verdict. Self-report drifts; record the result with a date and a confidence level, and expect reassessment. If the user already knows their type, take dictation and (optionally) run Round 2 as a light confirmation.

**Mechanics:** use clickable options for every round (a choice tool such as AskUserQuestion if available, otherwise a numbered list) — these are choice-shaped questions. Let the user add nuance in free text via "Other" whenever they want.

## Round 1 — find the center (3 triad questions)

Ask all three; note which single statement in each triad lands hardest (and which triad the user answers fastest — speed is signal).

**Q1 · The gut triad (8 / 9 / 1) — "Under pressure, which is most you?"**
- A. I push back — control the situation before it controls me. *(→ 8)*
- B. I keep the peace — merge, defuse, don't rock the boat. *(→ 9)*
- C. I fix what's wrong — there is a right way and it matters. *(→ 1)*
- D. None of these really lands.

**Q2 · The heart triad (2 / 3 / 4) — "What do you most want people to see?"**
- A. That I'm there for them — needed, generous, indispensable. *(→ 2)*
- B. That I deliver — successful, effective, worth admiring. *(→ 3)*
- C. That I'm not like everyone else — deep, authentic, particular. *(→ 4)*
- D. None of these really lands.

**Q3 · The head triad (5 / 6 / 7) — "What's your relationship with uncertainty?"**
- A. I retreat and study it — understand before engaging, protect my energy. *(→ 5)*
- B. I scan for what could go wrong — loyalty and preparation are safety. *(→ 6)*
- C. I outrun it — keep options open, next thing, keep it positive. *(→ 7)*
- D. None of these really lands.

**Scoring:** the dominant center is usually where the answer came fastest and hardest. Take the strongest 2–3 candidate types into Round 2.

## Round 2 — discriminate within the shortlist (core fear / desire / stress)

For each candidate type, test its core pattern. Ask 2–3 of these as choice questions, pitting the shortlisted types' versions against each other:

| Type | Core fear | Core desire | Under stress, becomes |
|---|---|---|---|
| 1 | Being corrupt, wrong | Integrity | Critical, resentful (→ moody like 4) |
| 2 | Being unwanted | Being loved | Intrusive, martyr-ish (→ aggressive like 8) |
| 3 | Being worthless without achievement | Feeling valuable | Image-managing, burnt out (→ disengaged like 9) |
| 4 | Having no identity | Being uniquely oneself | Envious, withdrawn (→ clingy like 2) |
| 5 | Being depleted, incompetent | Competence, self-sufficiency | Hoarding time/energy (→ scattered like 7) |
| 6 | Being without support | Security | Suspicious, testing loyalty (→ competitive like 3) |
| 7 | Being trapped in pain | Freedom, satisfaction | Escapist, scattered (→ critical like 1) |
| 8 | Being controlled | Self-determination | Domineering (→ withdrawn like 5) |
| 9 | Conflict, disconnection | Peace | Stubbornly passive (→ anxious like 6) |

Example discriminator (shortlist 3 vs 8): *"Which is worse: being seen as a failure, or being at someone else's mercy?"*

## Round 3 — confirm and wing

1. **Stress check:** describe the shortlist leader's stress movement in plain words and ask "does that happen to you?" A recognized stress pattern is the strongest confirmation available.
2. **Wing:** ask which neighbor flavors them (e.g. for a 3: "more diplomatic and steady (3w2-ish)... or more driven and image-precise (3w4-ish)?"). Record as `XwY` only if it's clear; a bare type is fine.

## Record format (write to `life/wiki/self/instruments/enneagram.md`)

```markdown
---
title: Personality type (Enneagram)
type: self
pillars: [identity]
tags: ["#enneagram"]
sources: [../../../raw/2026-07-18-setup-profiles.md]
updated: 2026-07-18
---
# Enneagram
- Working hypothesis: Type 3 (w4 unclear) — confidence: medium
- Typed: 2026-07-18, via the typing protocol (self-report)
- Signals: fastest triad = heart; core fear resonance = "worthless without achievement";
  stress pattern (disengage like 9) recognized immediately
- Reassess: yearly, or when a major season changes

## Sources
- [Setup answers, profiles stage](../../../raw/2026-07-18-setup-profiles.md)
```

**Rules:** never present the result as fact — it's a lens; never type someone from third-party descriptions; if two types stay tied after Round 3, record both and move on — daily captures will disambiguate over time.
