# First 72 hours

This is a sequencing plan, not a promise of traffic.

## Before public posting

- Create GitHub Release `v0.7.0` and attach the packaged `reporeel.zip`.
- Add repository topics: `agent-skills`, `claude`, `claude-code`, `developer-tools`, `github`, `readme`, `repository`, `open-source`, `audit`, `llm`, `ai-agents`.
- Verify the Release ZIP installs once in Claude.ai/Desktop.
- Verify the Claude Code marketplace install once from a clean environment.
- Make sure the CI badge is green.

## Wave 1 — direct proof

Publish the visual `ROAST → FIX → DIFF` on X and send the repository only to people who are genuinely likely to test developer tooling. Ask for **feedback**, not stars.

Goal: get the first unrelated repo audit and find the first false positive/false negative.

## Wave 2 — communities

Use the channel-specific drafts in this directory, adapted to the community. Do not cross-post the same wording everywhere.

- r/ClaudeAI: build/process story + free/open source + how Claude was used.
- r/LLMDevs: deterministic-tooling / agent-evaluation angle.
- r/github: self-promotion megathread only.
- Avoid r/opensource for this launch under its current anti-AI project rule.

Respond to technical questions with evidence and link to exact files/scripts when useful.

## Wave 3 — Hacker News

Only after the repo has already been exercised by outside users and only if you are familiar with HN. Write the submission yourself. Do not reuse generated launch prose.

## What to do with feedback

Turn useful criticism into visible repository activity:

- false-positive report → add an eval case
- false-negative report → add/update a launch pattern or rubric wording
- platform bug → reproduce in CI
- confusing install → simplify the Front Door
- successful before/after → ask permission before featuring it

The best launch loop for RepoReel is itself evidence-driven: **real repo → finding → fix → diff → better Skill**.
