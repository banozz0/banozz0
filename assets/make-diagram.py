"""Draws the "What I run" diagram as one SVG per GitHub theme.

Run: python3 assets/make-diagram.py  ->  assets/agents-light.svg, assets/agents-dark.svg,
and the README's diagram block between its markers (toggle title and alt text come from
the same content). Icons are Lucide (ISC licence). Text uses the system font stack,
because an SVG shown through <img> cannot load web fonts.
"""
from collections import namedtuple
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
README = OUT.parent / "README.md"
START, END = "<!-- diagram:start -->", "<!-- diagram:end -->"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
TITLE = "How a job moves from spec to done"

# GitHub Primer values, so the diagram sits on the page like native UI.
THEMES = {
    "light": dict(page="#ffffff", card="#f6f8fa", border="#d1d9e0", fg="#1f2328", muted="#59636e",
                  line="#818b98", blue="#0969da", orange="#bc4c00", green="#1a7f37",
                  violet="#8250df", red="#cf222e", done="#1f883d"),
    "dark": dict(page="#0d1117", card="#151b23", border="#3d444d", fg="#f0f6fc", muted="#9198a1",
                 line="#656c76", blue="#4493f8", orange="#f0883e", green="#3fb950",
                 violet="#ab7df8", red="#f85149", done="#238636"),
}

ICONS = {
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "board": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M8 7v7"/><path d="M12 7v4"/><path d="M16 7v9"/>',
    "bot": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/>'
           '<path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "code": '<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>',
    "flask": '<path d="M10 2v7.527a2 2 0 0 1-.211.896L4.72 20.55a1 1 0 0 0 .9 1.45h12.76a1 1 0 0 0 .9-1.45'
             'l-5.069-10.127A2 2 0 0 1 14 9.527V2"/><path d="M8.5 2h7"/><path d="M7 16h10"/>',
    "eye": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/>'
           '<path d="M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="1"/>'
           '<path d="M18.944 12.33a1 1 0 0 0 0-.66 7.5 7.5 0 0 0-13.888 0 1 1 0 0 0 0 .66 7.5 7.5 0 0 0 13.888 0"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
}

# The content. Order is the flow; change words here, never in the SVGs.
# Subtitle lists are display lines; a group's two lines read as one phrase.
# A group has rows (a crew list) or none (drawn as the workers window).
Spec = namedtuple("Spec", "icon hue title sub rows", defaults=[None])
ME = Spec("user", "fg", "Me", ["Specs, decisions, approvals"])
BOARD = Spec("board", "fg", "Shared task board", ["Every job is a card"])
HERMES = Spec("bot", "blue", "Hermes agents", ["Always on, reachable from", "Discord and Telegram"],
              [("Harry", "planning and triage"), ("Dobby", "runs the system"),
               ("Researcher", "sourced research"), ("Content", "drafts posts")])
BUILDERS = Spec("code", "orange", "Builders", ["Claude Code workers in Ghostex", "build and document"])
TESTED = Spec("flask", "green", "Tested", ["Tests, builds, checked in the real app"])
REVIEWED = Spec("eye", "violet", "Reviewed", ["A separate reviewer agent checks every finished card"])
FAIL = ["Failed test or review:", "back to the board"]

# Layout. Every coordinate below derives from these.
W, M = 792, 24                  # canvas width, outer margin
CX = (M + W - 56) / 2           # spine x; the right 56px hold the send-back rail
RAIL = W - M                    # send-back rail x
STAGE_W, STAGE_H = 440, 64      # single-stage cards
COL_GAP = 16
COL_W = CX - M - COL_GAP / 2
PAD, TILE, INNER_R = 12, 40, 6  # card padding, icon tile, radius of tiles and rows
R = INNER_R + PAD               # card radius, concentric with what sits inside
ICON = 20                       # Lucide's 24px icons, drawn at this size
ICON_INSET = (TILE - ICON) / 2
TEXT_X = PAD + TILE + 12        # title and subtitle start, from the card's left edge
TITLE_Y, SUB_Y, LINE = 30, 49, 17
ROW_H, ROW_GAP = 34, 6
WORKERS_MIN_H = 120             # the workers window never shrinks below four skeleton lines
GAP = 36                        # between stacked stages
SPLIT = 48                      # room for the split and merge elbows
CORNER = 10                     # connector corner radius
DONE_W, DONE_H = 132, 44        # the Done pill


def text(x, y, s, size, weight, fill, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return (f'<text x="{x:g}" y="{y:g}" font-size="{size}" font-weight="{weight}" fill="{fill}"'
            f'{a}>{escape(s)}</text>')


def rect(x, y, w, h, rx, fill=None, stroke=None, extra=""):
    f = f' fill="{fill}"' if fill else ""
    s = f' stroke="{stroke}"' if stroke else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}"{f}{s}{extra}/>'


