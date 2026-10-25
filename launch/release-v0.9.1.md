# Evidock v0.9.1: Branding cleanup

v0.9.1 is a small pre-promotion cleanup release for Evidock.

It removes stale RepoReel wording that remained in three packaged files after the v0.9.0 identity migration and adds a regression test so old branding cannot silently return in future Skill ZIPs.

## Fixed

- `references/pattern-library.md` now uses Evidock branding.
- `references/redaction.md` now uses Evidock branding.
- `templates/audit.json` now says Evidock and uses **Ship Blocker** in its default example value.
- Package tests now reject stale RepoReel / Reel Breaker copy outside the intentional legacy alias in `SKILL.md`.

## Compatibility

- Skill/plugin version: `0.9.1`
- Launch Score rubric/schema: still `0.6`
- Structured `reel_breaker` field: unchanged for historical audit/diff compatibility
- URL Roast, Fix Mode, Proof Mode, scoring and artifact behavior: unchanged

> Evidence before you ship.
