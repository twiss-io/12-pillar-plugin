# Folder Design — recommending a structure that fits the person

> The workspace is shaped around what fills the person's days. A student gets a place for their studies, an employee a place for their job, a founder one folder per business, and someone between things just `life/`. Each folder is sized to how much information it actually produces: a side project doesn't need a full wiki; a business with clients, a team and a pipeline does.

Use this during `/12-pillars:setup` and `/12-pillars:add-business`. The goal is a structure the person will actually keep up, not the most complete one possible.

## 1. Start from what fills their days

Ask one multi-select question (clickable options): **"What fills your days right now?"**
Studying · Working a job · Running a business · Freelance, agency or client work · Creating content · Investing · Between things right now.

If your question tool only allows one choice (as in Codex), ask five Yes / No questions in the same call so any mix works: "Studying?" · "Working a job?" · "Running a business, freelance or client work?" · "Creating content?" · "Investing?". No to all means between things right now. Don't offer a single list of combinations instead.

With Claude's question tool (multi-select, at most 4 options per question), ask it as two questions in one call: "Work and study" (Studying · Working a job · Running a business · Freelance, agency or client work) and "Anything else?" (Creating content · Investing · Between things right now).

Each answer maps to an **area**: a folder next to `life/` that holds that part of their world.

| They chose | Area folder | Archetype (section 4) |
|---|---|---|
| Studying | `study/` | Student |
| Working a job | `work/` (two jobs at once: `work/<employer>/` each) | Employee |
| Running a business | `businesses/<name>/`, one per business | the closest business archetype |
| Freelance, agency or client work | `businesses/<name>/` for their practice | Agency / services or Consulting / coaching |
| Creating content | `businesses/<channel-or-brand>/` | Content / media / creator |
| Investing | `investing/` | Investing / holding |
| Between things right now | nothing yet; `life/` covers it (Career and Opportunities pillars) | — |

Mix and match freely: an employee with a side shop gets `work/` and `businesses/side-shop/`. Use the person's own words for folder names when they ask (`uni/` instead of `study/`, `job/` instead of `work/`); the area's `AGENTS.md` or `notes.md` and the Areas section of `life/wiki/index.md` record what each folder is, so any name works. Never create an area folder they didn't choose.

## 2. Interview each area

Ask question 5 (how often) first. If the answer is "occasionally", it's Light: ask only question 1 and its aliases, and skip the rest.

For a business, freelance practice, channel or investing area, ask these one at a time, with clickable options where the answer is a choice:

1. **What does it do, and for whom?** (one line)
2. **Your role:** founder / partner / freelancer / investor / advisor
3. **Stage:** idea · building · launched · growing · established · winding down
4. **What does it run on?** Pick all that apply: clients · customers (many, small) · products · projects · deals/sales pipeline · content · a team · suppliers/partners · physical locations · research. (With a one-choice tool, ask five Yes / No questions: "Clients or customers?" · "Products?" · "Projects, deals or a sales pipeline?" · "Content?" · "A team, suppliers, partners or locations?"; research-only areas say no to all.)
5. **How often will you add information?** daily · weekly · occasionally
6. **Do you need to look things up later** (past decisions, client history, what was promised), **or is it mostly a to-do list?**

For **study/**: what they study and where, the year or stage, what they're juggling (courses · projects/thesis · exams · internships/applications · a job alongside), and questions 5–6.

For **work/**: the employer and role in one line, how long they've been there, what the job runs on (projects · a team they lead · stakeholders · clients · targets/reviews), and questions 5–6.

In the quick start, skip the interview: every area starts **Light** and gets upgraded when it grows.

## 3. Choose the tier

| Tier | When | Structure |
|---|---|---|
| **Light** | Side project, idea stage, occasional notes, little history to look up | `<area>/notes.md`, a single running page of dated bullets, starting with a one-paragraph summary and a `Tags:` line (folder name plus aliases). No raw/wiki split. |
| **Standard** | Ongoing information, but one main area of activity | `AGENTS.md` (+ `CLAUDE.md` importing it), `raw/`, `wiki/` with `index.md`, `log.md`, `overview.md`, and one or two sections. |
| **Deep** | Several areas of activity (clients plus team plus product, for example) and a real need to look things up | Standard plus all the sections that match its archetype below. |

When unsure, go one tier lighter. An area can always be upgraded later (`/12-pillars:add-business <name>` on an existing light folder offers the upgrade). Unused empty folders get ignored and become clutter.

## 4. Sections by archetype

Pick the archetype closest to the area, then keep only the sections it actually runs on (from the interview). Mixed areas can combine sections.

| Archetype | Suggested `wiki/` sections |
|---|---|
| Student | `courses/` (one page per course or module) · `projects/` (assignments, thesis) · `exams/` · `career/` (internships, applications) |
| Employee (working for someone else) | `role/` (responsibilities, goals, reviews) · `projects/` · `people/` (colleagues, stakeholders) · `wins/` |
| Agency / services | `clients/` · `projects/` · `proposals/` · `team/` |
| Consulting / coaching | `clients/` · `engagements/` · `frameworks/` (their own methods) · `content/` |
| SaaS / software product | `product/` (features, roadmap, decisions) · `customers/` · `metrics/` · `team/` |
| E-commerce / consumer brand | `products/` · `suppliers/` · `campaigns/` · `customers/` (segments, not individuals) |
| F&B / retail / physical | `outlets/` · `menu/` or `skus/` · `suppliers/` · `staff/` · `operations/` |
| Content / media / creator | `content/` (pieces and series) · `audience/` · `sponsors/` · `ideas/` |
| Investing / holding | `portfolio/` (one page per holding) · `deals/` · `theses/` |
| Deal-driven (sales, real estate, brokerage) | `deals/` (one page per deal: budget, decision-maker, need, timeline, status) · `contacts/` · `listings/` or `offers/` |
| Research / early-stage idea | `research/` · `experiments/` · `decisions/` |

Sections that apply to almost every area: `decisions/` (what was decided, when, why), and `meetings/` if it has many of them.

## 5. Write the area schema

Each Standard or Deep area gets its own `AGENTS.md` (with a one-line `CLAUDE.md`: `@AGENTS.md`, so Claude Code reads it too) holding:
- what the area is, in one line, and the person's role
- its tier and chosen sections, and what goes in each
- the tags that route captures here: the folder name (for example `#acme-studio`, `#study`) plus any short aliases the person will actually type (`#acme`, `#uni`)
- the boundary rule: content stays in this folder. Nothing from the personal `life/` folder is copied in. Nothing from here is copied into other areas.

## 6. Show it before building it

Always render the proposed tree for the whole workspace before creating anything, with a one-line reason per area ("Light — studies, notes for now" · "Deep — agency: clients and projects, weekly updates"). Ask for one confirm. Accept changes in plain language ("call it uni", "drop investing", "make App Lab light", "add a team section"). Only then create the folders and files.

Examples:

```
student/
├── AGENTS.md
├── life/              raw/ + wiki/ — your 12 pillars
└── study/             LIGHT — notes.md: courses, exams, internship hunt

employee-with-a-side-shop/
├── AGENTS.md
├── life/
├── work/              STANDARD — role/ projects/ people/ wins/
└── businesses/
    └── side-shop/     LIGHT — notes.md only, occasional updates

agency-owner/
├── AGENTS.md
├── life/
└── businesses/
    ├── acme-studio/   DEEP — agency: clients/ projects/ proposals/ team/ decisions/
    └── app-lab/       STANDARD — product studio: product/ decisions/
```