def icon(x, y, name, color, width):
    """A 24px Lucide icon drawn at ICON px with its top-left at (x, y)."""
    return (f'<g transform="translate({x:g} {y:g}) scale({ICON / 24:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def header(x, y, spec, t):
    c = t[spec.hue]
    out = [rect(x + PAD, y + PAD, TILE, TILE, INNER_R, c, extra=' fill-opacity="0.12"'),
           icon(x + PAD + ICON_INSET, y + PAD + ICON_INSET, spec.icon, c, 2.1),
           text(x + TEXT_X, y + TITLE_Y, spec.title, 15, 600, t["fg"])]
    out += [text(x + TEXT_X, y + SUB_Y + i * LINE, s, 13, 400, t["muted"]) for i, s in enumerate(spec.sub)]
    return out


def stage(y, spec, t):
    x = CX - STAGE_W / 2
    return [rect(x, y, STAGE_W, STAGE_H, R, t["card"], t["border"]), *header(x, y, spec, t)]


def group(x, y, h, spec, t):
    c = t[spec.hue]
    out = [rect(x, y, COL_W, h, R, t["card"], t["border"]),
           rect(x, y, COL_W, h, R, c, c, ' fill-opacity="0.05" stroke-opacity="0.45"'),
           *header(x, y, spec, t)]
    ry = y + group_head(spec)
    if spec.rows is None:
        return out + workers(x + PAD, ry, COL_W - 2 * PAD, y + h - PAD - ry, c, t)
    for who, role in spec.rows:
        out += [rect(x + PAD, ry, COL_W - 2 * PAD, ROW_H, INNER_R, t["page"], t["border"]),
                f'<circle cx="{x + PAD + 14:g}" cy="{ry + ROW_H / 2:g}" r="3" fill="{c}"/>',
                text(x + PAD + 26, ry + 22, who, 13, 600, t["fg"]),
                text(x + PAD + 112, ry + 22, role, 13, 400, t["muted"])]
        ry += ROW_H + ROW_GAP
    return out


def workers(x, y, w, h, c, t):
    """A Ghostex window with three Claude Code worker panes side by side."""
    bar, pw, first, pitch = 24, w / 3, 16, 16      # title bar, pane width, prompt line offset, skeleton pitch
    out = [rect(x, y, w, h, INNER_R, t["page"], t["border"]), f'<path d="M{x:g} {y + bar:g}H{x + w:g}" stroke="{t["border"]}"/>']
    out += [f'<circle cx="{x + 12 + i * 10:g}" cy="{y + bar / 2:g}" r="3" fill="{t["border"]}"/>' for i in range(3)]
    widths = (0.82, 0.55, 0.7, 0.4, 0.9, 0.6, 0.45, 0.75)
    ly = y + bar + first
    n = int((y + h - 14 - (ly + first + 1)) // pitch) + 1   # skeleton lines that fit above the bottom inset
    skeleton = []
    for i in range(3):
        px = x + i * pw
        if i:
            out.append(f'<path d="M{px:g} {y + bar:g}V{y + h:g}" stroke="{t["border"]}"/>')
        out.append(f'<path d="M{px + 12:g} {ly - 4:g}l4 4-4 4" fill="none" stroke="{c}" stroke-width="1.6" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
        out.append(rect(px + 22, ly - 3, (pw - 34) * 0.6, 6, 3, c, extra=' fill-opacity="0.55"'))
        skeleton += [rect(px + 12, ly + first + 1 + k * pitch, (pw - 24) * widths[(k * 3 + i * 2) % len(widths)], 6, 3)
                     for k in range(n)]
    return out + [f'<g fill="{t["muted"]}" fill-opacity="0.28">' + "".join(skeleton) + "</g>"]


def group_head(spec):
    return SUB_Y + (len(spec.sub) - 1) * LINE + 16


def group_h(spec):
    rows = spec.rows
    body = WORKERS_MIN_H if rows is None else len(rows) * ROW_H + (len(rows) - 1) * ROW_GAP
    return group_head(spec) + body + PAD


def elbow(x1, y1, x2, y2, r=CORNER):
    """Down from (x1,y1), across at the midpoint height, down to 1px above (x2,y2) so the
    arrowhead covers the end, rounded corners."""
    y2 -= 1
    if x1 == x2:
        return f'M{x1:g} {y1:g}V{y2:g}'
    ym, s = (y1 + y2) / 2, 1 if x2 > x1 else -1
    return (f'M{x1:g} {y1:g}V{ym - r:g}Q{x1:g} {ym:g} {x1 + s * r:g} {ym:g}'
            f'H{x2 - s * r:g}Q{x2:g} {ym:g} {x2:g} {ym + r:g}V{y2:g}')


def arrow_down(x, y, c):
    return f'<path d="M{x - 5:g} {y - 7:g}L{x:g} {y:g}L{x + 5:g} {y - 7:g}Z" fill="{c}"/>'


def arrow_left(x, y, c):
    return f'<path d="M{x + 7:g} {y - 5:g}L{x:g} {y:g}L{x + 7:g} {y + 5:g}Z" fill="{c}"/>'


def build(t):
    line = t["line"]
    y_me = M
    y_board = y_me + STAGE_H + GAP
    y_cols = y_board + STAGE_H + SPLIT
    col_h = max(group_h(HERMES), group_h(BUILDERS))
    y_test = y_cols + col_h + SPLIT
    y_rev = y_test + STAGE_H + GAP
    y_done = y_rev + STAGE_H + GAP
    H = y_done + DONE_H + M
    lx, rx = M, M + COL_W + COL_GAP
    lc, rc = lx + COL_W / 2, rx + COL_W / 2
    sx = CX + STAGE_W / 2           # right edge of the stage cards

    paths = [elbow(CX, y_me + STAGE_H, CX, y_board),
             elbow(CX, y_board + STAGE_H, lc, y_cols), elbow(CX, y_board + STAGE_H, rc, y_cols),
             elbow(lc, y_cols + col_h, CX, y_test), elbow(rc, y_cols + col_h, CX, y_test),
             elbow(CX, y_test + STAGE_H, CX, y_rev), elbow(CX, y_rev + STAGE_H, CX, y_done)]
    flow = [f'<path d="{d}" fill="none" stroke="{line}" stroke-width="1.5"/>' for d in paths]
    flow += [arrow_down(CX, y, line) for y in (y_board, y_test, y_rev, y_done)]
    flow += [arrow_down(x, y_cols, line) for x in (lc, rc)]

    # Send-back rail: out of Tested and Reviewed, up the right side, into the board.
    red, r = t["red"], CORNER
    yb, yt, yr = y_board + STAGE_H / 2, y_test + STAGE_H / 2, y_rev + STAGE_H / 2
    rail = (f'M{sx:g} {yr:g}H{RAIL - r:g}Q{RAIL:g} {yr:g} {RAIL:g} {yr - r:g}V{yb + r:g}'
            f'Q{RAIL:g} {yb:g} {RAIL - r:g} {yb:g}H{sx + 1:g}M{sx:g} {yt:g}H{RAIL:g}')
    back = [f'<path d="{rail}" fill="none" stroke="{red}" stroke-width="1.5" stroke-dasharray="5 4"/>',
            arrow_left(sx, yb, red)]
    back += [text(RAIL - 12, (yt + yr) / 2 - 2 + i * LINE, s, 12, 500 if i == 0 else 400, red, "end")
             for i, s in enumerate(FAIL)]

    cards = [*stage(y_me, ME, t), *stage(y_board, BOARD, t),
             *group(lx, y_cols, col_h, HERMES, t), *group(rx, y_cols, col_h, BUILDERS, t),
             *stage(y_test, TESTED, t), *stage(y_rev, REVIEWED, t)]
    dx = CX - DONE_W / 2
    ix = dx + 30                    # check icon, then the label 6px after it
    done = [rect(dx, y_done, DONE_W, DONE_H, DONE_H / 2, t["done"]),
            icon(ix, y_done + (DONE_H - ICON) / 2, "check", "#ffffff", 2.4),
            text(ix + ICON + 6, y_done + 28, "Done", 15, 600, "#ffffff")]

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:g}" viewBox="0 0 {W} {H:g}" '
            f'role="img" aria-label="{TITLE}" font-family="{FONT}">\n<title>{TITLE}</title>\n'
            + "\n".join(back + flow + cards + done) + "\n</svg>\n")


def alt_text():
    say = lambda spec: f"{spec.title}: {' '.join(spec.sub)}"
    crew = "; ".join(f"{who}: {role}" for who, role in HERMES.rows)
    return (f"{TITLE}. 1. {say(ME)}. 2. {say(BOARD)}. 3. In parallel, {say(HERMES)} ({crew}); "
            f"and {say(BUILDERS)}. 4. {say(TESTED)}. 5. {say(REVIEWED)}. 6. Done. {' '.join(FAIL)}.")


def readme_block():
    """The README's toggle, closed by default; <picture> swaps in the dark SVG on dark themes."""
    return (f'{START}\n<details>\n<summary><b>{TITLE}</b></summary>\n\n<picture>\n'
            f'  <source media="(prefers-color-scheme: dark)" srcset="assets/agents-dark.svg">\n'
            f'  <img alt="{escape(alt_text(), {chr(34): "&quot;"})}" src="assets/agents-light.svg">\n'
            f'</picture>\n</details>\n{END}')


if __name__ == "__main__":
    for name, theme in THEMES.items():
        (OUT / f"agents-{name}.svg").write_text(build(theme))
        print(OUT / f"agents-{name}.svg")
    head, rest = README.read_text().split(START)
    README.write_text(head + readme_block() + rest.split(END)[1])
    print(README)
