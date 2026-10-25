# RepoReel roadmap

RepoReel is intentionally a Skill first. The roadmap favors stronger evidence, better artifacts, and portable Agent Skills behavior over turning the project into a generic SaaS.

## 0.8 — close the launch loop

- GitHub URL Roast with a read-only evidence collector
- evidence-preserving Fix Mode
- before/after re-audit loop
- static RepoReel badge + Markdown snippet
- URL/fix/badge behavioral evals and smoke coverage

## Next — validate in the wild

The priority after v0.8 is external evidence, not feature volume:

- audit unrelated public repositories and record false positives/false negatives
- turn real failures into eval cases and launch patterns
- improve ecosystem-specific Front Door checks only where repeated evidence justifies them
- add richer versioned synthetic eval fixtures
- improve reproducible demo material from real RepoReel runs

## Later, only if evidence justifies it

- historical/trend views across compatible RepoReel audits
- a release-gate helper for CI
- a thin CLI wrapper around deterministic scripts
- optional hosted/public report surfaces

A hosted service, growth dashboard, generic code-review engine, or security scanner should not be added unless real usage shows that it strengthens the evidence-first launch workflow.

The Skill remains the source product; wrappers should not replace the evidence model.
