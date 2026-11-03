# Folder Design — units inside the pillars

> The twelve pillar folders are the whole second brain. Nothing lives outside them. When part of a person's world produces its own stream of information (their studies, their job, a business, their investing), it gets a **unit**: a subfolder inside the pillar it belongs to, sized to what it actually holds.

Use this during `/12-pillars:setup` and `/12-pillars:add-business`. The goal is a structure the person will actually keep up, not the most complete one possible.

## 1. Start from what fills their days

Ask one **open question** in plain text (no buttons): **"In a sentence or two, what fills your days right now? Studies, a job, businesses you run, clients, content, investing, anything goes."** Show one example answer so they know the level of detail: "I'm in my final year of uni, intern three days a week, and run a small design agency on the side with a friend."

Read the answer for every part of their world, including ones they mention in passing ("and I post on YouTube" is brand). Pick up names (the business, the employer, the school) so units can use them. If something is unclear, ask one short follow-up, then propose. Always ask it when it's unclear whether they **own** a business or **work for** one ("I work full time in an agency" could be either): "Is the agency yours (or part yours), or are you employed there?" Owner or partner → a business unit; employee → a job unit. Don't run through a checklist of roles they didn't mention.

| They mentioned | Where it lives | Archetype (section 3) |
|---|---|---|
| Studying | `05-development/<school>/` (e.g. `05-development/nus/`) | Student |
| Working a job | `07-career/<employer>/` (a new job later gets its own unit; the old one is archived where it is) | Employee |
| Running a business | `09-opportunities/<name>/`, one per business | the closest business archetype |
| Freelance, agency or client work | `09-opportunities/<name>/` for their practice | Agency / services or Consulting / coaching |
| Creating content as a channel or media business | `09-opportunities/<channel>/` | Content / media / creator |
| Building their own personal brand, posting their own content | directly in `08-brand/` (`posts/`, `ideas.md`); no unit | — |
| Investing | `10-finance/investing/` | Investing / holding |
| Between things right now | no unit; the pillars cover it (Career, Opportunities) | — |

Mix freely: a final-year student who also runs an agency and wants a personal brand gets `05-development/<school>/`, `09-opportunities/<agency>/`, and posts in `08-brand/`. Use the person's own words for unit names ("call it uni"); the unit's `overview.md` and the Units section of `index.md` record what it is, so any name works. Never create a unit for something they didn't mention.

## 2. What a unit gets

Every unit starts small: `overview.md` (what it is in one line, their role, the stage or current state, and the **names that route to it**: the unit name plus the clients, projects, school or employer names they'll actually type, never a pillar tag like `#brand`). Add `ideas.md`, `decisions/` and section folders only once there is something to put in them. Unused empty folders become clutter.

When a unit already shows things they'll need to look up later (named clients, a team, several live deliverables such as exams or projects), propose those sections up front, using the names they gave (`clients/`, `projects/`, `courses/`). Each named client or partner gets its own page once something is captured about it, not an empty page up front. Otherwise start with the overview only.

People are never stored inside a unit: colleagues, managers and client contacts get pages in `06-relationships/people/` with their role and a link to the unit. Client and partner organisations do get a page in the unit's `clients/`.

## 3. Sections by archetype

Pick the archetype closest to the unit, then keep only the sections it actually runs on.

| Archetype | Suggested sections |
|---|---|
| Student | `courses/` (one page per course or module) · `projects/` (assignments, thesis) · `exams/` · `applications/` (internships, jobs) |
| Employee (working for someone else) | `role/` (responsibilities, goals, reviews) · `projects/` · `clients/` · `wins/` |
| Agency / services | `clients/` · `projects/` · `proposals/` |
| Consulting / coaching | `clients/` · `engagements/` · `frameworks/` (their own methods) |
| SaaS / software product | `product/` (features, roadmap) · `customers/` · `metrics/` |
| E-commerce / consumer brand | `products/` · `suppliers/` · `campaigns/` · `customers/` (segments, not individuals) |
| F&B / retail / physical | `outlets/` · `menu/` or `skus/` · `suppliers/` · `operations/` |
| Content / media / creator | `content/` (pieces and series) · `audience/` · `sponsors/` |
| Investing / holding | `portfolio/` (one page per holding) · `deals/` · `theses/` |
| Deal-driven (sales, real estate, brokerage) | `deals/` (one page per deal: budget, decision-maker, need, timeline, status) · `listings/` or `offers/` |
| Research / early-stage idea | `research/` · `experiments/` |

`decisions/` (what was decided, when, why) applies to every unit once a decision is made; `meetings/` if it has many of them.

## 4. Show it before building it

Always show the proposed tree before creating anything: the twelve pillars as one line, then each unit under its pillar in the person's own words, with its sections. No plumbing files. Ask for one confirm and accept changes in plain language ("call it uni", "drop investing", "add a team section").

   ✅ Here's what I'd set up for you:
   ```
   01–12        your 12 pillars (the whole second brain)
   05-development/nus/      final sem (Y4S1)
     courses/  projects/  exams/
   07-career/twiss/         tech lead
     clients/   Supercane, Esperanza, Axcel
     projects/  Torchie, Noted
   08-brand/                your posts, starting small
   ```
   Everything you share is saved as-is in raw/, and I keep the pages organised.

Keep lines under about 50 characters so nothing wraps in a narrow chat window. Then the confirm question: "Create this?" with options "Create it" and "Change something".

## 5. When things change

- **A new job, school or business** that keeps coming up with no unit: offer a unit once.
- **A unit grows:** offer sections when its pages pile up (`/12-pillars:add-business <unit>`).
- **A unit ends** (graduated, left the job, closed the business): mark it `(archived)` in the Units section of `index.md` and remove its routing names, so new captures stop going there. Its folder stays where it is.
