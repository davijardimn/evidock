# RepoReel launch kit

This folder contains the public-launch material for RepoReel v0.7.0.

## Release baseline

- Public repository: https://github.com/davijardimn/reporeel
- Version: `0.7.0`
- License: MIT
- CI baseline: Linux, Windows and macOS; Python 3.9 and latest; unit tests + smoke test + eval lint passing.
- Installable Skill artifact: generated with `python tools/package_skill.py` as `dist/reporeel.zip`.

## Launch rule

Do not optimize for raw link volume. Optimize for the right developer seeing a concrete result and thinking: “I want to run this on my repo.”

Never ask for coordinated upvotes, stars, comments, or reposts. Do not manufacture adoption metrics, testimonials, benchmarks, or “X users already use this” claims.

## Channel order

1. GitHub Release `v0.7.0` with `reporeel.zip` attached.
2. X / personal network: show the `02 → 87` visual and link directly to the repo.
3. r/ClaudeAI showcase: explain that you built RepoReel for Claude, how Claude was used while developing/testing it, and that it is free/open source.
4. r/LLMDevs: technical angle — deterministic scoring, Proof Mode and the Agent Skills format.
5. r/github: use the self-promotion megathread rather than a standalone promotional post.
6. Hacker News only if you are already familiar with HN culture and eligible to post Show HN. Write the submission yourself; HN explicitly asks users not to post generated text.

## Success signals for the first launch

Prefer qualitative evidence over vanity numbers:

- someone installs it without asking how
- someone runs `roast` on an unrelated repository
- a real issue reports a false positive / false negative
- someone shares a RepoReel card or diff voluntarily
- someone contributes a launch pattern or eval case

Those are stronger signals than an isolated spike in impressions.
