# RepoReel v0.7.0: Public repository edition

**Your code might be ready. Your repo probably isn't.**

RepoReel is an evidence-first Agent Skill that audits how launch-ready a software repository is before you put it in front of GitHub, Hacker News, Reddit, or users.

## What v0.7.0 includes

- Front Door audit: separates what a visitor can understand from what an agent can infer by reading source.
- Claim Verification: classifies public claims as VERIFIED, INFERRED, UNKNOWN, or CONTRADICTED.
- Proof Mode: runs small, non-destructive runtime checks when static evidence is not enough and records the exact execution scope.
- Deterministic 100-point Launch Score built from explicit `PASS / FAIL / N_A / UNKNOWN` criteria. `N_A` earns zero points.
- Launch Status and prioritized launch blockers.
- Shareable `card.svg`, standalone `report.html`, and before/after `diff.svg`, all rendered from validated `audit.json`.
- 32-pattern Launch Pattern Library for recurring repository-launch failures.
- Behavioral eval suite, smoke tests, artifact integrity checks, and cross-platform CI.
- Claude Code marketplace metadata plus a packaged Skill ZIP for Claude.ai/Desktop.

## Install with Claude Code

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

Then open a repository and ask:

```text
Use RepoReel to roast this repository.
Use Proof Mode where it is safe and useful.
Generate the card and report too.
```

## Philosophy

> Market the evidence. Never manufacture it.

Launch Score measures repository launch readiness. It does not measure code quality, product quality, security, or product completeness.

Repository: https://github.com/davijardimn/reporeel
