<!--
  ─────────────────────────────────────────────────────────────────────────────
  Theme: Tokyo Night — Storm (dark) / Day (light). Both modes are hand-rendered
  SVGs in ./assets, swapped via <picture> + prefers-color-scheme.

  TO PERSONALISE, edit:
    · the links in the chips row below (GitHub / LinkedIn / X / email)
    · "Currently" and "Selected work" — replace with your real repos
    · the stack: edit GROUPS in assets/generate.py, then `python assets/generate.py`

  The stats card currently holds PLACEHOLDER numbers. It fills with real data the
  first time .github/workflows/profile-assets.yml runs (daily, or run it manually
  from the Actions tab).
  ─────────────────────────────────────────────────────────────────────────────
-->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Sourabh Jha — AI Engineer" src="assets/banner-dark.svg" width="880">
</picture>

<p>
  <a href="https://github.com/jha-sk">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/social-github-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/social-github-light.svg">
      <img alt="GitHub" src="assets/social-github-dark.svg" height="34">
    </picture>
  </a>
  <a href="https://www.linkedin.com/in/sk-jha/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/social-linkedin-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/social-linkedin-light.svg">
      <img alt="LinkedIn" src="assets/social-linkedin-dark.svg" height="34">
    </picture>
  </a>
  <a href="https://x.com/cannibiscoder">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/social-x-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/social-x-light.svg">
      <img alt="X" src="assets/social-x-dark.svg" height="34">
    </picture>
  </a>
  <a href="mailto:sourabhjha.personal@gmail.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/social-email-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/social-email-light.svg">
      <img alt="Email" src="assets/social-email-dark.svg" height="34">
    </picture>
  </a>
</p>

</div>

---

I build **AI tooling that runs unattended** — agents that do a real job end to end,
and developer tools that give a model genuine context about a codebase instead of a
pile of files. Most of what I ship is the unglamorous half: parsing, scheduling,
retries, and the plumbing that keeps a pipeline alive after the demo.

- 🧠 **Now** — MCP servers and code intelligence: tree-sitter parsing, dependency graphs, architectural risk scoring
- 🤖 **Running in production** — an autonomous job-hunt agent that fetches, scores, tailors, and reports every morning on a $0/month budget
- 🛠 **Also building** — offline-first product work in React + Supabase for people with bad connectivity and real deadlines
- 🤝 **Open to** — collaborating on open-source AI developer tooling and agent infrastructure

<br>

## Stack

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/stack-light.svg">
  <img alt="Tech stack" src="assets/stack-dark.svg" width="880">
</picture>

</div>

<br>

## Selected work

<!-- Pin these same three on your profile so the section and the sidebar agree. -->

| Project | What it does | Stack |
| :--- | :--- | :--- |
| **[codebase-analyzer](https://github.com/jha-sk/codebase-analyzer)** | MCP server + CLI giving Claude architectural insight into a repo — tree-sitter dependency graphs, Tarjan cycle detection, 0–100 risk scoring, and a self-contained 3-layer interactive graph | `Python` · `MCP` · `tree-sitter` |
| **[job-hunt-agent](https://github.com/jha-sk/job-hunt-agent)** | Autonomous daily job pipeline — fetch, score against your resume, tailor a PDF, watch for recruiter replies, email one digest. Runs on Actions' free tier at $0/month | `Python` · `LLM` · `GitHub Actions` |
| **[Logistics-dashboard](https://github.com/jha-sk/Logistics-dashboard)** | Offline-first PWA for small freight operators — trips, expenses, and P&L, with optional Supabase sync and invite-only access enforced in Postgres row-level security | `React 19` · `TypeScript` · `Supabase` |

<br>

## How I work

```yaml
principles:
  - parse, never regex          # tree-sitter over guesswork when reading code
  - filter before you spend     # cull 80% of the input before it reaches the model
  - read-only by default        # a tool that analyses your repo must not touch it
  - free tier as a constraint   # $0/month forces honest scope
  - it should survive Monday    # unattended beats impressive
```

<br>

## Stats

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/stats-light.svg">
  <img alt="GitHub statistics" src="assets/stats-dark.svg" width="880">
</picture>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=jha-sk&radius=14&hide_border=false&custom_title=Contribution%20activity&bg_color=24283b&color=c0caf5&title_color=bb9af7&line=7aa2f7&point=bb9af7&area_color=7aa2f7&area=true">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=jha-sk&radius=14&hide_border=false&custom_title=Contribution%20activity&bg_color=e1e2e7&color=3760bf&title_color=9854f1&line=2e7de9&point=9854f1&area_color=2e7de9&area=true">
  <img alt="Contribution activity" width="880" src="https://github-readme-activity-graph.vercel.app/graph?username=jha-sk&radius=14&hide_border=false&custom_title=Contribution%20activity&bg_color=24283b&color=c0caf5&title_color=bb9af7&line=7aa2f7&point=bb9af7&area_color=7aa2f7&area=true">
</picture>

</div>

<br>

<div align="center">
<sub>Tokyo Night · Storm &amp; Day — cards rendered from <a href="assets/">./assets</a>, refreshed daily by
<a href=".github/workflows/profile-assets.yml">GitHub Actions</a>.</sub>
</div>
