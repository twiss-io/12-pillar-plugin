# Folder Design — recommending a structure for each business

> Every business gets a folder shaped to how much information it actually produces. A side project doesn't need a full wiki. A business with clients, a team, and a pipeline does.

Use this during `/12-pillars:setup` and `/12-pillars:add-business`. The goal is a structure the person will actually keep up, not the most complete one possible.

## 1. Interview first

Ask these for each business, one at a time. Use clickable options where the answer is a choice.

1. **What does it do, and for whom?** (one line)
2. **Your role:** founder / partner / employee / freelancer / investor / advisor
3. **Stage:** idea · building · launched · growing · established · winding down
4. **What does it run on?** Pick all that apply: clients · customers (many, small) · products · projects · deals/sales pipeline · content · a team · suppliers/partners · physical locations · research
5. **How often will you add information?** daily · weekly · occasionally
6. **Do you need to look things up later** (past decisions, client history, what was promised), **or is it mostly a to-do list?**

## 2. Choose the tier

| Tier | When | Structure |
|---|---|---|
| **Light** | Side project, idea stage, occasional notes, little history to look up | `businesses/<name>/notes.md`, a single running page of dated bullets, starting with a one-paragraph summary and a `Tags:` line (folder name plus aliases). No raw/wiki split. |
| **Standard** | Active business with ongoing information, but one main area of activity | `AGENTS.md` (+ `CLAUDE.md` importing it), `raw/`, `wiki/` with `index.md`, `log.md`, `overview.md`, and one or two sections. |
| **Deep** | Several areas of activity (clients plus team plus product, for example) and a real need to look things up | Standard plus all the sections that match its archetype below. |

When unsure, go one tier lighter. A business can always be upgraded later (`/12-pillars:add-business <name>` on an existing light folder offers the upgrade). Unused empty folders get ignored and become clutter.

## 3. Sections by business type

Pick the archetype closest to the business, then keep only the sections it actually runs on (from interview question 4). Mixed businesses can combine sections.

| Archetype | Suggested `wiki/` sections |
|---|---|
| Agency / services | `clients/` · `projects/` · `proposals/` · `team/` |
| Consulting / coaching | `clients/` · `engagements/` · `frameworks/` (their own methods) · `content/` |
| SaaS / software product | `product/` (features, roadmap, decisions) · `customers/` · `metrics/` · `team/` |
| E-commerce / consumer brand | `products/` · `suppliers/` · `campaigns/` · `customers/` (segments, not individuals) |
| F&B / retail / physical | `outlets/` · `menu/` or `skus/` · `suppliers/` · `staff/` · `operations/` |
| Content / media / creator | `content/` (pieces and series) · `audience/` · `sponsors/` · `ideas/` |
| Investing / holding | `portfolio/` (one page per holding) · `deals/` · `theses/` |
| Deal-driven (sales, real estate, brokerage) | `deals/` (one page per deal: budget, decision-maker, need, timeline, status) · `contacts/` · `listings/` or `offers/` |
| Research / early-stage idea | `research/` · `experiments/` · `decisions/` |
| Employee (working for someone else) | `role/` (responsibilities, goals) · `projects/` · `people/` (colleagues, stakeholders) · `wins/` |

Sections that apply to almost every business: `decisions/` (what was decided, when, why), and `meetings/` if the business has many of them.

## 4. Write the business schema

Each Standard or Deep business gets its own `AGENTS.md` (with a one-line `CLAUDE.md`: `@AGENTS.md`, so Claude Code reads it too) holding:
- what the business is, in one line, and the person's role
- its tier and chosen sections, and what goes in each
- the tags that route captures here: the folder name (for example `#acme-studio`) plus any short aliases the person will actually type (`#acme`, `#studio`)
- the boundary rule: content stays in this folder. Nothing from the personal `life/` folder is copied in. Nothing from here is copied into other businesses.

## 5. Show it before building it

Always render the proposed tree for the whole workspace before creating anything, with a one-line reason per business ("Standard — active clients and projects, weekly updates"). Ask for one confirm. Accept changes in plain language ("make App Lab light", "add a team section"). Only then create the folders and files.

Example of a recommendation:

```
your-workspace/
├── AGENTS.md
├── life/            raw/ + wiki/ — your 12 pillars
└── businesses/
    ├── acme-studio/ DEEP — agency: clients/ projects/ proposals/ team/ decisions/
    ├── app-lab/     STANDARD — product studio: product/ decisions/
    └── side-shop/   LIGHT — notes.md only, occasional updates
```
