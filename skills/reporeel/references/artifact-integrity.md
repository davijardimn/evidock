# Artifact Integrity v0.6

RepoReel artifacts are generated from validated `audit.json`.

After rendering, verify them structurally when filesystem execution is available:

```bash
python3 <skill-directory>/scripts/verify_artifacts.py \
  --audit <audit.json> \
  --card <card.svg> \
  --report <report.html>
```

Add `--diff <diff.svg>` when a diff exists.

This check confirms:
- the audit still validates
- SVG files are parseable XML with an SVG root
- card score/status match the audit
- the HTML report contains required sections
- every recorded Proof Mode run appears in the report

It does **not** prove the SVG was visually inspected. If the environment cannot render/preview SVG, say so plainly and report structural validation instead of claiming visual review.
