# RepoReel evals

These cases test the **behavior contract** of the Skill: triggering, mode selection, evidence discipline, scope boundaries, redaction, `N_A != PASS`, Proof Mode and launch-vs-code-review separation.

`cases.json` is intentionally model-agnostic. Each case has:
- `prompt`
- expected mode
- concepts that must appear
- failure modes that must not appear

Lint the suite with:

```bash
python tools/lint_evals.py
```

For a manual model eval, run each prompt against a small fixture/project and record pass/fail plus the model/version. Do not treat these structural cases as claims of benchmark quality.
