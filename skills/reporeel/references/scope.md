# Scope and Completeness v0.6

Scope kinds: `local_worktree`, `uploaded_archive`, `partial_files`, `connected_repository`, `unknown`.
Completeness: `complete_for_artifact`, `partial`, `unknown`.

Mark `provisional: true` only when missing/uninspected scope could plausibly change scored criteria.

An uploaded ZIP may be complete_for_artifact and receive a non-provisional score for what was shipped while still not proving that an upstream repository lacks additional files.

Say `README not observed in the supplied archive.` not `This project has no README anywhere.`

Ignore the **contents** of local/generated folders such as `.venv/`, `node_modules/`, `__pycache__/`, caches, and build outputs during source analysis. Do **not** ignore the fact that they were shipped; their presence is hygiene evidence.
