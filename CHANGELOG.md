# Changelog

## 0.8.0 — Close the launch loop

- Added **GitHub URL Roast** with `inspect_github.py`, a bounded, read-only GitHub evidence collector that can use an already-configured `GITHUB_TOKEN` without emitting it.
- Added explicit remote-scope rules: a GitHub URL inspection is static evidence and must never be mislabeled as runtime Proof Mode.
- Hardened **Fix Mode** into baseline → fix plan → minimal patch → verification → re-audit → diff.
- Added anti-score-gaming rules: fixes cannot relax the rubric, hide failures, fabricate proof, or silently implement missing product features just to raise Launch Score.
- Added **RepoReel Badge** via `render_badge.py`, producing a static SVG plus ready-to-paste Markdown from validated `audit.json`.
- Added v0.8 references for URL scope, Fix Mode, and badge integrity.
- Expanded behavioral eval coverage for URL Roast, Fix Mode, contradicted-claim repair, and badge integrity.
- Expanded smoke/unit coverage for URL parsing and badge rendering.
- Updated public documentation and launch material around the URL → roast → fix → re-audit → diff/badge loop.
- Kept the stable Launch Score rubric/schema at v0.6 so compatible historical audits remain diffable.

## 0.7.0 — Public repository edition

- Restructured the project around the standard `skills/reporeel/` layout.
- Added Claude Code plugin marketplace manifests under `.claude-plugin/`.
- Added cross-platform smoke testing and release packaging.
- Added a curated Launch Pattern Library plus `search_patterns.py`.
- Added deterministic `score_audit.py` so agents do not perform score arithmetic manually.
- Added model-agnostic behavioral eval cases for triggering, scope, redaction, Proof Mode and `N_A != PASS`.
- Added public examples, visual documentation, package tooling and a repository-level README.
- Kept the stable Launch Score rubric/schema at v0.6; Skill/repository version is 0.7.0.

## 0.6.0-rc.2

- Proof Mode surfaced in HTML report.
- Artifact integrity validation.
- Formal redaction rules.
