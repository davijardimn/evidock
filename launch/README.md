# RepoReel launch kit

This folder contains the public-launch material for RepoReel v0.8.0.

## Release baseline

- Public repository: https://github.com/davijardimn/reporeel
- Version: `0.8.0`
- License: MIT
- Stable Launch Score rubric/schema: `0.6`
- CI target: Linux, Windows and macOS; Python 3.9 and latest; unit tests + smoke test + eval lint passing.
- Installable Skill artifact: generated with `python tools/package_skill.py` as `dist/reporeel.zip`.
- Core v0.8 loop: GitHub URL/local repo → roast → fix → verify → re-audit → diff + badge.

## Launch rule

Do not optimize for raw link volume. Optimize for a developer seeing a concrete RepoReel result and thinking: “I want to run that on my repo.”

Never ask for coordinated upvotes, stars, comments, or reposts. Never manufacture adoption metrics, testimonials, benchmarks, or “X users already use this” claims.

## The v0.8 story

Lead with the workflow, not with “AI Skill” jargon:

1. Paste a GitHub URL or open a local repo.
2. RepoReel tells you why a stranger would bounce.
3. It verifies consequential claims and keeps runtime proof scoped.
4. Fix Mode improves the launch surface without gaming the score.
5. Re-audit produces a before/after diff.
6. A static badge makes the result easy to share.

The strongest visual remains a real `BLOCKED → READY` before/after. The badge is secondary proof/distribution, not the product itself.

## Channel order

1. GitHub Release `v0.8.0` with `reporeel.zip` attached.
2. X / personal network: show the URL → roast → fix → diff loop and link directly to the repo.
3. r/ClaudeAI showcase: explain that you built RepoReel for Claude, how the evidence contract works, and that it is free/open source.
4. r/LLMDevs: technical angle — deterministic scoring, URL evidence boundaries, Proof Mode, Fix Mode anti-score-gaming, and Agent Skills.
5. r/github: use the self-promotion megathread rather than a standalone promotional post.
6. Hacker News only if familiar with the community and eligible to post; write the actual HN submission yourself.

## Success signals for the first launch

Prefer qualitative evidence over vanity numbers:

- someone roasts an unrelated repository URL
- someone uses Fix Mode and shares a real before/after
- a real issue reports a false positive / false negative
- someone voluntarily adds/shares a RepoReel badge
- someone contributes a launch pattern or eval case

Those signals are stronger than an isolated impression spike.
