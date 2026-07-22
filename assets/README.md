# assets

Every card on the profile is a hand-rendered SVG in two Tokyo Night variants —
**Storm** (`*-dark.svg`) and **Day** (`*-light.svg`) — swapped in the README with
`<picture>` + `prefers-color-scheme`. Nothing is fetched from a third-party badge
or stats service at render time, so the profile can't break when someone else's
Vercel deployment goes down.

| File | Built by | Contents |
| :--- | :--- | :--- |
| `theme.py` | — | The two palettes and the shared SVG helpers. Change an accent here and it changes everywhere. |
| `generate.py` | you, locally | `banner-*`, `stack-*`, `social-*-*` |
| `stats.py` | GitHub Actions, daily | `stats-*` (GitHub GraphQL API) |
| `icons/` | — | Vendored [Simple Icons](https://simpleicons.org) glyphs, inlined and recoloured |

## Editing

```bash
cd assets
python generate.py            # after editing GROUPS / SOCIALS / the banner text
python stats.py --demo        # preview the stats card with placeholder numbers
GITHUB_TOKEN=ghp_… python stats.py   # real numbers
```

No dependencies beyond the Python standard library.

## Richer stats (optional)

The daily workflow falls back to the ephemeral `GITHUB_TOKEN`, which only sees
public activity. To include private contributions and follower counts, create a
classic PAT with the `read:user` scope and save it as a repository secret named
`PROFILE_STATS_TOKEN`.

## Adding a technology

1. Grab the glyph: `curl -o icons/<slug>.svg https://cdn.jsdelivr.net/npm/simple-icons/icons/<slug>.svg`
   (browse slugs at [simpleicons.org](https://simpleicons.org)).
2. Add `("Label", "<slug>")` to the right group in `GROUPS` in `generate.py`.
3. `python generate.py`.

Chips wrap automatically, so a group can grow without breaking the layout.
