# Evidock: deterministic launch-readiness audits for repositories as an Agent Skill

Evidock is an open-source Agent Skill that separates repository launch readiness from generic code quality.

The core model is evidence-first: Front Door inspection, claim states (VERIFIED / INFERRED / UNKNOWN / CONTRADICTED), scoped Proof Mode, a deterministic 100-point rubric where only PASS earns points, evidence-preserving Fix Mode, and validated shareable artifacts.

v0.9.0 also accepts GitHub URLs through bounded read-only inspection. Remote inspection is never promoted to runtime proof.

The audit schema/rubric remains v0.6 for historical diff compatibility even though the Skill version is v0.9.0.

Everything agent-facing is Python standard library only, with cross-platform tests and behavioral evals.

https://github.com/davijardimn/evidock
