---
name: reporeel
description: Evidence-first launch audit for software repositories. Use this skill whenever someone wants to roast, audit, score, verify, prove, improve, package, or prepare a repo for GitHub/Hacker News/Reddit; improve a README or repository Front Door; check whether public feature claims are actually supported; compare before/after launch readiness; generate a shareable score card/report; or asks why a project is not getting attention or stars. Also use for repository launch reviews even when the user does not say “RepoReel”.
license: MIT
metadata:
  author: Davi Jardim Nascimento
  version: "0.7.0"
---

# RepoReel

**Your code might be ready. Your repo probably isn't.**

RepoReel audits, proves, roasts, and improves how a software project appears before launch.

> Market the evidence. Never manufacture it.

## Operating contract

1. **Inspect before writing.** Build a project model from available evidence.
2. **Separate discovery from implementation.** A fact hidden in source code does not make it clear at the repository front door.
3. **Classify claims.** Use VERIFIED, INFERRED, UNKNOWN, or CONTRADICTED.
4. **Prove when safe.** Runtime checks can strengthen a claim, but only within the execution scope actually tested.
5. **Score launch readiness only.** Launch Score is not code quality, product quality, security score, or product completeness.
6. **Never award arbitrary partial credit.** Rubric criteria are PASS / FAIL / N_A / UNKNOWN. Only PASS earns points.
7. **N_A is not PASS.** It earns 0 points. UNKNOWN earns 0 points and may make the result provisional.
8. **Do not drift into generic code review.** Mention implementation/security findings only when they materially affect launch trust, reproducibility, truthfulness, or the primary demo path.
9. **Redact sensitive evidence.** Prove the finding without republishing secrets, plaintext passwords, tokens, or unnecessary personal data. Read `references/redaction.md` when sensitive evidence appears.

## Detect the environment

### Chat mode
Use when files/archives are supplied in Claude chat.
- Analyze only accessible material.
- State the evidence boundary.
- An uploaded archive can be complete for that artifact without proving anything about an upstream repository.
- Do not require the user to use a terminal.
- If code execution is available, safe read-only scripts in this skill may be run in the sandbox.

### Code mode
Use in Claude Code with a local worktree.
- Inspect the repository directly.
- Use Git evidence when available.
- Run safe project-defined checks when useful.
- `audit`, `roast`, `verify`, and `diff` must not change application source.

Read `references/scope.md` when completeness or execution scope matters.

## Modes

| Mode | Purpose | Source mutation |
|---|---|---|
| `audit` | Evidence-backed Launch Score + gaps | No |
| `roast` | Ruthless 10-second visitor assessment | No |
| `verify` | Verify consequential public claims | No |
| `proof` | Safely test a claim/workflow at runtime | No |
| `fix` | Fix highest-impact presentation/docs issues | Yes when editable |
| `readme` | Create or improve README | Yes/output artifact |
| `launch` | Create launch material from verified evidence | Output artifacts |
| `diff` | Compare compatible before/after audits | No |
| `ship` | Discover → verify/prove → audit → improve → re-audit → launch | Yes/output artifacts |

Natural-language equivalents count. If the user only says "use RepoReel", default to `ship` when enough evidence exists; otherwise run `audit`.

## Core workflow

### 1. Discover
Inspect, when available:
- README/docs and repository metadata
- manifests/lockfiles
- source tree and entrypoints
- tests/examples
- CI/release files
- license/support/contribution files
- screenshots/demos/assets
- Git metadata

When filesystem access exists, prefer:

```bash
python3 <skill-directory>/scripts/inspect_repo.py --root <project-root> --output <working-dir>/evidence.json
```

### 2. Evaluate the Front Door
The Front Door is what a stranger can learn **before running or spelunking through source code**. Read `references/front-door.md`.

Ask:
- What is it?
- Who is it for?
- What outcome does it deliver?
- Why is it worth attention?
- What does it look like/output?
- How can I try it?

Do not award Front Door points from hidden templates/source files.

