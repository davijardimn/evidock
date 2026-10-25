# First 72 hours — v0.8.0

This is a sequencing plan, not a promise of traffic.

## Before public posting

- Merge v0.8.0 only after the full CI matrix is green.
- Create GitHub Release `v0.8.0` and attach the packaged `reporeel.zip`.
- Verify the Release ZIP installs in Claude.ai/Desktop.
- Verify the Claude Code marketplace install from a clean environment.
- Confirm repository topics and the CI badge.
- Run one real URL → roast → fix → re-audit → diff + badge flow on a repository that is not RepoReel itself.

## Wave 1 — direct proof

Publish one concrete visual showing the workflow, ideally with a real repository and permission when needed:

```text
GitHub URL → ROAST → FIX → 27 → 86 → BADGE
```

Send the repository only to people genuinely likely to test developer tooling. Ask for **feedback**, not stars.

Goal: obtain the first unrelated-repo audit and identify the first false positive/false negative.

## Wave 2 — communities

Adapt the channel-specific drafts in this directory. Do not cross-post identical wording everywhere.

- r/ClaudeAI: build/process story + free/open source + evidence-first Claude workflow.
- r/LLMDevs: deterministic tooling, remote scope, Proof Mode and anti-score-gaming design.
- r/github: self-promotion megathread only.
- Re-check current community rules immediately before posting; rules can change.

Respond to technical criticism with exact evidence/files rather than marketing language.

## Wave 3 — Hacker News

Only after RepoReel has been exercised by outside users and only if familiar with HN. Read current rules and write the actual submission yourself. Do not coordinate votes/comments.

## Feedback loop

Turn useful criticism into visible repository activity:

- false positive → eval case
- false negative → pattern/rubric clarification
- URL scope bug → parser/collector test
- platform bug → reproduce in CI
- confusing install → simplify Front Door
- successful before/after → ask permission before featuring it

The launch loop should mirror the product philosophy: **real repo → evidence → finding → fix → diff → better Skill**.
