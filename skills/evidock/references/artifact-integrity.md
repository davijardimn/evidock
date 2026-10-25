# Evidock Artifact Integrity

Evidock artifacts are generated from validated `audit.json`.

After rendering, verify them structurally when filesystem execution is available:

```bash
python3 <skill-directory>/scripts/verify_artifacts.py \
  --audit <audit.json> \
  --card <card.svg> \
  --report <report.html>
```

Add `--diff <diff.svg>` when a diff exists. This confirms the audit validates, SVG files are parseable, card score/status match the audit, required report sections exist, and recorded Proof Mode runs appear in the report.

It does **not** prove an SVG was visually inspected. If the environment cannot preview SVG, report structural validation instead of claiming visual review.
