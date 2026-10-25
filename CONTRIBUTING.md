# Contributing to Evidock

Evidock welcomes changes that make repository-launch diagnosis more evidence-backed, reproducible and portable.

Good contributions include new launch patterns with clear evidence signals, rubric wording fixes that preserve deterministic scoring, cross-platform script fixes, eval cases for real failure modes, artifact/report accessibility improvements, and reproducible bugs from Agent Skills hosts.

Before opening a PR:

```bash
python -m unittest discover -s tests -v
python tools/smoke_test.py
python tools/lint_evals.py
```

Principles: no invented benchmark/traction claims; `N_A` never earns points; a pattern cannot override direct evidence; runtime proof must record scope and limitations; shared reports must redact secrets and unnecessary personal data; keep agent-facing scripts standard-library-only unless a dependency creates overwhelming value.
