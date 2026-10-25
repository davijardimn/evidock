# Evidock Audit JSON: stable schema v0.6

`audit.json` is the source of truth for cards, reports, diffs, and badges.

Required top-level fields include `schema_version`, `rubric_version`, `project`, `scope`, `provisional`, `launch_score`, `launch_status`, `categories`, `reel_breaker`, `blockers`, `criteria`, `claims`, and `proof_runs`.

The `reel_breaker` field name is retained for historical v0.6 compatibility; Evidock labels it **THE SHIP BLOCKER** in user-facing output.

Invariants: versions are `0.6`; Launch Status is READY/CAUTION/BLOCKED/UNKNOWN; criterion status is PASS/FAIL/N_A/UNKNOWN; only PASS may have nonzero points and must equal `max_points`; category scores equal criterion sums; maxima are 20/20/20/15/15/10; Launch Score equals category sum; every criterion ID appears exactly once; blocker severities are CRITICAL/HIGH/MEDIUM/LOW; claim states are VERIFIED/INFERRED/UNKNOWN/CONTRADICTED; proof results are PASS/FAIL/INCONCLUSIVE/SKIPPED; linked proof claims must exist; provisional audits require `provisional_reason`; diffs require matching `rubric_version`.

Always run `scripts/validate_audit.py` before rendering.
