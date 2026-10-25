---
name: evidock
description: Evidence-first launch audit for software repositories. Use this skill whenever someone wants to roast, audit, score, verify, prove, improve, fix, package, or prepare a repo for GitHub/Hacker News/Reddit; audit a GitHub repository URL; improve a README or repository Front Door; check whether public feature claims are actually supported; compare before/after launch readiness; generate a shareable score card/report/badge; or asks why a project is not getting attention or stars. Also use for repository launch reviews even when the user does not say “Evidock”. If the user says “RepoReel”, treat it as the former name of Evidock.
license: MIT
metadata:
  author: Davi Jardim Nascimento
  version: "0.9.1"
---

# Evidock

**Evidence before you ship.**

Evidock audits, proves, fixes, roasts, and improves how a software project appears before launch.

> Market the evidence. Never manufacture it.

## Operating contract

1. **Inspect before writing.** Build a project model from available evidence.
2. **Separate discovery from implementation.** A fact hidden in source code does not make it clear at the repository Front Door.
3. **Classify claims.** Use VERIFIED, INFERRED, UNKNOWN, or CONTRADICTED.
4. **Prove when safe.** Runtime checks can strengthen a claim, but only within the execution scope actually tested.
5. **Score launch readiness only.** Launch Score is not code quality, product quality, security score, or product completeness.
6. **Never award arbitrary partial credit.** Rubric criteria are PASS / FAIL / N_A / UNKNOWN. Only PASS earns points.
7. **N_A is not PASS.** It earns 0 points. UNKNOWN earns 0 points and may make the result provisional.
8. **Do not drift into generic code review.** Mention implementation/security findings only when they materially affect launch trust, reproducibility, truthfulness, or the primary demo path.
9. **Redact sensitive evidence.** Prove the finding without republishing secrets, plaintext passwords, tokens, or unnecessary personal data. Read `references/redaction.md` when sensitive evidence appears.
10. **No score gaming.** A fix may raise Launch Score only when underlying evidence improves. Never relax the rubric, hide a failure, fabricate proof, or rewrite the audit to manufacture progress.

## Detect the environment and input scope

### Chat mode
Use when files/archives or repository links are supplied in Claude chat.
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
- `audit`, `roast`, `verify`, `proof`, and `diff` must not change application source.

### GitHub URL input
When the user supplies `https://github.com/owner/repo` (or a deeper URL within that repo), read `references/github-url.md`.
- Prefer a connected read-only GitHub/repository tool when available.
- Otherwise, when Python + network are available, use `scripts/inspect_github.py`.
- Remote URL inspection is static evidence, not runtime proof.
- Never ask the user to paste a GitHub token into chat. The collector may use an already-configured `GITHUB_TOKEN` without emitting it.
- If the remote repository cannot be accessed, say so rather than pretending it was inspected.

Read `references/scope.md` whenever completeness or execution scope could change a scored criterion.

## Modes

| Mode | Purpose | Source mutation |
|---|---|---|
| `audit` | Evidence-backed Launch Score + gaps | No |
| `roast` | Ruthless 10-second visitor assessment | No |
| `verify` | Verify consequential public claims | No |
| `proof` | Safely test a claim/workflow at runtime | No |
| `fix` | Baseline → plan → minimal launch-surface patch → verify → re-audit → diff | Yes when editable |
| `readme` | Create or improve README from evidence | Yes/output artifact |
| `launch` | Create launch material from verified evidence | Output artifacts |
| `diff` | Compare compatible before/after audits | No |
| `ship` | Discover → verify/prove → audit → fix → re-audit → artifacts → launch | Yes/output artifacts |

Natural-language equivalents count. If the user only says “use Evidock”, default to `ship` when enough editable evidence exists; otherwise run `audit`.

## Core workflow

### 1. Discover
Inspect, when available: README/docs and repository metadata; manifests/lockfiles; source tree and entrypoints; tests/examples; CI/release files; license/support/contribution files; screenshots/demos/assets; Git metadata.

For a local filesystem, prefer:

```bash
python3 <skill-directory>/scripts/inspect_repo.py --root <project-root> --output <working-dir>/evidence.json
```

For a GitHub URL when no native repository connector is available:

```bash
python3 <skill-directory>/scripts/inspect_github.py \
  --repo https://github.com/owner/repo \
  --output <working-dir>/github-evidence.json
```

The URL collector is read-only and bounded. Treat truncation/unavailable files as uninspected scope, not confirmed absence.

### 2. Evaluate the Front Door
The Front Door is what a stranger can learn **before running or spelunking through source code**. Read `references/front-door.md`.

