#!/usr/bin/env python3
"""Build dashboard.html for a 12-pillar workspace: pillars, deadlines, season,
people, areas and recent activity, read from the workspace's markdown files.

Usage: python3 dashboard.py [workspace]   (default: current directory)

Read-only on the workspace except for writing <workspace>/dashboard.html.
Uses only the standard library and loads nothing from the internet.
"""
import datetime as dt
import html
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
TODAY = dt.date.today()
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
if not os.path.isfile(os.path.join(ROOT, "life/wiki/index.md")):
    sys.exit("Not a 12-pillar workspace (no life/wiki/index.md): " + ROOT)


def read(path):
    try:
        if os.path.islink(path):
            return ""
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n?", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    return fm, text


def section(body, name):
    m = re.search(r"^##\s+" + re.escape(name) + r"\s*\n(.*?)(?=^##\s|\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def to_date(s):
    try:
        return dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def plain(s, n=220):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"[*_`>#]", "", s)
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def esc(s):
    return html.escape(s or "", quote=True)


def areas():
    """Folders with raw/ + wiki/ up to two levels down, besides life/."""
    found = []
    index = read(os.path.join(ROOT, "life/wiki/index.md"))
    for entry in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, entry)
        if entry.startswith(".") or entry == "life" or not os.path.isdir(p) or os.path.islink(p):
            continue
        cands = [p] + [os.path.join(p, e) for e in sorted(os.listdir(p)) if os.path.isdir(os.path.join(p, e))]
        for c in cands:
            if os.path.isdir(os.path.join(c, "raw")) and os.path.isdir(os.path.join(c, "wiki")):
                rel = os.path.relpath(c, ROOT)
                line = next((l for l in index.splitlines() if rel + "/" in l or "(" + rel in l), "")
                found.append((rel, "(archived)" in line.lower()))
    return found


LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def resolve(base_dir, href):
    """A relative link to a .md file inside the workspace, as a real path; else None."""
    if "://" in href or href.startswith(("#", "mailto:")):
        return None
    target = os.path.normpath(os.path.join(base_dir, href.split("#")[0]))
    inside = target.startswith(ROOT + os.sep) and "/raw/" not in target.replace(os.sep, "/")
    return target if inside and target.endswith(".md") and os.path.isfile(target) else None


def page_id(path):
    return "pg-" + re.sub(r"[^a-z0-9]+", "-", os.path.relpath(path, ROOT).lower()).strip("-")


def inline(text, base_dir, known):
    out, last = [], 0
    for m in LINK.finditer(text):
        out.append(esc(text[last:m.start()]))
        target = resolve(base_dir, m.group(2))
        if target and target in known:
            out.append('<a href="#%s">%s</a>' % (known[target], esc(m.group(1))))
        else:
            out.append(esc(m.group(1)))
        last = m.end()
    out.append(esc(text[last:]))
    h = "".join(out)
    h = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", h)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", h)


def md_to_html(body, base_dir, known):
    """Small markdown subset: headings, lists, checkboxes, paragraphs, bold, code, links."""
    html_out, para, in_list = [], [], False

    def flush():
        nonlocal para
        if para:
            html_out.append("<p>%s</p>" % inline(" ".join(para), base_dir, known))
            para = []

    for raw_line in body.splitlines():
        line = raw_line.rstrip()
        item = re.match(r"\s*[-*] (\[( |x|X)\] )?(.*)", line)
        if item and line.strip():
            flush()
            if not in_list:
                html_out.append("<ul>")
                in_list = True
            box = item.group(2)
            mark = "" if box is None else ('<span class="box">%s</span>' % ("☑" if box.lower() == "x" else "☐"))
            html_out.append("<li>%s%s</li>" % (mark, inline(item.group(3), base_dir, known)))
            continue
        if in_list:
            html_out.append("</ul>")
            in_list = False
        head = re.match(r"(#{1,4})\s+(.*)", line)
        if head:
            flush()
            level = min(len(head.group(1)) + 2, 6)
            html_out.append("<h%d>%s</h%d>" % (level, inline(head.group(2), base_dir, known), level))
        elif not line.strip():
            flush()
        else:
            para.append(line.strip())
    flush()
    if in_list:
        html_out.append("</ul>")
    return "".join(html_out)


# ---------- gather ----------
pillars = []
pdir = os.path.join(ROOT, "life/wiki/pillars")
for name in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
    if not name.endswith(".md"):
        continue
    fm, body = frontmatter(read(os.path.join(pdir, name)))
    status = re.search(r"\*\*Status:\*\*\s*(.+)", body)
    linked = [l for l in section(body, "Linked pages").splitlines() if l.strip().startswith("- ")]
    pillars.append({
        "num": name[:2],
        "title": fm.get("title") or name[3:-3].replace("-", " ").title(),
        "running": bool(status and status.group(1).strip().lower().startswith("running")),
        "updated": fm.get("updated", ""),
        "state": plain(section(body, "Where this stands"), 160),
        "links": len(linked),
        "path": os.path.join(pdir, name),
        "body": body,
    })

