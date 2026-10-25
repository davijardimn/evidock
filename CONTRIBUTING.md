# Contributing to RepoReel

RepoReel welcomes changes that make repository-launch diagnosis more evidence-backed, reproducible and portable.

Good contributions include:
- new launch patterns with clear evidence signals and remediation
- rubric wording fixes that preserve deterministic scoring
- cross-platform script fixes
- eval cases for real failure modes
- artifact/report accessibility improvements
- reproducible bugs from Claude.ai, Claude Code or other Agent Skills hosts

Before opening a PR:

```bash
python -m unittest discover -s tests -v
python tools/smoke_test.py
python tools/lint_evals.py
```

Principles:
1. No invented benchmark/traction claims.
2. `N_A` never earns points.
3. A pattern cannot override direct project evidence.
4. Runtime proof must record scope and limitations.
5. Shared reports must redact secrets and unnecessary personal data.
6. Keep agent-facing scripts standard-library-only unless a dependency creates overwhelming value.
