# Changelog

## 0.9.2: Public polish

- Removed typographic em and en dashes from maintained public copy, documentation, SVG assets, and generated report/diff text.
- Reworked punctuation and sentence structure for a cleaner, more consistent repository presentation.
- Added a regression test so typographic dashes do not return to maintained public text by accident.
- Kept the Launch Score rubric/schema at v0.6; scoring behavior and evidence rules are unchanged.

## 0.9.1: Branding cleanup

- Removed stale RepoReel wording from packaged Evidock reference files and the audit template.
- Updated the default `reel_breaker` example value to the user-facing **Ship Blocker** terminology while retaining the field name for v0.6 schema compatibility.
- Added a packaging regression test so stale RepoReel / Reel Breaker copy cannot silently return outside the intentional legacy alias in `SKILL.md`.
- Kept the Launch Score rubric/schema at v0.6; scoring behavior is unchanged.

## 0.9.0: Evidock

- Rebranded **RepoReel → Evidock** before broad public promotion.
- New product line: **Evidence before you ship.**
- Renamed the Agent Skill and package root from `reporeel` to `evidock`.
- Renamed generated working artifacts from `.reporeel/` to `.evidock/`.
- Renamed public visual identity in cards, reports, diffs and badges.
- Renamed the user-facing **THE REEL BREAKER** label to **THE SHIP BLOCKER** while retaining the `reel_breaker` audit field for stable v0.6 schema compatibility.
- Updated Claude plugin/marketplace metadata, package workflow, tests, docs and launch material for Evidock.
- Kept Launch Score rubric/schema at v0.6 so compatible historical audits remain diffable.

## 0.8.0: Close the launch loop

- Added GitHub URL Roast with a bounded, read-only evidence collector.
- Hardened Fix Mode into baseline → plan → minimal patch → verification → re-audit → diff.
- Added anti-score-gaming rules.
- Added a static shareable badge from validated `audit.json`.
- Expanded behavioral eval and cross-platform test coverage.

## 0.7.0: Public repository edition

- Adopted the standard Agent Skills layout.
- Added Front Door, Proof Mode, deterministic scoring, artifact validation, a 32-pattern launch anti-pattern library, behavioral evals, tests and CI.