now_text = read(os.path.join(ROOT, "life/wiki/self/now.md"))
season = {k: (re.search(r"^" + k + r":\s*(.+)$", now_text, re.M) or [None, ""])[1].strip() for k in ("Season", "Since", "Until")}

area_list = areas()
action_files = [("life", os.path.join(ROOT, "life/wiki/actions.md"))] + [
    (rel, os.path.join(ROOT, rel, "wiki/actions.md")) for rel, archived in area_list if not archived]
actions = []
for where, path in action_files:
    for line in read(path).splitlines():
        m = re.match(r"\s*- \[ \]\s*(.+)", line)
        if not m:
            continue
        due = re.search(r"due (\d{4}-\d{2}-\d{2})", m.group(1))
        d = to_date(due.group(1)) if due else None
        text = re.sub(r"(?:,|—|\s)*due \d{4}-\d{2}-\d{2}", "", m.group(1))
        actions.append({"text": plain(text, 140), "due": d, "where": where})
actions.sort(key=lambda a: (a["due"] is None, a["due"] or TODAY))

people = []
for where, d in [("life", os.path.join(ROOT, "life/wiki/people"))] + [
        (rel, os.path.join(ROOT, rel, "wiki", s)) for rel, _ in area_list for s in ("people", "team")]:
    if not os.path.isdir(d):
        continue
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md"):
            continue
        fm, body = frontmatter(read(os.path.join(d, name)))
        def field(label):
            m = re.search(r"\*\*" + label + r":\*\*\s*(.+)", body, re.I)
            return plain(m.group(1), 80) if m else ""
        lc = DATE.search(field("Last contact"))
        last = to_date(lc.group(0)) if lc else None
        people.append({
            "name": fm.get("title") or name[:-3].replace("-", " ").title(),
            "where": where, "circle": field("Circle").split(" ")[0] if field("Circle") else "",
            "role": field("Role"), "last": last, "cadence": field("Stay in touch"),
        })

activity = []
for where, path in [("life", os.path.join(ROOT, "life/wiki/log.md"))] + [
        (rel, os.path.join(ROOT, rel, "wiki/log.md")) for rel, _ in area_list]:
    for m in re.finditer(r"^## \[(\d{4}-\d{2}-\d{2})\]\s*(\w+)\s*\|\s*(.+)$", read(path), re.M):
        activity.append((m.group(1), m.group(2), plain(m.group(3), 100), where))
seen, recent = set(), []
for a in sorted(activity, key=lambda x: x[0], reverse=True):
    if (a[0], a[2]) in seen:
        continue
    seen.add((a[0], a[2]))
    recent.append(a)
month = TODAY.strftime("%Y-%m")
# One operation is logged in every folder it touched, under that folder's own title: count life's
# log, plus area entries on days life has no entry of that kind.
ops = [a for a in activity if a[0].startswith(month) and a[1] in ("capture", "wrap")]
life_ops = [a for a in ops if a[3] == "life"]
life_keys = {(a[0], a[1]) for a in life_ops}
month_count = len(life_ops) + len({(a[0], a[1], a[3]) for a in ops if a[3] != "life" and (a[0], a[1]) not in life_keys})

owner = (re.match(r"#\s*(.+?)'s Life Workspace", read(os.path.join(ROOT, "AGENTS.md"))) or [None, ""])[1]

# ---------- render ----------
def due_chip(d):
    if d is None:
        return '<span class="chip">no date</span>'
    days = (d - TODAY).days
    if days < 0:
        return f'<span class="chip bad">overdue {-days}d</span>'
    if days == 0:
        return '<span class="chip bad">today</span>'
    if days <= 7:
        return f'<span class="chip warn">in {days}d</span>'
    return f'<span class="chip">{d.strftime("%d %b")}</span>'


running = sum(p["running"] for p in pillars)
open_due = [a for a in actions if a["due"] and (a["due"] - TODAY).days <= 7]

def pillar_card(p):
    meta = "running" if p["running"] else "not yet running"
    if p["running"] and p["updated"]:
        meta += " · updated " + esc(p["updated"])
    if p["links"]:
        meta += " · %d linked" % p["links"]
    state = "<p>%s</p>" % esc(p["state"]) if p["state"] else ""
    return ('<a class="pillar %s" href="#p-%s"><div class="ph"><span class="pn">%s</span><span class="pt">%s</span></div>%s<div class="pm">%s</div></a>'
            % ("on" if p["running"] else "off", esc(p["num"]), esc(p["num"]), esc(p["title"]), state, meta))


pillar_cards = "".join(pillar_card(p) for p in pillars)

