# X launch copy

## Single-post version

I built RepoReel: an open-source Agent Skill that asks one uncomfortable question about your project:

**Is the code ready — but the repo impossible to discover?**

It audits the Front Door, verifies README claims, runs scoped Proof Mode checks, gives an evidence-backed Launch Score, and renders a before → after card.

MIT / free:
https://github.com/davijardimn/reporeel

## Short thread

**1/** Your code can work perfectly and still have a repo nobody understands.

I built RepoReel to audit that gap.

**2/** It does not just “improve your README”.

It separates what a visitor sees from what an AI can infer by reading source, then checks whether public claims are actually backed by implementation.

**3/** When static inspection is not enough, Proof Mode can run a small non-destructive experiment — and records exactly what environment was tested so one sandbox run never becomes a fake “works everywhere” claim.

**4/** The score is deliberately boring in a good way:

PASS / FAIL / N_A / UNKNOWN.
Only PASS earns points.

The card/report/diff are rendered from validated `audit.json`; the renderer cannot invent a nicer number.

**5/** The fun part is the diff:

`02 / 100 · BLOCKED → 87 / 100 · READY`

Not because an AI decided to be nicer — because the evidence changed.

RepoReel is MIT licensed and free/open source:
https://github.com/davijardimn/reporeel
