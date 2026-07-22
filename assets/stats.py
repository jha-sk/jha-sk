#!/usr/bin/env python3
"""Render the GitHub stats card from the GraphQL API, in both Tokyo Night modes.

    GITHUB_TOKEN=... python assets/stats.py            # live data
    python assets/stats.py --demo                      # placeholder data

Run by .github/workflows/profile-assets.yml on a schedule. Self-hosted on purpose:
the public github-readme-stats deployment goes down often enough that a profile
depending on it renders as broken images.
"""
import json
import os
import sys
import urllib.request

from theme import MODES, MONO, card, esc, icon, write

USER = os.environ.get("PROFILE_USER", "jha-sk")
API = "https://api.github.com/graphql"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
    }
    pullRequests(states: MERGED) { totalCount }
    issues { totalCount }
    followers { totalCount }
    repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, ISSUE]) { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false,
                 orderBy: {field: STARGAZERS, direction: DESC}) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""

DEMO = dict(
    commits=1284, stars=342, prs=96, issues=57, reviews=73, contributed=18,
    followers=112, repos=41,
    langs=[("Python", 46.2), ("TypeScript", 21.4), ("Go", 12.8),
           ("Rust", 8.1), ("SQL", 6.3), ("Other", 5.2)],
)

# Languages get a stable accent so the bar and the legend always agree.
LANG_ACCENT = ["blue", "magenta", "cyan", "green", "orange", "yellow", "red", "muted"]


def fetch(token):
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {token}",
                 "Content-Type": "application/json",
                 "User-Agent": f"{USER}-profile-assets"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    u = payload["data"]["user"]
    cc = u["contributionsCollection"]

    sizes = {}
    for repo in u["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            sizes[edge["node"]["name"]] = sizes.get(edge["node"]["name"], 0) + edge["size"]
    total = sum(sizes.values()) or 1
    ranked = sorted(sizes.items(), key=lambda kv: -kv[1])
    langs = [(n, round(s * 100 / total, 1)) for n, s in ranked[:5]]
    rest = round(100 - sum(p for _, p in langs), 1)
    if rest > 0.1:
        langs.append(("Other", rest))

    return dict(
        commits=cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        stars=sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),
        prs=u["pullRequests"]["totalCount"],
        issues=u["issues"]["totalCount"],
        reviews=cc["totalPullRequestReviewContributions"],
        contributed=u["repositoriesContributedTo"]["totalCount"],
        followers=u["followers"]["totalCount"],
        repos=u["repositories"]["totalCount"],
        langs=langs,
    )


def human(n):
    if n >= 10_000:
        return f"{n/1000:.1f}k".replace(".0k", "k")
    return f"{n:,}"


def render(c, d):
    W, H = 880, 250
    mid = 448
    p = [card(W, H, c, f"GitHub statistics for {USER}")]

    # header ------------------------------------------------------------------
    p.append(icon("github", 26, 22, 17, c["magenta"]))
    p.append(f'<text x="52" y="36" font-family="{MONO}" font-size="14" font-weight="700" '
             f'fill="{c["magenta"]}">github.com/{esc(USER)}</text>')
    p.append(f'<text x="{W-26}" y="36" text-anchor="end" font-family="{MONO}" font-size="12" '
             f'fill="{c["muted"]}">{human(d["followers"])} followers · '
             f'{human(d["repos"])} public repos</text>')
    p.append(f'<line x1="26" y1="50" x2="{W-26}" y2="50" stroke="{c["border"]}" '
             'stroke-width="1"/>')

    # left column: counters ---------------------------------------------------
    rows = [("commits", d["commits"], "green"),
            ("stars earned", d["stars"], "yellow"),
            ("pull requests merged", d["prs"], "blue"),
            ("issues opened", d["issues"], "orange"),
            ("reviews given", d["reviews"], "magenta"),
            ("repos contributed to", d["contributed"], "cyan")]
    y = 76
    for label, value, colkey in rows:
        col = c[colkey]
        p.append(f'<circle cx="{34}" cy="{y-4}" r="4" fill="{col}"/>')
        p.append(f'<text x="50" y="{y}" font-family="{MONO}" font-size="13" '
                 f'fill="{c["dim"]}">{esc(label)}</text>')
        p.append(f'<text x="{mid-40}" y="{y}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="15" font-weight="700" fill="{col}">{human(value)}</text>')
        y += 29

    p.append(f'<line x1="{mid}" y1="68" x2="{mid}" y2="{H-26}" stroke="{c["border"]}" '
             'stroke-width="1"/>')

    # right column: language split -------------------------------------------
    rx = mid + 34
    rw = W - 26 - rx
    p.append(f'<text x="{rx}" y="{82}" font-family="{MONO}" font-size="13" font-weight="700" '
             f'fill="{c["fg"]}">most used languages</text>')

    bar_y, bar_h = 96, 12
    x = rx
    for i, (_, pct) in enumerate(d["langs"]):
        seg = rw * pct / 100.0
        col = c[LANG_ACCENT[i % len(LANG_ACCENT)]]
        p.append(f'<rect x="{x:.2f}" y="{bar_y}" width="{max(seg-2, 1):.2f}" height="{bar_h}" '
                 f'rx="6" fill="{col}"/>')
        x += seg
    p.append(f'<rect x="{rx}" y="{bar_y}" width="{rw}" height="{bar_h}" rx="6" fill="none" '
             f'stroke="{c["border"]}" stroke-width="1"/>')

    ly, lx, col_w = bar_y + 40, rx, (rw + 10) / 2
    for i, (name, pct) in enumerate(d["langs"]):
        col = c[LANG_ACCENT[i % len(LANG_ACCENT)]]
        cx = lx + (i % 2) * col_w
        cy = ly + (i // 2) * 26
        p.append(f'<circle cx="{cx+4}" cy="{cy-4}" r="4.5" fill="{col}"/>')
        p.append(f'<text x="{cx+18}" y="{cy}" font-family="{MONO}" font-size="12.5" '
                 f'fill="{c["fg"]}">{esc(name)}</text>')
        p.append(f'<text x="{cx + col_w - 24}" y="{cy}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="12.5" fill="{c["muted"]}">{pct}%</text>')

    return "".join(p) + "</svg>"


if __name__ == "__main__":
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if "--demo" in sys.argv or not token:
        if not token:
            print("no GITHUB_TOKEN in env — rendering demo data", file=sys.stderr)
        data = DEMO
    else:
        data = fetch(token)
    for mode, palette in MODES:
        write("stats", mode, render(palette, data))