# Each pillar opens a full view: the hub page, then every wiki page it links to, all in this file.
details = []
for p in pillars:
    base = os.path.dirname(p["path"])
    linked_pages = []
    for m in LINK.finditer(p["body"]):
        t = resolve(base, m.group(2))
        if t and t not in linked_pages and t != p["path"]:
            linked_pages.append(t)
    linked_pages = linked_pages[:25]
    known = {t: "p%s-%s" % (p["num"], page_id(t)) for t in linked_pages}
    parts = []
    for t in linked_pages:
        fm, body = frontmatter(read(t)[:30000])
        body = re.sub(r"^#\s+.*\n", "", body, count=1)
        parts.append('<details id="%s"><summary>%s <span class="aw">%s</span></summary><div class="md">%s</div></details>'
                     % (known[t], esc(fm.get("title") or os.path.basename(t)[:-3]), esc(os.path.relpath(t, ROOT)),
                        md_to_html(body, os.path.dirname(t), known)))
    hub = re.sub(r"^#\s+.*\n", "", p["body"], count=1)
    details.append('<section class="detail" id="p-%s"><a class="back" href="#top">← All pillars</a><h2 class="dt">%s %s</h2>'
                   '<div class="md">%s</div>%s</section>'
                   % (esc(p["num"]), esc(p["num"]), esc(p["title"]), md_to_html(hub, base, known),
                      ('<h3>The pages behind it <span class="aw">(click to open)</span></h3>' + "".join(parts)) if parts else ""))
pillar_details = "".join(details)

action_rows = "".join(
    f'<li>{due_chip(a["due"])}<span class="at">{esc(a["text"])}</span><span class="aw">{esc(a["where"])}</span></li>'
    for a in actions[:30]) or '<li class="muted">No open to-dos. Mention a deadline in chat and it lands here.</li>'


def last_txt(p):
    if not p["last"]:
        return "—"
    days = (TODAY - p["last"]).days
    return f"{days}d ago" if days > 0 else "today"


people_rows = "".join(
    f'<tr><td>{esc(p["name"])}</td><td>{esc(p["circle"] or p["role"] or "")}</td>'
    f'<td>{esc(p["cadence"])}</td><td>{esc(last_txt(p))}</td><td class="muted">{esc(p["where"])}</td></tr>'
    for p in sorted(people, key=lambda p: (p["last"] is not None, p["last"] or TODAY))[:40]
) or '<tr><td colspan="5" class="muted">No people pages yet.</td></tr>'

area_rows = "".join(
    f'<li><b>{esc(rel)}/</b>{" <span class=chip>archived</span>" if arch else ""}</li>' for rel, arch in area_list
) or '<li class="muted">Only life/ so far.</li>'

recent_rows = "".join(
    f'<li><span class="ad">{esc(d)}</span><span class="chip">{esc(k)}</span>{esc(t)} <span class="aw">{esc(w)}</span></li>'
    for d, k, t, w in recent[:12]) or '<li class="muted">Nothing logged yet.</li>'

