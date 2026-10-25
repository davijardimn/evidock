# Evidock roadmap

Evidock is intentionally a Skill first. The roadmap favors stronger evidence, better artifacts, and portable Agent Skills behavior over turning the project into a generic SaaS.

## 0.9 — Evidock identity

- rebrand RepoReel → Evidock before broad promotion
- rename Skill/package/artifact paths to `evidock` / `.evidock`
- keep stable rubric/schema v0.6 for historical audit compatibility
- preserve GitHub URL Roast, evidence-preserving Fix Mode, diff and badge integrity
- validate the renamed package across Linux, Windows and macOS

## Next — validate in the wild

The priority after v0.9 is external evidence, not feature volume: audit unrelated public repositories; record false positives/false negatives; turn real failures into evals/patterns/tests; improve ecosystem-specific checks only where repeated evidence justifies them; publish reproducible demos from real Evidock runs.

## Later, only if evidence justifies it

Historical/trend views across compatible audits; a release-gate helper for CI; a thin CLI wrapper; optional hosted/public report surfaces.

A hosted service, growth dashboard, generic code-review engine, or security scanner should not be added unless real usage shows that it strengthens the evidence-first launch workflow.
