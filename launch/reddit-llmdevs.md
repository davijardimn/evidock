# r/LLMDevs draft

## Suggested title

Open-sourced RepoReel: an Agent Skill with deterministic repo launch scoring + scoped runtime proof

## Post

I open-sourced a developer-tool Skill called **RepoReel**.

Most agent-based repo reviews I tried eventually blurred into generic code review or subjective “this README feels like 7/10” feedback. RepoReel takes a narrower approach: evaluate **repository launch readiness** and require evidence for every scored point.

A few design decisions:

- Front Door is scored separately from facts hidden in implementation.
- Public claims are VERIFIED / INFERRED / UNKNOWN / CONTRADICTED.
- Runtime checks use a scoped Proof Mode and cannot silently become “works everywhere” claims.
- The 100-point score is recomputed from PASS / FAIL / N_A / UNKNOWN criteria; only PASS gets points.
- `audit.json` is the source of truth; card/report/diff renderers validate against it instead of re-scoring.
- Shareable output redacts secrets and unnecessary personal data.
- The Skill ships with a 32-pattern launch anti-pattern library plus behavioral evals.

The current scripts are Python standard-library-only, and CI runs on Linux, Windows and macOS.

It is MIT licensed and free/open source:
https://github.com/davijardimn/reporeel

I would be interested in feedback from people building agent skills: where would you draw the boundary between model judgment and deterministic tooling in this kind of review workflow?