season_html = (
    f'<div class="season"><span class="lbl">Season</span><b>{esc(season["Season"])}</b>'
    f'{"<span>since " + esc(season["Since"]) + "</span>" if season["Since"] else ""}'
    f'{"<span>until " + esc(season["Until"]) + "</span>" if season["Until"] else ""}</div>'
    if season["Season"] else "")

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(owner + "'s " if owner else "")}Life Dashboard</title>
<style>
:root{{--bg:#f7f6f2;--card:#fff;--fg:#1e2422;--muted:#6b736f;--line:#e2dfd6;--accent:#2f6b57;--accent-soft:#e2efe8;--warn:#a1620f;--warn-soft:#f8ecd9;--bad:#b23a2e;--bad-soft:#f8e1de}}
@media (prefers-color-scheme:dark){{:root{{--bg:#131816;--card:#1b2220;--fg:#e6ebe8;--muted:#98a29d;--line:#2c3532;--accent:#7cc4a6;--accent-soft:#1e3a2f;--warn:#e2b26a;--warn-soft:#3a2d18;--bad:#ef8a7e;--bad-soft:#3d2220;color-scheme:dark}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif;padding:32px max(16px,env(safe-area-inset-left))}}
main{{max-width:1100px;margin:0 auto;display:grid;gap:28px}}
h1{{font-size:1.8rem;margin:0}}h2{{font-size:1.05rem;margin:0 0 12px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600}}
header{{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:baseline;justify-content:space-between}}
.stats{{display:flex;gap:18px;flex-wrap:wrap;color:var(--muted)}}.stats b{{color:var(--fg);font-size:1.15rem;font-variant-numeric:tabular-nums}}
.season{{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline;background:var(--accent-soft);padding:12px 16px;border-radius:10px}}
.lbl{{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}}
.pillar{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;gap:6px;align-content:start}}
.pillar.on{{border-color:var(--accent)}}.pillar.off{{opacity:.75}}.pillar p{{margin:0;font-size:.92rem}}
.ph{{display:flex;gap:8px;align-items:baseline}}.pn{{font-variant-numeric:tabular-nums;color:var(--accent);font-weight:700}}.pt{{font-weight:600}}
.pm,.muted,.aw,.ad{{color:var(--muted);font-size:.82rem}}
.two{{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:28px}}.two>section{{min-width:0}}@media (max-width:820px){{.two{{grid-template-columns:minmax(0,1fr)}}}}
section>div,section>ul{{min-width:0}}
ul.list{{list-style:none;margin:0;padding:0;display:grid;gap:8px}}ul.list li{{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px 12px}}
.at{{flex:1;min-width:160px}}
.chip{{font-size:.75rem;padding:1px 8px;border-radius:999px;background:var(--line);white-space:nowrap}}.chip.warn{{background:var(--warn-soft);color:var(--warn)}}.chip.bad{{background:var(--bad-soft);color:var(--bad)}}
.tw{{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:10px}}table{{border-collapse:collapse;width:100%;font-size:.92rem}}
th,td{{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line)}}th{{font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}}
footer{{color:var(--muted);font-size:.8rem}}
a.pillar{{color:inherit;text-decoration:none}}a.pillar:hover,a.pillar:focus-visible{{outline:2px solid var(--accent);outline-offset:1px}}
.detail{{display:none;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 22px;gap:10px}}
.detail:target{{display:grid}}.back{{color:var(--accent);text-decoration:none;font-size:.9rem}}.dt{{font-size:1.4rem;text-transform:none;letter-spacing:0;color:var(--fg)}}
.md{{max-width:72ch;min-width:0;overflow-wrap:anywhere}}.md h3,.md h4,.md h5,.md h6{{margin:18px 0 6px;font-size:1rem}}.md p{{margin:6px 0}}.md ul{{margin:6px 0;padding-left:1.2em}}
.md a{{color:var(--accent)}}.md code{{font-size:.9em;background:var(--bg);padding:0 4px;border-radius:4px}}.box{{margin-right:6px;color:var(--accent)}}
details{{border-top:1px solid var(--line);padding:10px 0}}summary{{cursor:pointer;font-weight:600}}details .md{{padding:6px 0 0 14px}}
.overview{{display:grid;gap:28px}}body.in-detail .overview{{display:none}}
</style></head><body><main id="top">
{pillar_details}
<div class="overview">
<header><h1>{esc(owner + "'s " if owner else "")}Life Dashboard</h1>
<div class="stats"><span><b>{running}</b>/12 pillars running</span><span><b>{len(open_due)}</b> due this week</span><span><b>{month_count}</b> captures &amp; wraps this month</span></div></header>
{season_html}
<section><h2>The 12 pillars <span class="aw" style="text-transform:none;letter-spacing:0">· click one to open it</span></h2><div class="grid">{pillar_cards or '<p class="muted">No pillar pages found. Run setup first.</p>'}</div></section>
<div class="two">
<section><h2>Deadlines &amp; to-dos</h2><ul class="list">{action_rows}</ul></section>
<section><h2>Recent activity</h2><ul class="list">{recent_rows}</ul></section>
</div>
<div class="two">
<section><h2>People</h2><div class="tw"><table><tr><th>Name</th><th>Circle / role</th><th>Stay in touch</th><th>Last contact</th><th>Where</th></tr>{people_rows}</table></div></section>
<section><h2>Areas</h2><ul class="list">{area_rows}</ul></section>
</div>
</div>
<footer>Built {TODAY.isoformat()} from the files in this folder. Nothing here leaves your computer. Ask for the 12-pillars dashboard skill to refresh it.</footer>
</main>
<script>
function show(){{
  var id = decodeURIComponent(location.hash.slice(1)), el = id && document.getElementById(id);
  var sec = el && (el.classList.contains("detail") ? el : el.closest(".detail"));
  document.body.classList.toggle("in-detail", !!sec);
  document.querySelectorAll(".detail").forEach(function (d) {{ d.style.display = d === sec ? "grid" : "none"; }});
  if (el && el.tagName === "DETAILS") {{ el.open = true; el.scrollIntoView(); }} else {{ window.scrollTo(0, 0); }}
}}
window.addEventListener("hashchange", show); show();
</script></body></html>"""

out = os.path.join(ROOT, "dashboard.html")
if os.path.islink(out):
    sys.exit("dashboard.html is a symlink; not writing through it.")
tmp = out + ".tmp"
fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_NOFOLLOW", 0), 0o600)
with os.fdopen(fd, "w", encoding="utf-8") as f:
    f.write(page)
os.replace(tmp, out)
print(out)
