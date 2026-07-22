"""Tokyo Night palettes + shared SVG helpers.

Storm is the dark mode, Day is the light mode. Every asset in this folder is
built from these two dicts, so changing an accent here changes it everywhere.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, "icons")

STORM = dict(
    bg="#24283b", panel="#1f2335", bar="#1f2335", border="#3b4261",
    fg="#c0caf5", muted="#565f89", dim="#9aa5ce",
    blue="#7aa2f7", cyan="#7dcfff", magenta="#bb9af7",
    green="#9ece6a", orange="#ff9e64", red="#f7768e", yellow="#e0af68",
    chip="#292e42", chipborder="#3b4261",
)
DAY = dict(
    bg="#e1e2e7", panel="#d5d6db", bar="#d5d6db", border="#a8aecb",
    fg="#3760bf", muted="#848cb5", dim="#6172b0",
    blue="#2e7de9", cyan="#007197", magenta="#9854f1",
    green="#587539", orange="#b15c00", red="#f52a65", yellow="#8c6c3e",
    chip="#c9cddc", chipborder="#a8aecb",
)
MODES = (("dark", STORM), ("light", DAY))

MONO = "ui-monospace,'JetBrains Mono','SFMono-Regular',Menlo,Consolas,monospace"
CW = 8.4  # approx advance width of the mono stack at font-size 14


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_cache = {}


def icon(slug, x, y, size, color, opacity="1"):
    """Inline a Simple Icons glyph (24x24 viewBox) at (x, y), scaled to `size`."""
    if slug not in _cache:
        with open(os.path.join(ICONS, f"{slug}.svg")) as f:
            src = f.read()
        _cache[slug] = re.findall(r'<path[^>]*\bd="([^"]+)"', src)
    s = size / 24.0
    return "".join(
        f'<path d="{d}" fill="{color}" fill-opacity="{opacity}" '
        f'transform="translate({x:.2f},{y:.2f}) scale({s:.4f})"/>'
        for d in _cache[slug])


def chevron(x, y, color, size=13, weight=2.2):
    """A drawn prompt chevron — no font-fallback roulette on `❯`."""
    h = size / 2
    return (f'<polyline points="{x},{y-h} {x+size*0.52},{y} {x},{y+h}" fill="none" '
            f'stroke="{color}" stroke-width="{weight}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def card(w, h, c, extra=""):
    """Opening tag + rounded panel shared by every asset."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{extra}">'
            f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="{c["bg"]}" '
            f'stroke="{c["border"]}" stroke-width="1.5"/>')


def write(name, mode, svg):
    path = os.path.join(HERE, f"{name}-{mode}.svg")
    with open(path, "w") as f:
        f.write(svg)
    print("wrote", os.path.relpath(path, os.path.dirname(HERE)))
