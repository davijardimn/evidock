# RepoReel Launch Score v0.6

**Launch Score measures repository launch readiness, not code quality, product quality, security, or completeness.**

Every criterion has one state:
- `PASS` — earns full listed points
- `FAIL` — earns 0
- `N_A` — prerequisite does not apply; earns 0
- `UNKNOWN` — insufficient evidence; earns 0 and may make the audit provisional

**N_A is not PASS. No vacuous points. No partial points.**

## Discovery — 20
1. **+5 `discovery.purpose`** — Purpose at the Front Door.
2. **+4 `discovery.user`** — User/use case explicit.
3. **+5 `discovery.value`** — Concrete outcome/value explicit.
4. **+4 `discovery.differentiation`** — Reason to choose it explicit.
5. **+2 `discovery.identity`** — Repository identity coherent.

Source code hidden behind the Front Door cannot satisfy criteria 1–4.

## Demonstration — 20
1. **+5 `demonstration.proof`** — Real proof exists.
2. **+5 `demonstration.core`** — Core capability demonstrated.
3. **+5 `demonstration.reachability`** — Proof is easy to reach.
4. **+5 `demonstration.credibility`** — Proof is credible.

## Quick Start — 20
1. **+5 `quick_start.prerequisites`** — Prerequisites explicit.
2. **+5 `quick_start.install`** — Installation/setup explicit.
3. **+5 `quick_start.first_use`** — First-use action explicit.
4. **+5 `quick_start.short_path`** — Short path to value.

## Documentation — 15
1. **+5 `documentation.core_usage`** — Core usage documented.
2. **+5 `documentation.behavior`** — Important behavior/config documented.
3. **+5 `documentation.navigation`** — Deeper information navigable.

## Trust — 15
1. **+3 `trust.license`** — License explicit.
2. **+3 `trust.verification`** — Verification signal exists.
3. **+3 `trust.process`** — Maintenance/release process signal exists.
4. **+3 `trust.claims`** — Consequential public claims stay within evidence; N_A when there are no consequential claims.
5. **+3 `trust.support`** — Collaboration/support expectation clear.

## Polish — 10
1. **+2 `polish.no_noise`** — No shipped local/generated noise.
2. **+2 `polish.primary_files_intentional`** — Primary files are intentional.
3. **+2 `polish.front_door_refs`** — Front Door local references resolve; no refs → N_A, 0.
4. **+2 `polish.naming`** — Naming is consistent; one surface only → N_A, 0.
5. **+2 `polish.first_impression`** — Front Door has identity + purpose/value + next step.

For every criterion record `status`, `points`, `max_points`, `prerequisite`, and one concise evidence sentence. Only PASS may earn points. `UNKNOWN` does not automatically make an audit provisional; use `provisional: true` only when missing scope could flip material criteria.

Launch Status is independent from numeric score.

Arithmetic: 20 + 20 + 20 + 15 + 15 + 10 = **100**.
