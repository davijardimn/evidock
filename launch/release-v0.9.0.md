# Evidock v0.9.0: Evidence before you ship

v0.9.0 is the public identity release: **RepoReel is now Evidock**.

The product remains evidence-first. Give Evidock a local repository or GitHub URL and it audits the Front Door, verifies public claims, uses scoped Proof Mode when safe, computes a deterministic Launch Score, fixes evidence-backed launch blockers, re-audits, and renders shareable artifacts.

## Rebrand

- Skill/plugin/package name: `evidock`
- Skill path: `skills/evidock/`
- working artifacts: `.evidock/`
- package: `evidock.zip`
- public badge/card/report/diff identity: Evidock
- user-facing diagnosis label: **THE SHIP BLOCKER**

The structured audit field `reel_breaker` remains unchanged because the stable audit/rubric schema stays at v0.6 for historical diff compatibility.

## Integrity unchanged

- URL Roast is read-only/static evidence, not runtime proof.
- Fix Mode cannot game the score by relaxing criteria or inventing evidence.
- Only PASS earns points; N_A and UNKNOWN earn zero.
- Shareable artifacts render from validated `audit.json`.
- The badge is a launch-readiness snapshot, not a security/code-quality certification.

> Evidence before you ship.
