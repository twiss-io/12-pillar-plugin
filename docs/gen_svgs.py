"""Generate the animated README SVGs for 12-pillar-plugin: flywheel.svg and onboarding.svg."""
import math, sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]

STYLE = """
<style>
  .txt { fill: #1f2328; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  .mut { fill: #59636e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
  .ring { stroke: #d0d7de; }
  .node { fill: #f6f8fa; stroke: #afb8c1; }
  .card { fill: #ffffff; stroke: #d0d7de; }
  .panel { fill: #f6f8fa; stroke: #d0d7de; }
  .chip { fill: #eaeef2; }
  @media (prefers-color-scheme: dark) {
    .txt { fill: #e6edf3; }
    .mut { fill: #9198a1; }
    .ring { stroke: #3d444d; }
    .node { fill: #151b23; stroke: #3d444d; }
    .card { fill: #0d1117; stroke: #3d444d; }
    .panel { fill: #151b23; stroke: #3d444d; }
    .chip { fill: #262c36; }
  }
</style>
"""
ACCENT = "#E8833A"


def show(t_in, t_out, T, fade=0.35):
    """Opacity animation: hidden, fade in at t_in, visible, fade out at t_out, hidden."""
    k = [0, t_in, t_in + fade, t_out - fade, t_out, T]
    k = [round(x / T, 4) for x in k]
    return (f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="{";".join(map(str, k))}"/>')


# ---------------------------------------------------------------- flywheel
def flywheel():
    W = H = 800
    cx, cy, R = 400, 400, 230
    T = 12
    pillars = ["Faith", "Identity", "Time", "Health", "Development", "Relationships",
               "Career", "Brand", "Opportunities", "Finance", "Lifestyle", "Legacy"]
    gives = ["direction", "clarity", "allocation", "capacity", "skill", "access",
             "credibility", "opportunity", "finance", "lifestyle", "legacy", "back to faith"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'role="img" aria-label="The 12-Pillar Life Flywheel: each pillar feeds the next, in a loop">', STYLE]
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" class="ring" stroke-width="2"/>')
    # direction chevrons + currency labels between nodes
    for i in range(12):
        a = math.radians(-90 + i * 30 + 15)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        rot = math.degrees(a) + 90
        o.append(f'<path d="M -6 -6 L 2 0 L -6 6" transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})" '
                 f'fill="none" class="ring" stroke-width="2.5" stroke-linecap="round"/>')
        lx, ly = cx + (R - 42) * math.cos(a), cy + (R - 42) * math.sin(a)
        o.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" font-size="13" class="mut" font-style="italic">{gives[i]}</text>')
        o.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" text-anchor="middle" font-size="13" fill="{ACCENT}" font-weight="700" '
                 f'font-style="italic" font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif" opacity="0">{gives[i]}'
                 f'<animate attributeName="opacity" dur="{T}s" begin="{i + 0.5}s" repeatCount="indefinite" '
                 f'values="0;1;1;0;0" keyTimes="0;0.03;0.07;0.12;1"/></text>')
    # nodes
    for i, name in enumerate(pillars):
        a = math.radians(-90 + i * 30)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        o.append(f'<g>')
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26" class="node" stroke-width="2"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="26" fill="{ACCENT}" opacity="0">'
                 f'<animate attributeName="opacity" dur="{T}s" begin="{i}s" repeatCount="indefinite" '
                 f'values="0;1;1;0;0" keyTimes="0;0.03;0.07;0.15;1"/></circle>')
        o.append(f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-size="17" font-weight="700" class="txt">{i + 1}</text>')
        c = math.cos(a)
        anchor = "start" if c > 0.3 else "end" if c < -0.3 else "middle"
        lx, ly = cx + (R + 42) * math.cos(a), cy + (R + 42) * math.sin(a) + 6
        if anchor == "middle":
            ly += 6 if math.sin(a) > 0 else -2
        o.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-size="17" font-weight="600" class="txt">{name}</text>')
        o.append('</g>')
    # travelling dot
    path = f"M {cx} {cy - R} A {R} {R} 0 1 1 {cx - 0.01} {cy - R} Z"
    o.append(f'<circle r="8" fill="{ACCENT}"><animateMotion dur="{T}s" repeatCount="indefinite" path="{path}"/></circle>')
    # centre text, alternating messages
    o.append(f'<text x="{cx}" y="{cy - 40}" text-anchor="middle" font-size="22" font-weight="700" class="txt">The 12-Pillar Flywheel</text>')
    msgs = [("Each pillar gives the next", "what it runs on."),
            ("Stuck somewhere?", "Look one or two pillars upstream."),
            ("Start where it hurts.", "Momentum carries the rest.")]
    for j, (a1, a2) in enumerate(msgs):
        t0 = j * 4 + 0.1
        o.append(f'<g opacity="0">{show(t0, t0 + 3.8, T)}'
                 f'<text x="{cx}" y="{cy + 2}" text-anchor="middle" font-size="16" class="mut">{escape(a1)}</text>'
                 f'<text x="{cx}" y="{cy + 26}" text-anchor="middle" font-size="16" class="mut">{escape(a2)}</text></g>')
    o.append('</svg>')
    return "\n".join(o)


# ---------------------------------------------------------------- onboarding
def onboarding():
    W, H = 800, 420
    T = 20
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'role="img" aria-label="Setup walkthrough: choose full or quick start; tell it who you are; your job, studies and business go inside their pillars; then the AI learns as you go">', STYLE]
    o.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" class="card" stroke-width="1.5"/>')
    o.append(f'<path d="M1 13 a12 12 0 0 1 12 -12 H{W - 13} a12 12 0 0 1 12 12 V40 H1 Z" class="panel"/>')
    for k, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        o.append(f'<circle cx="{24 + k * 20}" cy="21" r="6" fill="{col}"/>')
    o.append(f'<text x="{W / 2}" y="26" text-anchor="middle" font-size="13" class="mut">~/my-life — claude</text>')

    def t(x, y, s, size=16, cls="txt", weight="400", extra=""):
        return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" class="{cls}" {extra}>'
                f'{escape(s)}</text>')

    def scene(t0, t1, body):
        return f'<g opacity="0">{show(t0, t1, T)}{body}</g>'

    def appear(t0, t1, body):  # element that appears inside a scene at t0
        return f'<g opacity="0">{show(t0, t1, T, 0.25)}{body}</g>'

    # step label chips
    steps = ["1 · Choose", "2 · Who you are", "3 · Your pillars", "4 · Learns as you go"]
    spans = [(0.2, 5), (5, 9.5), (9.5, 14.5), (14.5, 19.8)]
    for k, (lab, (a, b)) in enumerate(zip(steps, spans)):
        x = 30 + k * 190
        o.append(f'<rect x="{x}" y="56" width="176" height="28" rx="14" class="chip"/>')
        o.append(f'<rect x="{x}" y="56" width="176" height="28" rx="14" fill="{ACCENT}" opacity="0">{show(a, b, T, 0.2)}</rect>')
        o.append(f'<text x="{x + 88}" y="75" text-anchor="middle" font-size="13" font-weight="600" class="txt">{lab}</text>')

    y0 = 125
    # scene 1: command + three choices
    s = [t(36, y0, "> /12-pillars:setup", 17, "txt mono", "600"),
         appear(1.0, 5, t(36, y0 + 42, "How do you want to start?", 17, "txt", "600"))]
    opts = [("Full setup", "~30–40 min: who you are, your days, one pillar"),
            ("Quick start", "~5 min: who you are and your days, learn the rest")]
    for k, (a, b) in enumerate(opts):
        yy = y0 + 70 + k * 52
        body = (f'<rect x="36" y="{yy}" width="560" height="42" rx="8" class="panel" stroke-width="1.5"/>'
                + t(56, yy + 27, a, 16, "txt", "600") + t(190, yy + 27, b, 14, "mut"))
        if k == 1:
            body += (f'<rect x="36" y="{yy}" width="560" height="42" rx="8" fill="none" stroke="{ACCENT}" '
                     f'stroke-width="2.5" opacity="0">{show(3.2, 5, T, 0.2)}</rect>')
        s.append(appear(1.4 + k * 0.4, 5, body))
    o.append(scene(0.2, 5, "".join(s)))

    # scene 2: identity first
    qa = [("Who are you, in a sentence or two?", "Final-year student, tech lead, building a brand."),
          ("Where do you want to be in 3–5 years?", "Leading engineering, my own studio on the side.")]
    s = []
    for k, (q, a) in enumerate(qa):
        yy = y0 + k * 100
        s.append(appear(5.2 + k * 1.6, 9.5, t(36, yy, q, 17, "txt", "600")))
        s.append(appear(5.8 + k * 1.6, 9.5, t(56, yy + 32, "> " + a, 15, "mut mono")))
    s.append(appear(8.4, 9.5, f'<rect x="36" y="{y0 + 196}" width="520" height="38" rx="8" fill="{ACCENT}"/>'
                    + t(56, y0 + 221, "✓ 02-identity: north star written, running", 15, "txt", "700", 'style="fill:#fff"')))
    o.append(scene(5, 9.5, "".join(s)))

    # scene 3: recommended tree
    tree = [("01 … 12", 0, "your 12 pillars, the whole brain"), ("05-development/nus/", 0, "your studies"),
            ("07-career/twiss/", 0, "your job · clients, projects"), ("09-opportunities/side-shop/", 0, "a business you run"),
            ("raw/  actions.md", 0, "sources · every deadline")]
    s = [t(36, y0, "Studies, a job + a side shop? Here's the plan:", 17, "txt", "600")]
    for k, (a, ind, why) in enumerate(tree):
        yy = y0 + 40 + k * 36
        body = t(56 + ind * 26, yy, a, 16, "txt mono")
        if why:
            body += t(380, yy, "← " + why, 14, "mut")
        s.append(appear(10.0 + k * 0.45, 14.5, body))
    s.append(appear(12.6, 14.5, f'<rect x="36" y="{y0 + 228}" width="200" height="38" rx="8" fill="{ACCENT}"/>'
                    + t(56, y0 + 253, "✓ Create it", 16, "txt", "700", 'style="fill:#fff"')))
    o.append(scene(9.5, 14.5, "".join(s)))

    # scene 4: learns as you go
    s = [t(36, y0, "> help me reply to this client email", 17, "txt mono", "600"),
         t(36, y0 + 30, "(keep it short, exams until Dec 4 and I quit coffee lol)", 15, "mut mono"),
         appear(16.0, 19.8,
                f'<rect x="36" y="{y0 + 60}" width="700" height="132" rx="10" class="panel" stroke-width="1.5"/>'
                + t(56, y0 + 90, "Done. I also picked up 2 things about you:", 16, "txt", "600")
                + t(70, y0 + 120, "• Exam season until Dec 4  → 02-identity/now.md, Time", 15)
                + t(70, y0 + 148, "• Quit coffee  → Health pillar", 15)
                + t(56, y0 + 178, "File them?  [yes]", 15, "mut")),
         appear(17.6, 19.8, f'<rect x="36" y="{y0 + 210}" width="420" height="38" rx="8" fill="{ACCENT}"/>'
                + t(56, y0 + 235, "✓ Filed. Your pillars keep filling in.", 15, "txt", "700", 'style="fill:#fff"'))]
    o.append(scene(14.5, 19.8, "".join(s)))
    o.append('</svg>')
    return "\n".join(o)


open(f"{OUT}/flywheel.svg", "w").write(flywheel())
open(f"{OUT}/onboarding.svg", "w").write(onboarding())
print("ok")
