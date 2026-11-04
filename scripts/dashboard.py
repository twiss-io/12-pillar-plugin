#!/usr/bin/env python3
"""Build dashboard.html for a 12-pillar workspace: pillars, deadlines, season,
people, units and recent activity, read from the workspace's twelve pillar folders.

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
if not (os.path.isfile(os.path.join(ROOT, "index.md")) and os.path.isdir(os.path.join(ROOT, "02-identity"))):
    if os.path.isfile(os.path.join(ROOT, "life/wiki/index.md")):
        sys.exit("This workspace uses the layout from before 0.8.0. Run the 12-pillars lint skill with 'rules' to move it into the pillar folders first.")
    sys.exit("Not a 12-pillar workspace (no index.md and pillar folders): " + ROOT)
PILLAR_DIR = re.compile(r"^(\d\d)-[a-z-]+$")
SKIP = {"README.md", "AGENTS.md", "CLAUDE.md"}


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


def units():
    """Unit folders (an overview.md) inside the pillar folders, with their archived state."""
    found = []
    index = read(os.path.join(ROOT, "index.md"))
    for entry in sorted(os.listdir(ROOT)):
        if not PILLAR_DIR.match(entry):
            continue
        p = os.path.join(ROOT, entry)
        for sub in sorted(os.listdir(p)):
            c = os.path.join(p, sub)
            if os.path.isdir(c) and not os.path.islink(c) and os.path.isfile(os.path.join(c, "overview.md")):
                rel = os.path.relpath(c, ROOT)
                line = next((l for l in index.splitlines() if rel + "/" in l), "")
                found.append((rel, "(archived)" in line.lower()))
    return found


def pages_in(folder):
    """Every page in a pillar folder (units included), README and agent files left out."""
    out = []
    for dirpath, dirnames, files in os.walk(folder):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and not os.path.islink(os.path.join(dirpath, d)))
        for f in sorted(files):
            if f.endswith(".md") and not (dirpath == folder and f in SKIP) and f not in ("AGENTS.md", "CLAUDE.md"):
                out.append(os.path.join(dirpath, f))
    return out


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
PILLARS = [  # number, short name, colour (light, dark)
    ("01", "Faith", "#8b6fd6", "#b3a0f0"), ("02", "Identity", "#5b7be0", "#94acff"),
    ("03", "Time", "#2f9fb8", "#6fd0e4"), ("04", "Health", "#3aa66b", "#74d49c"),
    ("05", "Development", "#7aa33a", "#b0d46c"), ("06", "Relationships", "#d9677e", "#f39aac"),
    ("07", "Career", "#c98a2e", "#ecb764"), ("08", "Brand", "#e0773f", "#ffa775"),
    ("09", "Opportunities", "#b85c9e", "#e594cb"), ("10", "Finance", "#2e8c7a", "#6cc9b5"),
    ("11", "Lifestyle", "#d4a017", "#f2c94c"), ("12", "Legacy", "#6b7a8f", "#a7b4c6"),
]
SHORT = {n: (short, c, cd) for n, short, c, cd in PILLARS}
TAG2NUM = {short.lower(): n for n, short, _, _ in PILLARS}
TAG2NUM.update({"opportunity": "09", "wbo": "09", "work": "09", "growth": "05", "study": "05"})

pillars = []
for name in sorted(os.listdir(ROOT)):
    folder = os.path.join(ROOT, name)
    if not PILLAR_DIR.match(name) or not os.path.isdir(folder) or os.path.islink(folder):
        continue
    readme = os.path.join(folder, "README.md")
    fm, body = frontmatter(read(readme))
    status = re.search(r"\*\*Status:\*\*\s*(.+)", body)
    focus = [plain(l.strip()[2:], 120) for l in section(body, "Current focus").splitlines() if l.strip().startswith(("- ", "* "))]
    if not focus and section(body, "Current focus"):
        focus = [plain(section(body, "Current focus"), 120)]
    num = name[:2]
    pillars.append({
        "num": num, "short": SHORT.get(num, (name[3:].title(), "#888", "#aaa"))[0],
        "title": fm.get("title") or name[3:].replace("-", " ").title(),
        "running": bool(status and status.group(1).strip().lower().startswith("running")),
        "updated": fm.get("updated", ""), "state": plain(section(body, "Where this stands"), 170),
        "focus": focus[:2], "pages": pages_in(folder), "path": readme, "body": body,
    })

now_text = read(os.path.join(ROOT, "02-identity/now.md"))
season = {k: (re.search(r"^" + k + r":\s*(.+)$", now_text, re.M) or [None, ""])[1].strip() for k in ("Season", "Since", "Until")}

# Latest self-scores (pillars skill): "### YYYY-MM-DD" then "- Faith: 7".
scores, score_date = {}, ""
blocks = re.split(r"^###\s+(\d{4}-\d{2}-\d{2}).*$", section(now_text, "Scores"), flags=re.M)
if len(blocks) >= 3:
    score_date, last = blocks[-2], blocks[-1]
    for n, short, _, _ in PILLARS:
        m = re.search(r"\b" + short + r"\b[^0-9\n]{0,40}?(\d{1,2})\b", last, re.I)
        if m and 0 < int(m.group(1)) <= 10:
            scores[n] = int(m.group(1))

goals = []
ns_fm, ns_body = frontmatter(read(os.path.join(ROOT, "02-identity/north-star.md")))
for l in ns_body.split("## Sources")[0].splitlines():
    if l.strip().startswith(("- ", "* ")):
        goals.append(plain(l.strip()[2:], 140))

unit_list = units()
actions = []
for line in read(os.path.join(ROOT, "actions.md")).splitlines():
    m = re.match(r"\s*- \[ \]\s*(.+)", line)
    if not m:
        continue
    due = re.search(r"due (\d{4}-\d{2}-\d{2})(?: (\d{1,2}:\d{2}))?", m.group(1))
    tags = re.findall(r"#([\w-]+)", m.group(1))
    num = next((TAG2NUM[t.lower()] for t in tags if t.lower() in TAG2NUM), "")
    text = re.sub(r"(?:,|—|\s)*due \d{4}-\d{2}-\d{2}(?: \d{1,2}:\d{2})?", "", re.sub(r"\s*#[\w-]+", "", m.group(1)))
    if due and due.group(2):
        text += " · " + due.group(2)
    actions.append({"text": plain(text, 120), "due": to_date(due.group(1)) if due else None, "num": num,
                    "tags": [t for t in tags if t.lower() not in TAG2NUM]})
actions.sort(key=lambda a: (a["due"] is None, a["due"] or TODAY))

CADENCE = [("week", 7), ("fortnight", 14), ("month", 31), ("quarter", 92), ("4", 92), ("year", 366)]
people = []
pdir = os.path.join(ROOT, "06-relationships/people")
for name in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
    if not name.endswith(".md"):
        continue
    fm, body = frontmatter(read(os.path.join(pdir, name)))
    def field(label):
        m = re.search(r"\*\*" + label + r":\*\*\s*(.+)", body, re.I)
        return plain(m.group(1), 80) if m else ""
    lc = DATE.search(field("Last contact"))
    cad = field("Stay in touch")
    every = next((d for k, d in CADENCE if k in cad.lower()), None)
    last = to_date(lc.group(0)) if lc else None
    people.append({
        "name": fm.get("title") or name[:-3].replace("-", " ").title(),
        "about": re.split(r"[(;,—]", field("Circle"))[0].strip()[:24] or field("Role")[:40],
        "last": last, "cadence": cad, "every": every,
        "overdue": bool(every and last and (TODAY - last).days > every),
    })
people.sort(key=lambda p: (not p["overdue"], p["last"] or dt.date.min))

activity = [(m.group(1), m.group(2), plain(m.group(3), 90))
            for m in re.finditer(r"^## \[(\d{4}-\d{2}-\d{2})\]\s*(\w+)\s*\|\s*(.+)$", read(os.path.join(ROOT, "log.md")), re.M)]
recent = sorted(activity, key=lambda x: x[0], reverse=True)
month = TODAY.strftime("%Y-%m")
month_count = sum(1 for a in activity if a[0].startswith(month) and a[1] in ("capture", "wrap"))

owner = (re.match(r"#\s*(.+?)'s Life Workspace", read(os.path.join(ROOT, "AGENTS.md"))) or [None, ""])[1]


# ---------- render ----------
# Design: an engineering-pad notebook. Grid paper, ink and pen marks instead of boxes; the
# flywheel drawn like a hand sketch; pillars as index tabs. Blueprint paper in dark mode.
import math

GIVES = {"01": "direction", "02": "clarity", "03": "allocation", "04": "capacity", "05": "skill",
         "06": "access", "07": "credibility", "08": "opportunity", "09": "finance", "10": "lifestyle",
         "11": "legacy", "12": "back to faith"}
by_num = {p["num"]: p for p in pillars}
running = sum(p["running"] for p in pillars)
overdue = [a for a in actions if a["due"] and a["due"] < TODAY]
week_start = TODAY - dt.timedelta(days=TODAY.weekday())
week_days = [week_start + dt.timedelta(days=k) for k in range(7)]
this_week = [a for a in actions if a["due"] and TODAY <= a["due"] <= week_days[-1]]
later = [a for a in actions if not a["due"] or a["due"] > week_days[-1]]


def pnum(num, cls=""):
    return '<span class="pn %s" style="--c:var(--p%s)">%s</span>' % (cls, num or "x", int(num) if num else "·")


def when(d):
    days = (d - TODAY).days
    if days < 0:
        return '<span class="pen">%d days late</span>' % -days if days < -1 else '<span class="pen">yesterday</span>'
    if days == 0:
        return '<mark>today</mark>'
    if days == 1:
        return '<mark>tomorrow</mark>'
    return '<span class="when">%s</span>' % (d.strftime("%a") if days <= 7 else d.strftime("%d %b"))


def todo_line(a, show_when=True):
    late = a["due"] and a["due"] < TODAY
    extra = (' <span class="faint">%s</span>' % esc(" · ".join(a["tags"]))) if a["tags"] else ""
    return ('<li class="%s"><span class="box"></span>%s<span class="txt">%s%s</span>%s</li>'
            % ("late" if late else "", pnum(a["num"]), esc(a["text"]), extra, when(a["due"]) if (a["due"] and show_when) else ""))


# Which pillar to start on: the lowest score, ties going upstream; without scores, the first not running.
def start_here():
    if scores:
        return min(scores, key=lambda n: (scores[n], n))
    off = [p["num"] for p in pillars if not p["running"]]
    return off[0] if off else ""


START = start_here()


def flywheel():
    W, H, cx, cy, R = 720, 600, 360, 305, 210
    out = ['<svg viewBox="0 0 %d %d" class="wheel" role="img" aria-label="The 12-pillar flywheel">' % (W, H)]
    out.append('<circle cx="%d" cy="%d" r="%d" class="ring"/>' % (cx, cy, R))
    pts = []
    for k in range(12):
        ang = -math.pi / 2 + k * 2 * math.pi / 12
        pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang), ang))
    for k in range(12):  # currency labels on the arcs
        a1, a2 = pts[k][2], pts[(k + 1) % 12][2] + (2 * math.pi if k == 11 else 0)
        mid = (a1 + a2) / 2
        lx, ly = cx + (R - 34) * math.cos(mid), cy + (R - 34) * math.sin(mid)
        out.append('<text x="%.0f" y="%.0f" class="cur" text-anchor="middle">%s</text>' % (lx, ly + 4, esc(GIVES["%02d" % (k + 1)])))
        # arrowhead on the ring just before the next node
        ah = a2 - 0.16
        ax, ay = cx + R * math.cos(ah), cy + R * math.sin(ah)
        tx, ty = -math.sin(ah), math.cos(ah)
        out.append('<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" class="arr"/>'
                   % (ax, ay, -7 * tx + 5 * ty * 0, -7 * ty, ax, ay, -7 * tx - 0, -7 * ty + 0))
    for k, (x, y, ang) in enumerate(pts):
        num = "%02d" % (k + 1)
        p = by_num.get(num)
        sc = scores.get(num)
        r = 27
        fill = (sc / 10.0) if sc else (0.35 if p and p["running"] else 0)
        clip = "c%s" % num
        out.append('<a href="#p-%s" class="node%s" style="--c:var(--p%s)">' % (num, " on" if p and p["running"] else "", num))
        out.append('<clipPath id="%s"><rect x="%.0f" y="%.1f" width="%d" height="%.1f"/></clipPath>'
                   % (clip, x - r, y + r - 2 * r * fill, 2 * r, 2 * r * fill))
        out.append('<circle cx="%.0f" cy="%.0f" r="%d" class="nb"/>' % (x, y, r))
        if fill:
            out.append('<circle cx="%.0f" cy="%.0f" r="%d" class="nf" clip-path="url(#%s)"/>' % (x, y, r, clip))
        out.append('<circle cx="%.0f" cy="%.0f" r="%d" class="no"/>' % (x, y, r))
        out.append('<text x="%.0f" y="%.0f" class="nn" text-anchor="middle">%d</text>' % (x, y + 6, k + 1))
        lx, ly = cx + (R + 52) * math.cos(ang), cy + (R + 50) * math.sin(ang)
        anchor = "middle" if abs(math.cos(ang)) < 0.3 else ("start" if math.cos(ang) > 0 else "end")
        lx = cx + (R + 40) * math.cos(ang) if anchor != "middle" else lx
        label = by_num[num]["short"] if p else num
        out.append('<text x="%.0f" y="%.0f" class="nl" text-anchor="%s">%s%s</text>'
                   % (lx, ly + 5, anchor, esc(label), (' <tspan class="sc">%d</tspan>' % sc) if sc else ""))
        out.append('</a>')
        if num == START:
            hx, hy = cx + (R + 95) * math.cos(ang), cy + (R + 95) * math.sin(ang)
            hx = min(max(hx, 70), W - 70); hy = min(max(hy, 48), H - 10)
            out.append('<path d="M%.0f %.0f Q %.0f %.0f %.0f %.0f" class="hand"/>' % (hx, hy - 12, (hx + x) / 2 + 20, (hy + y) / 2 - 20, x + (8 if x < hx else -8), y - 26))
            out.append('<text x="%.0f" y="%.0f" class="note" text-anchor="middle">start here</text>' % (hx, hy - 18))
    out.append('<text x="%d" y="%d" class="big" text-anchor="middle">%d<tspan class="of">/12</tspan></text>' % (cx, cy + 4, running))
    out.append('<text x="%d" y="%d" class="cap" text-anchor="middle">pillars running</text>' % (cx, cy + 30))
    out.append('</svg>')
    return "".join(out)


# Season as a ruler: ticks from Since to Until with today marked.
def season_ruler():
    if not season["Season"]:
        return '<p class="faint">No season set. Tell me what season you\'re in (a launch, exams, a reset) and it shows here.</p>'
    s0, s1 = to_date(season["Since"]), to_date(season["Until"])
    head = '<div class="sz"><span class="eyebrow">Season</span><b>%s</b></div>' % esc(season["Season"])
    if not (s0 and s1 and s1 > s0):
        return head + ('<p class="faint">%s</p>' % (("since " + esc(season["Since"])) if s0 else ""))
    total = (s1 - s0).days
    done = min(max((TODAY - s0).days, 0), total)
    left = (s1 - TODAY).days
    ticks = "".join('<i class="%s"></i>' % ("d" if k < done else "") for k in range(total + 1))
    return head + ('<div class="ruler" style="--n:%d">%s</div><div class="rl"><span>%s</span><b>%s</b><span>%s</span></div>'
                   % (total + 1, ticks, s0.strftime("%d %b"),
                      ("%d days left" % left) if left > 0 else ("ends today" if left == 0 else "ended"), s1.strftime("%d %b")))


week_cols = []
for d in week_days:
    items = [a for a in actions if a["due"] == d]
    lis = "".join('<li>%s%s</li>' % (pnum(a["num"]), esc(a["text"])) for a in items)
    week_cols.append('<div class="wd%s"><div class="wh"><span>%s</span><b>%d</b></div><ul>%s</ul></div>'
                     % (" today" if d == TODAY else " past" if d < TODAY else "", d.strftime("%a"), d.day, lis))

first = TODAY.replace(day=1)
nxt = (first + dt.timedelta(days=32)).replace(day=1)
d = first - dt.timedelta(days=first.weekday())
cal = ['<b>%s</b>' % w for w in "MTWTFSS"]
while d < nxt or d.weekday() != 0:
    items = [a for a in actions if a["due"] == d]
    cls = " ".join(c for c in ("out" if d.month != TODAY.month else "", "now" if d == TODAY else "", "has" if items else "") if c)
    cal.append('<span class="%s" title="%s">%d%s</span>' % (cls, esc("; ".join(a["text"] for a in items)), d.day,
               "".join('<i style="--c:var(--p%s)"></i>' % (a["num"] or "x") for a in items[:3])))
    d += dt.timedelta(days=1)


def last_txt(p):
    if not p["last"]:
        return "—"
    days = (TODAY - p["last"]).days
    return "today" if days <= 0 else "%dd" % days


people_lines = "".join(
    '<li class="%s"><span class="txt"><b>%s</b> <span class="faint">%s</span></span>%s</li>'
    % ("late" if p["overdue"] else "", esc(p["name"]), esc(p["about"]),
       '<span class="pen">reach out</span>' if p["overdue"] else '<span class="when">%s</span>' % esc(last_txt(p)))
    for p in people[:8]) or '<li class="faint">People you mention get a page; who\'s due a check-in shows here.</li>'

goal_lines = "".join('<li><span class="gn">%d</span><span class="txt">%s</span></li>' % (k + 1, esc(g)) for k, g in enumerate(goals[:9])) \
    or '<li class="faint">Your north star declarations show here once setup writes them.</li>'

log_lines = "".join('<li><span class="ld">%s</span><span class="lk">%s</span><span class="txt">%s</span></li>'
                    % (esc(dt.date.fromisoformat(a[0]).strftime("%d.%m")), esc(a[1]), esc(a[2])) for a in recent[:9]) \
    or '<li class="faint">Nothing logged yet.</li>'

unit_lines = "".join('<li>%s<span class="txt"><b>%s</b> <span class="faint">in %s%s</span></span></li>'
                     % (pnum(rel[:2]), esc(rel.split("/", 1)[-1].replace("-", " ").title()), esc(SHORT.get(rel[:2], ("",))[0]),
                        " · archived" if arch else "") for rel, arch in unit_list)

today_list = "".join(todo_line(a) for a in overdue + this_week) or '<li class="faint">Nothing due this week. Enjoy it.</li>'
later_list = "".join(todo_line(a) for a in later[:6])

focus_lines = "".join('<li>%s<span class="txt">%s</span></li>' % (pnum(p["num"]), esc(p["focus"][0])) for p in pillars if p["focus"]) \
    or '<li class="faint">Each pillar\'s current focus shows here.</li>'


# ---------- pillar pages and reading views ----------
def summary(body):
    for para in re.split(r"\n\s*\n", body):
        t = para.strip()
        if t and not t.startswith(("#", "---", "|", "**Status")):
            return plain(t, 140)
    return ""


def bullets(text):
    out = [l.strip()[2:] for l in text.splitlines() if l.strip().startswith(("- ", "* "))]
    return out or ([text.strip()] if text.strip() else [])


details, readers = [], []
for p in pillars:
    base = os.path.dirname(p["path"])
    linked_out = []
    for m in LINK.finditer(p["body"]):
        t = resolve(base, m.group(2))
        if t and t not in p["pages"] and t not in linked_out and t != p["path"]:
            linked_out.append(t)
    known = {t: "p%s-%s" % (p["num"], page_id(t)) for t in p["pages"][:80] + linked_out[:20]}

    def entry(t):
        fm, body = frontmatter(read(t)[:30000])
        body = re.sub(r"^#\s+.*\n", "", body, count=1)
        main_body = body.split("\n## Sources")[0]
        srcs = section(body, "Sources")
        title = fm.get("title") or os.path.basename(t)[:-3].replace("-", " ").title()
        rid = known[t]
        readers.append(
            '<article class="view reader" id="%s" style="--c:var(--p%s)"><a class="back" href="#p-%s">← %s</a>'
            '<p class="eyebrow">%s · %s</p><h1>%s</h1><div class="md">%s</div>%s</article>'
            % (rid, p["num"], p["num"], esc(p["short"]), esc(fm.get("type", "page")),
               esc(fm.get("updated", "")), esc(title), md_to_html(main_body, os.path.dirname(t), known),
               ('<div class="srcs"><p class="eyebrow">From your notes</p>%s</div>' % md_to_html(srcs, os.path.dirname(t), known)) if srcs else ""))
        return ('<li><a href="#%s"><span class="tt">%s</span><span class="dots"></span><span class="faint">%s</span></a>%s</li>'
                % (rid, esc(title), esc(fm.get("updated", "") or fm.get("type", "")),
                   ('<span class="sum">%s</span>' % esc(summary(main_body))) if summary(main_body) else ""))

    groups, own = {}, []
    for t in p["pages"][:80]:
        rel = os.path.relpath(t, base).split(os.sep)
        if len(rel) > 1 and os.path.isfile(os.path.join(base, rel[0], "overview.md")):
            groups.setdefault(rel[0], []).append(t)
        else:
            own.append(t)
    toc = []
    for unit, ts in groups.items():
        ts.sort(key=lambda t: (os.path.basename(t) != "overview.md", t))
        toc.append('<h3>%s <span class="faint">· unit</span></h3><ul class="toc">%s</ul>' % (esc(unit.replace("-", " ").title()), "".join(entry(t) for t in ts)))
    if own:
        toc.append('<h3>In %s</h3><ul class="toc">%s</ul>' % (esc(p["short"]), "".join(entry(t) for t in own)))
    if linked_out:
        toc.append('<h3>From other pillars</h3><ul class="toc">%s</ul>' % "".join(entry(t) for t in linked_out[:20]))
    if not toc:
        toc.append('<p class="faint">No pages yet. Tell me anything about your %s and it lands here.</p>' % esc(p["short"].lower()))

    n = int(p["num"])
    pv, nx = "%02d" % (12 if n == 1 else n - 1), "%02d" % (1 if n == 12 else n + 1)
    focus = bullets(section(p["body"], "Current focus"))
    openq = bullets(section(p["body"], "Open questions"))
    tasks = "".join(todo_line(a) for a in actions if a["num"] == p["num"])
    li = lambda xs, empty: "".join('<li><span class="txt">%s</span></li>' % inline(x, base, known) for x in xs) or '<li class="faint">%s</li>' % empty
    where = section(p["body"], "Where this stands")
    sc = scores.get(p["num"])
    details.append(
        '<article class="view pillar" id="p-%(n)s" style="--c:var(--p%(n)s)"><a class="back" href="#top">← Dashboard</a>'
        '<header class="ph"><span class="huge">%(n)s</span><div><p class="eyebrow">Pillar %(i)d of 12%(sc)s</p><h1>%(title)s</h1>'
        '<p class="flowline"><a href="#p-%(pv)s">← %(pvs)s</a> gives %(pvg)s · <span class="hand">this gives %(g)s</span> · to <a href="#p-%(nx)s">%(nxs)s →</a></p></div></header>'
        '<p class="stands">%(where)s</p>'
        '<div class="cols3"><section><h2>Current focus</h2><ul class="lines">%(focus)s</ul></section>'
        '<section><h2>To do</h2><ul class="lines todo">%(tasks)s</ul></section>'
        '<section><h2>Open questions</h2><ul class="lines">%(openq)s</ul></section></div>'
        '<section class="index"><h2>Index</h2>%(toc)s</section></article>'
        % {"n": p["num"], "i": n, "title": esc(p["title"].split("·")[-1].strip()), "g": esc(GIVES[p["num"]]),
           "sc": (" · you scored it %d/10" % sc) if sc else ("" if p["running"] else " · not started"),
           "pv": pv, "pvs": esc(by_num[pv]["short"]) if pv in by_num else pv, "pvg": esc(GIVES.get(pv, "")),
           "nx": nx, "nxs": esc(by_num[nx]["short"]) if nx in by_num else nx,
           "where": inline(plain(where, 600), base, known) if where else '<span class="faint">Not filled in yet. It fills in as you share things about this part of your life.</span>',
           "focus": li(focus, "Nothing set yet."), "tasks": tasks or '<li class="faint">Nothing to do here right now.</li>',
           "openq": li(openq, "None yet."), "toc": "".join(toc)})
pillar_details = "".join(details) + "".join(readers)

tabs = "".join('<a href="#p-%s" style="--c:var(--p%s)" title="%s"><b>%s</b><span>%s</span></a>'
               % (p["num"], p["num"], esc(p["title"]), int(p["num"]), esc(p["short"])) for p in pillars)

palette_l = "".join("--p%s:%s;" % (n, c) for n, _, c, _ in PILLARS)
palette_d = "".join("--p%s:%s;" % (n, cd) for n, _, _, cd in PILLARS)
title = (owner + "'s " if owner else "") + "Life Planner"
greet = "Morning" if dt.datetime.now().hour < 12 else "Afternoon" if dt.datetime.now().hour < 18 else "Evening"

page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
:root{--paper:#fbfcfd;--grid:#e4eaf1;--grid2:#d3dce7;--ink:#1d2b45;--ink2:#56647d;--faint:#8b97aa;--pen:#d4402f;--mark:#ffe873;--px:#a7b0bd;
--disp:"Avenir Next Condensed","Futura","Helvetica Neue",Arial Narrow,sans-serif;--body:"Avenir Next","Helvetica Neue",system-ui,sans-serif;--hand:"Bradley Hand","Segoe Print","Comic Neue",cursive;--mono:"SF Mono",ui-monospace,Menlo,monospace;%(pl)s}
@media (prefers-color-scheme:dark){:root{--paper:#0e1d33;--grid:#173052;--grid2:#1f3d66;--ink:#e9f0fb;--ink2:#a9bbd6;--faint:#7086a6;--pen:#ff8a7a;--mark:#5c5214;--px:#5b6f8e;%(pd)s;color-scheme:dark}}
*{box-sizing:border-box}html,body{margin:0}
body{color:var(--ink);font:15px/1.55 var(--body);background-color:var(--paper);
background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px),linear-gradient(var(--grid2) 1px,transparent 1px),linear-gradient(90deg,var(--grid2) 1px,transparent 1px);
background-size:20px 20px,20px 20px,100px 100px,100px 100px;background-attachment:fixed}
a{color:inherit}
.sheet{max-width:1240px;margin:0 auto;padding:36px max(16px,4vw) 60px max(16px,4vw);padding-right:170px}@media (max-width:1180px){.sheet{padding-right:150px}}
.eyebrow{font:600 .72rem/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:0 0 6px}
.faint{color:var(--faint)}.pen{font-family:var(--hand);color:var(--pen);font-size:1.05rem;white-space:nowrap}
mark{background:linear-gradient(transparent 45%%,var(--mark) 45%%,var(--mark) 90%%,transparent 90%%);color:inherit;padding:0 2px;white-space:nowrap}
.when{font:.8rem var(--mono);color:var(--ink2);white-space:nowrap}
/* index tabs */
.tabs{position:fixed;right:0;top:50%%;transform:translateY(-50%%);display:grid;gap:3px;z-index:5}
.tabs a{display:flex;align-items:center;gap:8px;text-decoration:none;background:var(--c);color:#fff;border-radius:8px 0 0 8px;padding:7px 12px 7px 10px;width:138px;overflow:hidden;white-space:nowrap;font:600 .82rem var(--body);opacity:.82;transform:translateX(6px);transition:transform .15s ease,opacity .15s ease}
.tabs a b{font:700 .82rem var(--mono);min-width:18px;text-align:center}
.tabs a:hover,.tabs a:focus-visible,.tabs a.on{opacity:1;transform:none}.tabs a.on{box-shadow:-3px 0 0 var(--ink) inset}
@media (max-width:1180px){.tabs a{width:130px;padding:6px 8px;gap:6px;font-size:.76rem}}
/* masthead */
.mast{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px;border-bottom:2px solid var(--ink);padding-bottom:12px}
.date{font:700 clamp(2.4rem,6vw,4.2rem)/.9 var(--disp);letter-spacing:-.01em;text-transform:uppercase;margin:0}
.hi{font-family:var(--hand);font-size:1.35rem;color:var(--ink2);margin:6px 0 0}
.tally{display:flex;gap:22px;flex-wrap:wrap}.tally div{text-align:right}.tally b{display:block;font:700 2rem/1 var(--disp)}.tally span{font:.7rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.tally .late b{color:var(--pen)}
/* spread */
.spread{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px 44px;margin-top:22px}
.wheel{width:100%%;height:auto;display:block}
.ring{fill:none;stroke:var(--ink2);stroke-width:1.2;stroke-dasharray:2 5}
.arr{stroke:var(--ink2);stroke-width:1.4;fill:none}
.cur{font:italic 11px var(--body);fill:var(--faint)}
.node .nb{fill:var(--paper);stroke:none}.node .nf{fill:var(--c);opacity:.9}.node .no{fill:none;stroke:var(--c);stroke-width:2.4}
.node .nn{font:700 17px var(--mono);fill:var(--ink)}.node.on .nn{fill:var(--ink)}
.node .nl{font:600 14px var(--body);fill:var(--ink)}.node .sc{font:600 12px var(--mono);fill:var(--faint)}
.node:hover .no{stroke-width:4}
.big{font:700 54px var(--disp);fill:var(--ink)}.big .of{font-size:26px;fill:var(--faint)}.cap{font:11px var(--mono);letter-spacing:.14em;text-transform:uppercase;fill:var(--faint)}
.hand{fill:none;stroke:var(--pen);stroke-width:1.6;stroke-linecap:round}.note{font:20px var(--hand);fill:var(--pen)}
h2{font:700 1.05rem/1 var(--disp);letter-spacing:.08em;text-transform:uppercase;margin:0 0 10px;padding-bottom:8px;border-bottom:1px solid var(--ink)}
h2 .faint{font:400 .72rem var(--mono);letter-spacing:.08em;margin-left:8px}
ul.lines{list-style:none;margin:0;padding:0}
ul.lines li{display:flex;gap:10px;align-items:baseline;padding:7px 0;border-bottom:1px solid var(--grid2);min-height:36px}
.txt{flex:1;min-width:0;overflow-wrap:anywhere}
.box{width:13px;height:13px;border:1.6px solid var(--ink);border-radius:2px;flex:none;transform:translateY(2px)}
li.late .txt{background:linear-gradient(transparent 55%%,color-mix(in srgb,var(--pen) 22%%,transparent) 55%%)}
.pn{font:700 .72rem var(--mono);color:var(--c);border:1.5px solid var(--c);border-radius:50%%;width:22px;height:22px;display:inline-grid;place-items:center;flex:none;transform:translateY(-1px)}
.sz{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}.sz b{font:700 1.5rem var(--disp)}
.ruler{display:grid;grid-template-columns:repeat(var(--n),1fr);align-items:end;height:22px;margin-top:10px;border-bottom:2px solid var(--ink)}
.ruler i{height:8px;border-left:1px solid var(--ink2)}.ruler i:nth-child(7n+1){height:16px}.ruler i.d{border-color:var(--pen)}
.rl{display:flex;justify-content:space-between;font:.75rem var(--mono);color:var(--faint);margin-top:4px}.rl b{color:var(--pen);font-family:var(--hand);font-size:1.05rem}
.side{display:grid;gap:26px;align-content:start}
/* week */
.week{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));border-top:2px solid var(--ink);margin-top:34px}
.wd{border-right:1px solid var(--grid2);padding:8px 10px 14px;min-height:130px}.wd:last-child{border-right:0}
.wh{display:flex;justify-content:space-between;align-items:baseline;font:.72rem var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--faint)}
.wh b{font:700 1.6rem/1 var(--disp);color:var(--ink)}
.wd.today{background:color-mix(in srgb,var(--mark) 40%%,transparent)}.wd.past{opacity:.55}
.wd ul{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:8px;font-size:.85rem}.wd li{display:flex;gap:6px;overflow-wrap:anywhere}
/* lower */
.cols3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px 36px;margin-top:34px}
.cal{display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font:.85rem var(--mono);row-gap:4px}
.cal b{color:var(--faint);font-weight:400;font-size:.7rem}.cal span{position:relative;padding:5px 0 9px}.cal .out{color:var(--faint);opacity:.45}
.cal .now{outline:2px solid var(--pen);outline-offset:-3px;border-radius:50%%;font-weight:700}
.cal i{display:inline-block;width:5px;height:5px;border-radius:50%%;background:var(--c,var(--px));position:relative;top:9px;margin:0 1px}
.gn{font:700 1.3rem/1 var(--disp);color:var(--faint);width:20px}
.ld{font:.78rem var(--mono);color:var(--faint);width:42px;flex:none}.lk{font:.68rem var(--mono);text-transform:uppercase;letter-spacing:.08em;color:var(--ink2);width:58px;flex:none}
footer{margin-top:40px;font:.72rem var(--mono);color:var(--faint);letter-spacing:.06em}
/* pillar page */
.view{display:none}.view .back{font:.8rem var(--mono);text-decoration:none;color:var(--ink2);letter-spacing:.06em}
.ph{display:flex;gap:22px;align-items:center;margin:18px 0 8px;border-bottom:2px solid var(--ink);padding-bottom:14px}
.huge{font:800 clamp(5rem,12vw,9rem)/.8 var(--disp);color:transparent;-webkit-text-stroke:2px var(--c);letter-spacing:-.04em}
.ph h1{font:700 clamp(1.9rem,4vw,2.8rem)/1 var(--disp);text-transform:uppercase;margin:0 0 8px}
.flowline{margin:0;color:var(--ink2)}.flowline a{text-decoration:none;border-bottom:1px solid var(--ink2)}.flowline .hand{font-family:var(--hand);color:var(--c);font-size:1.15rem;fill:none;stroke:none}
.stands{font:500 clamp(1.15rem,2vw,1.45rem)/1.55 var(--body);max-width:62ch;margin:22px 0 0}
.index{margin-top:36px}.index h3{font:700 .95rem var(--disp);letter-spacing:.06em;text-transform:uppercase;margin:18px 0 6px}
ul.toc{list-style:none;margin:0;padding:0}ul.toc li{padding:6px 0;border-bottom:1px dashed var(--grid2)}
ul.toc a{display:flex;align-items:baseline;gap:8px;text-decoration:none}ul.toc .tt{font-weight:600}ul.toc a:hover .tt{color:var(--c)}
.dots{flex:1;border-bottom:2px dotted var(--faint);transform:translateY(-4px)}ul.toc .sum{display:block;color:var(--ink2);font-size:.88rem;padding-right:20%%}
.reader h1{font:700 clamp(1.8rem,4vw,2.6rem)/1.05 var(--disp);margin:6px 0 16px}
.md{max-width:70ch;overflow-wrap:anywhere}.md h3,.md h4,.md h5,.md h6{font:700 .95rem var(--disp);letter-spacing:.06em;text-transform:uppercase;margin:20px 0 6px}
.md p{margin:8px 0}.md ul{margin:6px 0;padding-left:1.2em}.md a{color:var(--c);font-weight:600}.md code{font-family:var(--mono);font-size:.88em}
.srcs{margin-top:26px;border-top:1px solid var(--ink);padding-top:10px;font-size:.88rem;color:var(--ink2)}
body.viewing .home{display:none}
@media (max-width:900px){.spread,.cols3{grid-template-columns:minmax(0,1fr)}.week{grid-template-columns:repeat(2,minmax(0,1fr))}.wd{border-bottom:1px solid var(--grid2)}
.sheet{padding-right:max(16px,4vw);padding-bottom:90px}.tabs{top:auto;bottom:0;right:0;left:0;transform:none;display:flex;overflow-x:auto;gap:2px;padding:4px;background:var(--paper)}
.tabs a{width:auto;border-radius:8px;transform:none}.tabs a span,.tabs a:hover span{display:none}}
@media (prefers-reduced-motion:reduce){.tabs a{transition:none}}
</style></head><body>
<nav class="tabs" aria-label="Pillars">%(tabs)s</nav>
<div class="sheet" id="top">
%(details)s
<div class="home">
  <header class="mast"><div><p class="eyebrow">%(title)s</p><h1 class="date">%(date)s</h1><p class="hi">%(greet)s%(name)s. Here's your life on one page.</p></div>
    <div class="tally"><div><b>%(running)d</b><span>running</span></div><div><b>%(nweek)d</b><span>due this week</span></div><div class="%(latecls)s"><b>%(nover)d</b><span>overdue</span></div><div><b>%(month)d</b><span>captured</span></div></div></header>
  <div class="spread">
    <section><a href="#p-%(start)s" style="text-decoration:none">%(wheel)s</a></section>
    <div class="side">
      <section>%(season)s</section>
      <section><h2>On your plate <span class="faint">overdue + this week</span></h2><ul class="lines todo">%(today)s</ul></section>
      %(later)s
    </div>
  </div>
  <section class="week" id="week">%(week)s</section>
  <div class="cols3">
    <section id="goals"><h2>North star</h2><ul class="lines">%(goals)s</ul></section>
    <section><h2>Focus <span class="faint">by pillar</span></h2><ul class="lines">%(focus)s</ul></section>
    <section id="calendar"><h2>%(monthname)s</h2><div class="cal">%(cal)s</div></section>
    <section id="people"><h2>Keep in touch</h2><ul class="lines">%(people)s</ul></section>
    <section><h2>Studies, work &amp; business</h2><ul class="lines">%(units)s</ul></section>
    <section id="activity"><h2>Log</h2><ul class="lines">%(log)s</ul></section>
  </div>
  <footer>Drawn %(iso)s from the files in this folder · nothing leaves your computer · tap a numbered tab to open a pillar</footer>
</div>
</div>
<script>
function show(){
  var id = decodeURIComponent(location.hash.slice(1)), el = id && document.getElementById(id);
  var v = el && (el.classList.contains("view") ? el : el.closest(".view"));
  document.body.classList.toggle("viewing", !!v);
  document.querySelectorAll(".view").forEach(function (d) { d.style.display = d === v ? "block" : "none"; });
  if (el && !v && id !== "top") { el.scrollIntoView(); } else { window.scrollTo(0, 0); }
  var pid = v ? v.id.replace(/^p-?(\d+).*/, "#p-$1") : "";
  document.querySelectorAll(".tabs a").forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === pid); });
}
window.addEventListener("hashchange", show); show();
</script></body></html>""" % {
    "title": esc(title), "pl": palette_l, "pd": palette_d, "tabs": tabs, "details": pillar_details,
    "date": TODAY.strftime("%a %d %b"), "greet": greet, "name": (", " + esc(owner)) if owner else "",
    "running": running, "nweek": len(this_week), "nover": len(overdue), "latecls": "late" if overdue else "",
    "month": month_count, "start": START or "01", "wheel": flywheel(), "season": season_ruler(),
    "today": today_list, "later": ('<section><h2>Later</h2><ul class="lines todo">%s</ul></section>' % later_list) if later_list else "",
    "week": "".join(week_cols), "goals": goal_lines, "focus": focus_lines, "monthname": TODAY.strftime("%B"),
    "cal": "".join(cal), "people": people_lines,
    "units": unit_lines or '<li class="faint">Studies, a job or a business show here, inside their pillar.</li>',
    "log": log_lines, "iso": TODAY.isoformat(),
}


out = os.path.join(ROOT, "dashboard.html")
if os.path.islink(out):
    sys.exit("dashboard.html is a symlink; not writing through it.")
tmp = out + ".tmp"
fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_NOFOLLOW", 0), 0o600)
with os.fdopen(fd, "w", encoding="utf-8") as f:
    f.write(page)
os.replace(tmp, out)
print(out)
