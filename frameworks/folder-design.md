# Folder Design — recommending a structure that fits the person

> The workspace is shaped around what fills the person's days. A student gets a place for their studies, an employee a place for their job, a founder one folder per business, and someone between things just `life/`. Each folder is sized to how much information it actually produces: a side project doesn't need a full wiki; a business with clients, a team and a pipeline does.

Use this during `/12-pillars:setup` and `/12-pillars:add-business`. The goal is a structure the person will actually keep up, not the most complete one possible.

## 1. Start from what fills their days

Ask one **open question** in plain text (no buttons): **"In a sentence or two, what fills your days right now? Studies, a job, businesses you run, clients, content, investing, anything goes."** Show one example answer so they know the level of detail: "I'm in my final year of uni, intern three days a week, and run a small design agency on the side with a friend."

Read the answer for every part of their world, including ones they mention in passing ("and I post on YouTube" is a content area). Pick up names (the business, the employer, the school) so folders can use them. If something is unclear, ask one short follow-up, then propose. Always ask it when it's unclear whether they **own** a business or **work for** one ("I work full time in an agency" could be either): "Is the agency yours (or part yours), or are you employed there?" Owner or partner → `businesses/<name>/`; employee → `work/`. Don't run through a checklist of roles they didn't mention.

Each part of their world maps to an **area**: a folder next to `life/` that holds that part of their world.

| They mentioned | Area folder | Archetype (section 4) |
|---|---|---|
| Studying | `study/` | Student |
| Working a job | `work/` (two jobs at once: `work/<employer>/` each) | Employee |
| Running a business | `businesses/<name>/`, one per business | the closest business archetype |
| Freelance, agency or client work | `businesses/<name>/` for their practice | Agency / services or Consulting / coaching |
| Creating content as a channel or media business | `businesses/<channel-or-brand>/` | Content / media / creator |
| Building their own personal brand or posting their own content | `content/` (ideas, drafts, what was posted, what worked); who they want to be known for stays in `life/` on the Brand pillar (8) | Content / media / creator |
| Investing | `investing/` | Investing / holding |
| Between things right now | nothing yet; `life/` covers it (Career and Opportunities pillars) | — |

Mix and match freely: an employee with a side shop gets `work/` and `businesses/side-shop/`; a final-year student who also runs an agency and wants to build a personal brand gets `study/`, `businesses/<agency>/` and `content/`. Use the person's own words for folder names when they ask (`uni/` instead of `study/`, `job/` instead of `work/`); the area's `AGENTS.md` or `notes.md` and the Areas section of `life/wiki/index.md` record what each folder is, so any name works. Never create an area folder for something they didn't mention.

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

In the quick start, skip the interview and choose the tier from what they already said (section 3).

## 3. Choose the tier

Every area has the same core structure, whatever its tier: `AGENTS.md` (+ `CLAUDE.md` importing it), `raw/`, and `wiki/` with `index.md`, `log.md`, `overview.md`, `ideas.md`, `actions.md` and `decisions/`. The tier only decides how many section folders it gets.

| Tier | When | Sections |
|---|---|---|
| **Light** | Side project, idea stage, occasional notes, little history to look up | None yet: the core only. |
| **Standard** | Ongoing information, but one main area of activity | A few sections, only those it already has things for. |
| **Deep** | Several areas of activity (clients plus team plus product, for example) and a real need to look things up | All the sections that match its archetype below. |

**Tier from a quick-start answer** (no interview): make an area **Standard** when the answer already shows things they'll need to look up later: named clients, customers or partners; a team; several live deliverables or deadlines (exams, projects, presentations); or it's full time. Give it the sections those things need, from section 4 (for example an agency with named clients: `clients/` `projects/`; a final-year student with exams and projects: `courses/` `projects/` `exams/`). Make it **Light** when it's mentioned in passing, is a side interest, or is something they only *want* to start. Each named client or partner gets its own page under `clients/` once something is captured about it, not empty pages up front.

When unsure, go one tier lighter. An area can always grow later (`/12-pillars:add-business <name>` on an existing area offers to add sections). Unused empty section folders get ignored and become clutter.

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

Every area gets its own `AGENTS.md` (with a one-line `CLAUDE.md`: `@AGENTS.md`, so Claude Code reads it too) holding:
- what the area is, in one line, and the person's role
- its tier and chosen sections, and what goes in each
- the tags that route captures here: the folder name (for example `#acme-studio`, `#study`) plus any short aliases the person will actually type (`#acme`, `#uni`)
- the boundary rule: content stays in this folder. Nothing from the personal `life/` folder is copied in. Nothing from here is copied into other areas.

## 6. Show it before building it

Always show the proposed tree for the whole workspace before creating anything, in the short style of the quick-start example in the setup skill: one line per area in the person's own words, its section folders with the names they gave, no plumbing files or tier labels, and one sentence saying every folder also gets raw/ and wiki/. Ask for one confirm. Accept changes in plain language ("call it uni", "drop investing", "make App Lab light", "add a team section"). Only then create the folders and files.

Examples of what gets built (the tier labels are for you, not for the proposal):

```
student/
├── AGENTS.md
├── life/              raw/ + wiki/ — your 12 pillars
└── study/             LIGHT — raw/ + wiki/ core, no sections yet

employee-with-a-side-shop/
├── AGENTS.md
├── life/
├── work/              STANDARD — role/ projects/ people/ wins/
└── businesses/
    └── side-shop/     LIGHT — raw/ + wiki/ core, occasional updates

agency-owner/
├── AGENTS.md
├── life/
└── businesses/
    ├── acme-studio/   DEEP — agency: clients/ projects/ proposals/ team/ decisions/
    └── app-lab/       STANDARD — product studio: product/ decisions/
```