Ask: What is it? Who is it for? What outcome does it deliver? Why is it worth attention? What does it look like/output? How can I try it?

Do not award Front Door points from hidden templates/source files.

### 3. Verify claims
Read `references/claim-verification.md` and `references/evidence.md`. For consequential claims, classify VERIFIED, INFERRED, UNKNOWN, or CONTRADICTED.

### 4. Use Proof Mode when valuable and safe
Read `references/proof-mode.md`. Prefer the smallest non-destructive runtime experiment that can confirm/refute a meaningful claim. Record command/action, environment/scope, result, observations, and limitations. A sandbox pass proves only the tested sandbox/configuration. A remote GitHub URL by itself is not Proof Mode.

### 5. Determine Launch Status
Read `references/launch-status.md`. Launch Status is independent of Launch Score: READY, CAUTION, BLOCKED, UNKNOWN.

### 6. Calculate Launch Score
Read `references/audit-rubric.md`. Categories total 100: Discovery 20, Demonstration 20, Quick Start 20, Documentation 15, Trust 15, Polish 10. Each criterion must have a state and evidence. Only PASS gets its full points.

The stable audit/rubric schema remains `0.6` in Evidock v0.9.1 so compatible historical audits can still be diffed. The structured field `reel_breaker` is retained for v0.6 schema compatibility; user-facing output calls it **THE SHIP BLOCKER**.

### 7. Persist structured output when supported
Read `references/audit-schema.md`.

Preferred artifacts:

```text
.evidock/
├── evidence.json
├── github-evidence.json
├── audit.json
├── report.html
├── card.svg
├── badge.svg
├── badge.md
├── before.audit.json
├── after.audit.json
└── diff.svg
```

Validate before rendering:

```bash
python3 <skill-directory>/scripts/validate_audit.py --audit <audit.json>
python3 <skill-directory>/scripts/render_card.py --audit <audit.json> --output <card.svg>
python3 <skill-directory>/scripts/render_report.py --audit <audit.json> --output <report.html>
python3 <skill-directory>/scripts/render_badge.py --audit <audit.json> --output <badge.svg> --markdown-output <badge.md>
python3 <skill-directory>/scripts/verify_artifacts.py --audit <audit.json> --card <card.svg> --report <report.html>
```

For before/after:

```bash
python3 <skill-directory>/scripts/render_diff.py --before <before.json> --after <after.json> --output <diff.svg>
```

`audit.json` is the source of truth. Renderers must not reinterpret scores. Read `references/artifact-integrity.md` and `references/badge.md`.

## Mode-specific behavior

### Roast
Use this recognizable order:

```text
EVIDOCK / ROAST
SCOPE
LAUNCH READINESS
10-SECOND TEST
THE SHIP BLOCKER
CLAIM VERIFICATION
PROOF MODE
LAUNCH BLOCKERS
SCORECARD
IF THIS WERE MY REPO
```

`THE SHIP BLOCKER` is the single evidence-backed issue causing the most launch damage. Be sharp but useful. Do not insult the author. Do not end with a question. End with the diagnosis and `Then run Evidock roast again.` For URL Roast, explicitly label the scope as remote/static when that is all that was inspected.

### Audit
Be less theatrical than roast. Include scope, snapshot, status, Launch Score, strengths, gaps, unknowns, and priorities.

### Verify / Proof
Do not treat documentation as runtime proof. State exactly what was and was not tested.

### Fix
Read `references/fix-mode.md` before mutation. Preserve a baseline audit, map edits to evidence, apply the smallest evidence-supported launch-surface patch, verify, re-audit with the same rubric version, then generate the diff. If a public claim is CONTRADICTED because a product feature does not exist, default to correcting the public claim rather than silently implementing a feature for points.

### README
Read `references/readme-system.md`. Improve only evidence-supported presentation/documentation. Never invent metrics, users, compatibility, benchmarks, or security claims.

### Launch
Read `references/launch.md`. Generate channel-native copy only from verified evidence and clearly framed inferences.

### Diff
Read `references/diff.md`. Only compare matching `rubric_version` values.

### Badge
Read `references/badge.md`. A badge is a snapshot of validated launch readiness, not a quality/security certification. Never hand-edit it to display a better result.

## Launch Pattern Library

When a failure resembles a recurring repository-launch anti-pattern, read `references/pattern-library.md` and optionally query the bundled library. Use patterns to improve diagnosis and remediation, never to override direct evidence.

## Safety

Prefer non-destructive local checks. Never deploy, publish packages, migrate production data, expose secrets, make purchases, start paid services, or execute suspicious project code solely to improve a score. Network access is optional; Evidock must remain useful offline except for explicitly remote URL inspection.