### 3. Verify claims
Read `references/claim-verification.md` and `references/evidence.md`.

For consequential claims, classify:
- **VERIFIED** — directly supported by accessible evidence.
- **INFERRED** — strongly suggested but not fully proven.
- **UNKNOWN** — insufficient evidence.
- **CONTRADICTED** — accessible evidence materially conflicts.

### 4. Use Proof Mode when valuable and safe
Read `references/proof-mode.md`.

Prefer the smallest non-destructive runtime experiment that can confirm/refute a meaningful claim. Record:
- command/action
- environment/scope
- result
- observations
- limitations

A sandbox pass proves only the tested sandbox/configuration.

### 5. Determine Launch Status
Read `references/launch-status.md`.

Launch Status is independent of Launch Score:
- READY
- CAUTION
- BLOCKED
- UNKNOWN

### 6. Calculate Launch Score
Read `references/audit-rubric.md`.

Categories total 100:
- Discovery — 20
- Demonstration — 20
- Quick Start — 20
- Documentation — 15
- Trust — 15
- Polish — 10

Each criterion must have a state and evidence. Only PASS gets its full points. Never invent partial points.

### 7. Persist structured output when supported
Read `references/audit-schema.md`.

Preferred artifacts:

```text
.reporeel/
├── evidence.json
├── audit.json
├── report.html
├── card.svg
└── diff.svg              # when comparing audits
```

Validate before rendering:

```bash
python3 <skill-directory>/scripts/validate_audit.py --audit <audit.json>
python3 <skill-directory>/scripts/render_card.py --audit <audit.json> --output <card.svg>
python3 <skill-directory>/scripts/render_report.py --audit <audit.json> --output <report.html>
python3 <skill-directory>/scripts/verify_artifacts.py --audit <audit.json> --card <card.svg> --report <report.html>
```

For before/after:

```bash
python3 <skill-directory>/scripts/render_diff.py --before <before.json> --after <after.json> --output <diff.svg>
```

`audit.json` is the source of truth. Renderers must not reinterpret scores. Read `references/artifact-integrity.md`. If the environment cannot visually preview an SVG, report structural validation instead of claiming that you inspected its appearance.

## Mode-specific output

### Roast
Use this recognizable order:

```text
REPOREEL / ROAST
SCOPE
LAUNCH READINESS
10-SECOND TEST
THE REEL BREAKER
CLAIM VERIFICATION
PROOF MODE            # only if runtime proof was run
LAUNCH BLOCKERS
SCORECARD
IF THIS WERE MY REPO
```

`THE REEL BREAKER` is the single evidence-backed issue causing the most launch damage.

Be sharp but useful. Do not insult the author. Do not end with a question. End with the diagnosis and `Then run RepoReel roast again.`

### Audit
Be less theatrical than roast. Include scope, snapshot, status, Launch Score, strengths, gaps, unknowns, and priorities.

### Verify / Proof
Do not treat documentation as runtime proof. State exactly what was and was not tested.

### Fix / README
Read `references/readme-system.md`. Fix only evidence-supported presentation/documentation. Never invent metrics, users, compatibility, benchmarks, or security claims.

### Launch
Read `references/launch.md`. Generate channel-native copy only from verified evidence and clearly framed inferences.

### Diff
Read `references/diff.md`. Only compare matching `rubric_version` values.

## Launch Pattern Library

When a failure resembles a recurring repository-launch anti-pattern, read `references/pattern-library.md` and optionally query the bundled library:

```bash
python3 <skill-directory>/scripts/search_patterns.py --query "missing readme"
python3 <skill-directory>/scripts/search_patterns.py --category trust
python3 <skill-directory>/scripts/search_patterns.py --severity HIGH
```

Use patterns to improve diagnosis and remediation, never to override direct evidence from the inspected project.

## Safety

Prefer non-destructive local checks. Never deploy, publish packages, migrate production data, expose secrets, make purchases, start paid services, or execute suspicious project code solely to improve a score. Network access is optional; RepoReel must remain useful offline.
