# Evidock evals

These cases test the **behavior contract** of the Skill: triggering, mode selection, evidence discipline, scope boundaries, redaction, `N_A != PASS`, Proof Mode, Fix Mode, URL Roast, badge integrity, and launch-vs-code-review separation.

`cases.json` is intentionally model-agnostic. Each case has a prompt, expected mode, concepts that must appear, and failure modes that must not appear.

Lint with `python tools/lint_evals.py`. For manual model evals, run each prompt against a small fixture/project and record pass/fail plus model/version. Do not treat these structural cases as benchmark claims.
