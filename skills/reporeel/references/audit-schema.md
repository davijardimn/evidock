# RepoReel Audit JSON v0.6

`audit.json` is the source of truth for cards, reports, and diffs.

Required top-level fields include `schema_version`, `rubric_version`, `project`, `scope`, `provisional`, `launch_score`, `launch_status`, `categories`, `reel_breaker`, `blockers`, `criteria`, `claims`, and `proof_runs`.

## Invariants
- Versions must be `0.6`.
- Launch Status: READY / CAUTION / BLOCKED / UNKNOWN.
- Criterion status: PASS / FAIL / N_A / UNKNOWN.
- Only PASS may have nonzero points; PASS must equal `max_points`.
- Category scores must equal criterion sums.
- Category maxima are exactly 20/20/20/15/15/10.
- Launch Score equals category sum.
- Every rubric criterion ID appears exactly once.
- Blocker severities: CRITICAL / HIGH / MEDIUM / LOW.
- Claim states: VERIFIED / INFERRED / UNKNOWN / CONTRADICTED.
- Proof results: PASS / FAIL / INCONCLUSIVE / SKIPPED.
- A `proof_run.claim_id`, when present, must reference a claim in the same audit.
- `provisional_reason` is required when provisional is true.
- Diff requires matching `rubric_version`.

Always run `scripts/validate_audit.py` before rendering.
