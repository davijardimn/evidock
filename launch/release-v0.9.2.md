# Evidock v0.9.2: Public polish

v0.9.2 is the public polish release for Evidock before broader promotion.

It keeps the product behavior, Launch Score rubric, evidence model, URL Roast, Proof Mode, Fix Mode, diff, badge, and artifact pipeline unchanged. The focus is presentation consistency and release readiness.

## Improved

- Removed typographic em and en dashes from maintained public copy, documentation, SVG assets, and generated report/diff text.
- Reworked punctuation and sentence structure for a cleaner repository presentation.
- Added a regression test that prevents typographic dashes from returning to maintained public text.
- Synchronized Skill, plugin, marketplace, README, publishing checklist, and launch material at version `0.9.2`.

## Compatibility

- Skill/plugin version: `0.9.2`
- Launch Score rubric/schema: `0.6`
- Structured `reel_breaker` field: unchanged for historical audit/diff compatibility
- URL Roast, Fix Mode, Proof Mode, scoring, and artifact behavior: unchanged

## Install

```text
/plugin marketplace add davijardimn/evidock
/plugin install evidock@evidock
```

For Claude.ai or Claude Desktop, use the versioned Skill ZIP attached to this Release.

> Evidence before you ship.
