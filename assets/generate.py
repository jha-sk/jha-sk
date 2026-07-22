#!/usr/bin/env python3
"""Render the static profile assets (banner, stack, link chips) in both modes.

    python assets/generate.py

Brand marks are Simple Icons paths, inlined from ./icons (no external requests)
and recoloured to the Tokyo Night accent of their group, so the whole page reads
as one system rather than a pile of vendor logos.
"""
import re

from theme import MODES, MONO, card, chevron, esc, icon, write


# --------------------------------------------------------------------------- banner
def banner(c):
    W, H = 880, 258
    p = [card(W, H, c, "Sourabh Jha - AI Engineer"),
         '<defs><linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">'
         f'<stop offset="0%" stop-color="{c["magenta"]}" stop-opacity=".16"/>'
         f'<stop offset="55%" stop-color="{c["blue"]}" stop-opacity=".06"/>'
         f'<stop offset="100%" stop-color="{c["cyan"]}" stop-opacity=".13"/>'
         '</linearGradient></defs>',
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#glow)"/>',
         f'<path d="M1 15a14 14 0 0 1 14-14h{W-30}a14 14 0 0 1 14 14v23H1z" fill="{c["bar"]}"/>',
         f'<line x1="1" y1="38" x2="{W-1}" y2="38" stroke="{c["border"]}" stroke-width="1"/>']
    for i, col in enumerate((c["red"], c["yellow"], c["green"])):
        p.append(f'<circle cx="{24 + i*20}" cy="20" r="6" fill="{col}"/>')
    p.append(f'<text x="{W/2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" '
             f'fill="{c["muted"]}">jha-sk — ~/ai-engineering — zsh</text>')
    p.append(icon("anthropic", W - 190, 74, 150, c["magenta"], opacity=".07"))

    x, y, lh = 32, 82, 30

    def line(parts, yy):
        out = [f'<text x="{x}" y="{yy}" xml:space="preserve" font-family="{MONO}" font-size="15">']
        for txt, col, weight in parts:
            out.append(f'<tspan fill="{col}" font-weight="{weight}">{esc(txt)}</tspan>')
        p.append("".join(out) + '</text>')

    p.append(chevron(x + 1, y - 5, c["green"]))
    line([("     whoami", c["fg"], 500)], y)
    line([("Sourabh Jha", c["magenta"], 700), ("  ::  ", c["muted"], 400),
          ("AI Engineer", c["cyan"], 600)], y + lh)
    p.append(chevron(x + 1, y + lh * 2 + 5, c["green"]))
    line([("     cat  focus.txt", c["fg"], 500)], y + lh * 2 + 10)
    p.append(f'<line x1="{x}" y1="{y + lh*2 + 22}" x2="{x + 300}" y2="{y + lh*2 + 22}" '
             f'stroke="{c["border"]}" stroke-width="1"/>')

    fy, fx = y + lh * 3 + 14, x
    focus = [("langchain", "LLM systems", c["blue"]), ("qdrant", "RAG", c["orange"]),
             ("ray", "agents", c["green"]), ("weightsandbiases", "evals", c["yellow"]),
             ("vllm", "inference @ scale", c["cyan"])]
    for slug, label, col in focus:
        p.append(icon(slug, fx, fy - 12, 15, col))
        p.append(f'<text x="{fx + 21}" y="{fy}" font-family="{MONO}" font-size="14" '
                 f'font-weight="600" fill="{col}">{esc(label)}</text>')
        fx += 21 + int(len(label) * 8.4) + 26

    p.append(chevron(x + 1, fy + lh - 1, c["green"]))
    p.append(f'<rect x="{x + 22}" y="{fy + lh - 9}" width="9" height="16" fill="{c["blue"]}">'
             '<animate attributeName="opacity" values="1;1;0;0" dur="1.1s" repeatCount="indefinite"/>'
             '</rect>')
    return "".join(p) + '</svg>'


# --------------------------------------------------------------------------- stack
GROUPS = [
    ("code", "blue", "python", [
        ("Python", "python"), ("TypeScript", "typescript"), ("Go", "go"),
        ("Rust", "rust"), ("SQL", "postgresql")]),
    ("llm / genai", "magenta", "claude", [
        ("PyTorch", "pytorch"), ("Transformers", "huggingface"), ("LangGraph", "langchain"),
        ("Claude API", "claude"), ("OpenAI", "openai"), ("vLLM", "vllm")]),
    ("retrieval / data", "cyan", "duckdb", [
        ("pgvector", "postgresql"), ("Qdrant", "qdrant"), ("Redis", "redis"),
        ("DuckDB", "duckdb"), ("Airflow", "apacheairflow"), ("Kafka", "apachekafka")]),
    ("serving / ops", "green", "kubernetes", [
        ("FastAPI", "fastapi"), ("Ray", "ray"), ("Docker", "docker"),
        ("Kubernetes", "kubernetes"), ("AWS", "amazonaws"), ("Terraform", "terraform"),
        ("W&B", "weightsandbiases")]),
]


def stack(c):
    W = 880
    pad_x, gap, chip_h, row_gap, label_w = 26, 8, 30, 14, 156
    y = 26
    body = []
    for name, colkey, licon, items in GROUPS:
        col = c[colkey]
        body.append(icon(licon, pad_x, y + 7, 15, col))
        body.append(f'<text x="{pad_x + 22}" y="{y + 20}" font-family="{MONO}" font-size="13" '
                    f'font-weight="700" fill="{col}">{esc(name)}</text>')
        cx = pad_x + label_w
        for label, slug in items:
            w = int(len(label) * 7.3) + 42
            if cx + w > W - pad_x:
                cx, y = pad_x + label_w, y + chip_h + 7
            body.append(f'<rect x="{cx}" y="{y}" width="{w}" height="{chip_h}" rx="8" '
                        f'fill="{c["chip"]}" stroke="{c["chipborder"]}" stroke-width="1"/>')
            body.append(icon(slug, cx + 11, y + 8, 14, col))
            body.append(f'<text x="{cx + 31}" y="{y + 19.5}" font-family="{MONO}" '
                        f'font-size="12.5" fill="{c["fg"]}">{esc(label)}</text>')
            cx += w + gap
        y += chip_h + row_gap + 5
    return card(W, y + 10, c, "Tech stack") + "".join(body) + "</svg>"


# --------------------------------------------------------------------------- link chips
SOCIALS = [
    ("GitHub", "github", "blue"),
    ("LinkedIn", "linkedin", "cyan"),
    ("X", "x", "magenta"),
    ("Hugging Face", "huggingface", "orange"),
    ("Email", "gmail", "green"),
]


def social_chip(c, label, slug, colkey):
    """One standalone chip per link, so each can carry its own href in the README."""
    h, W = 36, int(len(label) * 7.3) + 46
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" '
            f'viewBox="0 0 {W} {h}" role="img" aria-label="{esc(label)}">'
            f'<rect x="0.75" y="0.75" width="{W-1.5}" height="{h-1.5}" rx="9" '
            f'fill="{c["chip"]}" stroke="{c["chipborder"]}" stroke-width="1.5"/>'
            + icon(slug, 13, 11, 15, c[colkey])
            + f'<text x="35" y="23" font-family="{MONO}" font-size="13" font-weight="600" '
              f'fill="{c["fg"]}">{esc(label)}</text></svg>')


if __name__ == "__main__":
    for mode, palette in MODES:
        write("banner", mode, banner(palette))
        write("stack", mode, stack(palette))
        for label, slug, colkey in SOCIALS:
            key = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
            write(f"social-{key}", mode, social_chip(palette, label, slug, colkey))
