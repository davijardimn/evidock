# Evidock Launch Score: stable rubric v0.6

**Launch Score measures repository launch readiness, not code quality, product quality, security, or completeness.**

Every criterion has one state: `PASS` earns full listed points; `FAIL`, `N_A`, and `UNKNOWN` earn 0. `UNKNOWN` may make the audit provisional when missing scope could materially flip criteria. **N_A is not PASS. No vacuous points. No partial points.**

## Discovery: 20
1. +5 `discovery.purpose`: Purpose at the Front Door.
2. +4 `discovery.user`: User/use case explicit.
3. +5 `discovery.value`: Concrete outcome/value explicit.
4. +4 `discovery.differentiation`: Reason to choose it explicit.
5. +2 `discovery.identity`: Repository identity coherent.

Source hidden behind the Front Door cannot satisfy criteria 1 through 4.

## Demonstration: 20
+5 real proof exists; +5 core capability demonstrated; +5 proof easy to reach; +5 proof credible.

## Quick Start: 20
+5 prerequisites explicit; +5 installation/setup explicit; +5 first-use action explicit; +5 short path to value.

## Documentation: 15
+5 core usage; +5 important behavior/config; +5 deeper information navigable.

## Trust: 15
+3 license; +3 verification signal; +3 maintenance/release process; +3 consequential public claims stay within evidence; +3 collaboration/support expectation.

## Polish: 10
+2 no shipped generated noise; +2 primary files intentional; +2 Front Door local references resolve; +2 naming consistent; +2 Front Door has identity + purpose/value + next step.

For every criterion record `status`, `points`, `max_points`, `prerequisite`, and concise evidence. Launch Status is independent from numeric score. Arithmetic: 20 + 20 + 20 + 15 + 15 + 10 = **100**.
