# Fix Mode

Fix Mode turns a RepoReel diagnosis into a minimal, evidence-preserving launch improvement loop.

## Contract

The default loop is:

```text
baseline audit
    ↓
fix plan
    ↓
minimal patch
    ↓
verification
    ↓
re-audit
    ↓
before → after diff
```

When filesystem access exists, preserve the baseline as `.reporeel/before.audit.json` before editing and write the post-fix result as `.reporeel/after.audit.json`.

## What Fix Mode may change by default

Prefer launch-surface changes:
- README/front-door copy
- install/quick-start documentation
- docs navigation
- broken local documentation/demo references
- repository-facing metadata/configuration when clearly safe
- `.gitignore` / removal instructions for obvious generated noise
- contribution/support/release guidance
- demo/example presentation using real existing behavior

Keep patches small and explain which failed criterion/blocker each change addresses.

## Product behavior boundary

Do **not** silently implement missing product features just to raise Launch Score.

If a public claim is CONTRADICTED because the product does not implement it, the default launch fix is to make the public claim truthful. Implementing the missing feature is a separate product-development task and requires explicit user intent.

Do not modify application/security behavior in ordinary Fix Mode unless the user explicitly asks for that implementation work and it is safe to do so.

## No score gaming

Never improve the score by:
- relaxing or rewriting rubric criteria
- marking failures `N_A`
- deleting evidence solely to hide a failure
- fabricating screenshots, metrics, testimonials, users, benchmarks or compatibility
- claiming Proof Mode ran when it did not
- removing a truthful limitation just because it hurts presentation
- changing `audit.json` arithmetic without changing underlying evidence

The evidence must improve before the score improves.

## Verification after patching

Re-run the smallest checks that can validate the changed launch surface. Examples:
- local README/reference validation
- documented command syntax
- safe quick-start Proof Mode when available
- claim verification for rewritten claims
- artifact validation

A documentation-only fix must not be presented as runtime proof.

## Re-audit and diff

After verification, perform a fresh audit using the same `rubric_version`. Then generate the diff:

```bash
python3 <skill-directory>/scripts/render_diff.py \
  --before .reporeel/before.audit.json \
  --after .reporeel/after.audit.json \
  --output .reporeel/diff.svg
```

Report both wins and unresolved failures. If the score did not improve, say so; a truthful zero-delta fix is better than manufactured progress.
