<p align="center">
  <img src="docs/images/hero.svg" alt="RepoReel — evidence-first repository launch audits" width="100%">
</p>

# RepoReel — repository launch audits for Claude & AI agents

<p align="center">
  <a href="https://github.com/davijardimn/reporeel/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/davijardimn/reporeel?style=flat-square"></a>
  <a href="https://github.com/davijardimn/reporeel/actions/workflows/validate.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/davijardimn/reporeel/validate.yml?branch=main&style=flat-square&label=tests"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"></a>
  <img alt="Python standard library only" src="https://img.shields.io/badge/runtime-Python%20stdlib%20only-3776AB?style=flat-square">
</p>

RepoReel turns Claude — or any agent that supports the Agent Skills format — into an **evidence-first launch reviewer for software repositories**. It tells you why a stranger would bounce, verifies what your README claims, safely proves important workflows, scores launch readiness with an auditable rubric, and renders shareable before/after artifacts.

> **Market the evidence. Never manufacture it.**

## Try it in 30 seconds

### 1. Install in Claude Code

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

### 2. Open any software repository and ask

```text
Use RepoReel to roast this repository.
Use Proof Mode where it is safe and useful.
Generate the card and report too.
```

That is enough. RepoReel inspects the repository, separates what a visitor can see from what an agent can infer, verifies public claims, runs scoped proof when useful, and builds the audit from evidence.

<p align="center">
  <img src="docs/images/demo-flow.svg" alt="RepoReel roast to fix to diff demo" width="100%">
</p>

The score above is **launch readiness**, not code quality. A brilliant project can score badly when its repository does not explain, prove or package the product well.

## What RepoReel catches

| Problem | What RepoReel does |
| --- | --- |
| The product only makes sense after reading source | **Front Door audit** tests what a stranger understands before source spelunking |
| README promises more than the code delivers | **Claim Verification** classifies claims as VERIFIED / INFERRED / UNKNOWN / CONTRADICTED |
| Static inspection is not enough | **Proof Mode** runs small, safe experiments and records scope + limitations |
| “AI score” feels arbitrary | **Deterministic Launch Score** maps every point to PASS / FAIL / N_A / UNKNOWN; `N_A` earns 0 |
| The same launch mistakes repeat across repos | **32-pattern library** names recurring failures such as `front-door-void`, `claim-exceeds-code`, `platform-trap` and `na-as-pass` |
| The audit is hard to share | **Validated artifacts** generate `card.svg`, `report.html` and `diff.svg` from structured `audit.json` |

**Contents:** [Install](#install) · [How it works](#how-it-works) · [Example](#example) · [Use](#use) · [What’s inside](#whats-inside) · [Pattern library](#launch-pattern-library) · [Tests & evals](#tests--evals)

---

## Install

### Claude Code — plugin marketplace (recommended)

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

### Claude Code — manual

```bash
git clone https://github.com/davijardimn/reporeel.git
cp -r reporeel/skills/reporeel ~/.claude/skills/reporeel
# or per-project:
cp -r reporeel/skills/reporeel .claude/skills/reporeel
```

### Claude.ai / Claude Desktop

Build the uploadable Skill ZIP:

```bash
python tools/package_skill.py
```

Upload `dist/reporeel.zip` under Claude's Skills settings. The ZIP contains `reporeel/SKILL.md` at its root. A packaged ZIP is also intended to be attached to GitHub Releases.

### Codex, Gemini CLI, Cursor and other agents

RepoReel uses the open Agent Skills layout: a directory containing `SKILL.md`, plain Markdown references, JSON assets and dependency-free Python tools. Copy `skills/reporeel/` into the skills directory supported by your agent.

---

## How it works

```mermaid
flowchart LR
    A[Scope] --> B[Front Door]
    B --> C[Claims]
    C --> D{Need runtime proof?}
    D -- yes --> E[Proof Mode]
    D -- no --> F[Rubric]
    E --> F
    F --> G[Launch Status + Score]
    G --> H[Card + Report]
    H --> I[Fix / Launch / Diff]
```

RepoReel deliberately separates four things that are easy to blur:

```text
Can the agent understand the source?      ≠ Can a visitor understand the repo?
A command is documented                   ≠ The command was proven to work
The software may be good                  ≠ The repository is launch-ready
A criterion is not applicable             ≠ The criterion passed
```

A `roast` ends with a diagnosis, not generic code-review noise. A `proof` records exactly what environment was exercised and what the result does **not** prove.

### Evidence before copy

RepoReel classifies repository claims using four evidence states:

- `VERIFIED` — directly supported by repository evidence or scoped proof.
- `INFERRED` — strongly suggested, but not directly proven.
- `UNKNOWN` — insufficient evidence.
- `CONTRADICTED` — evidence conflicts with the public claim.

Secrets, passwords and unnecessary personal data are redacted from shareable reports. RepoReel proves the finding without republishing the sensitive value.

---

## Example

A roast follows a recognizable structure:

```text
REPOREEL / ROAST
SCOPE
LAUNCH READINESS
10-SECOND TEST
THE REEL BREAKER
CLAIM VERIFICATION
PROOF MODE
LAUNCH BLOCKERS
SCORECARD
IF THIS WERE MY REPO
```

The visual output is generated from validated `audit.json`; renderers do not invent or re-score anything:

<p align="center"><img src="docs/images/roast-card.svg" alt="RepoReel score card" width="82%"></p>

After improvements, `diff` makes the change visible:

<p align="center"><img src="docs/images/before-after.svg" alt="RepoReel before and after score diff" width="82%"></p>

Typical output:

```text
.reporeel/
├── evidence.json
├── audit.json
├── card.svg
├── report.html
└── diff.svg
```

---

## Use

Just ask naturally — the Skill is designed to trigger on repository launch/readiness work even if the user never says “RepoReel”.

> “Why would someone open this repo and leave without starring it?”  
> “Verify the claims in my README.”  
> “Prove the quick start works, but don't change the source.”  
> “Fix my Front Door and re-audit it.”  
> “Prepare HN, Reddit and X launch copy from verified evidence.”  
> “Compare the before and after RepoReel audits.”

Modes: `audit` · `roast` · `verify` · `proof` · `fix` · `readme` · `launch` · `diff` · `ship`.

### Agent-facing tools

All current tools use Python's standard library only:

```bash
python skills/reporeel/scripts/inspect_repo.py --root . --output .reporeel/evidence.json
python skills/reporeel/scripts/search_patterns.py --query "broken readme"
python skills/reporeel/scripts/score_audit.py --audit .reporeel/audit.json
python skills/reporeel/scripts/validate_audit.py --audit .reporeel/audit.json
python skills/reporeel/scripts/render_card.py --audit .reporeel/audit.json --output .reporeel/card.svg
python skills/reporeel/scripts/render_report.py --audit .reporeel/audit.json --output .reporeel/report.html
python skills/reporeel/scripts/verify_artifacts.py --audit .reporeel/audit.json --card .reporeel/card.svg --report .reporeel/report.html
```

---

## What's inside

```text
.claude-plugin/                 Claude Code marketplace/plugin manifests
.github/workflows/             cross-platform validation + packaging
skills/reporeel/
├── SKILL.md                    operating contract and workflow
├── references/                 loaded on demand
│   ├── front-door.md           what counts before source spelunking
│   ├── evidence.md             VERIFIED / INFERRED / UNKNOWN / CONTRADICTED
│   ├── proof-mode.md           safe runtime proof protocol
│   ├── audit-rubric.md         deterministic 100-point rubric
│   ├── launch-status.md        READY / CAUTION / BLOCKED / UNKNOWN
│   ├── redaction.md            share findings without leaking secrets/PII
│   └── pattern-library.md      how to use recurring launch anti-patterns
├── scripts/
│   ├── inspect_repo.py         static evidence collector
│   ├── search_patterns.py      query the launch-pattern library
│   ├── score_audit.py          recompute scores from criterion states
│   ├── validate_audit.py       enforce the audit contract
│   ├── render_card.py          audit.json → shareable SVG
│   ├── render_report.py        audit.json → standalone HTML
│   ├── render_diff.py          before/after → SVG
│   └── verify_artifacts.py     structural integrity checks
├── assets/patterns.json        curated launch anti-pattern library
└── templates/                  structured audit template
evals/                          behavior-contract eval cases
tests/                          repository/tooling tests
tools/
├── smoke_test.py               run scripts the way an agent runs them
├── lint_evals.py               validate eval suite
└── package_skill.py            build dist/reporeel.zip
```

---

## Launch Pattern Library

RepoReel currently ships **32 recurring launch patterns** covering discovery, demonstration, quick start, documentation, trust, polish and audit-method failures. Examples include `front-door-void`, `claim-exceeds-code`, `platform-trap`, `proof-scope-overreach`, `na-as-pass` and `code-review-drift`.

Search it locally:

```bash
python skills/reporeel/scripts/search_patterns.py --category trust
python skills/reporeel/scripts/search_patterns.py --severity HIGH
python skills/reporeel/scripts/search_patterns.py --query "runtime support"
```

Patterns never replace direct evidence or the rubric. They help the agent name and remediate what it has already observed.

---

## Tests & evals

RepoReel ships unit/integration tests, an end-to-end smoke test and a behavioral eval suite. CI runs the validation matrix on Linux, Windows and macOS with Python 3.9 and the latest available Python.

```bash
python -m unittest discover -s tests -v
python tools/smoke_test.py
python tools/lint_evals.py
```

The `evals/` suite checks implicit triggering, scope discipline, redaction, `N_A != PASS`, runtime-proof limits, claim verification and preventing generic code-review drift. It is a behavioral contract, not a model benchmark.

---

## Why RepoReel is not a README generator

A README generator can make weak evidence sound polished. RepoReel does the opposite: it establishes scope, checks the Front Door, classifies claims, proves consequential workflows when safe, records limitations, computes points from explicit states, and **only then** helps improve presentation or launch copy.

It must never manufacture stars, users, testimonials, benchmarks, compatibility, production readiness, security properties or feature completeness. Missing evidence becomes `UNKNOWN`, not marketing.

## Contributing

Contributions are welcome: sharper rubric wording, new launch patterns, platform fixes, eval cases, artifact improvements and reproducible bug reports. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## License

MIT — see [LICENSE](LICENSE).
