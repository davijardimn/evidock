# Fix Mode

Fix Mode turns an Evidock diagnosis into a minimal, evidence-preserving launch improvement loop.

## Contract

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

When filesystem access exists, preserve the baseline as `.evidock/before.audit.json` before editing and write the post-fix result as `.evidock/after.audit.json`.

Prefer launch-surface changes: README/front-door copy, install/quick-start documentation, docs navigation, broken local documentation/demo references, repository-facing metadata/configuration when clearly safe, `.gitignore`/generated-noise guidance, contribution/support/release guidance, and demo/example presentation using real existing behavior.

Keep patches small and explain which failed criterion/blocker each change addresses.

## Product behavior boundary

Do **not** silently implement missing product features just to raise Launch Score. If a public claim is CONTRADICTED because the product does not implement it, the default launch fix is to make the public claim truthful. Implementing the missing feature is a separate product-development task and requires explicit user intent.

## No score gaming

Never improve the score by relaxing/rewording rubric criteria, marking failures `N_A`, deleting evidence solely to hide a failure, fabricating screenshots/metrics/testimonials/users/benchmarks/compatibility, claiming Proof Mode ran when it did not, removing truthful limitations, or changing audit arithmetic without changing underlying evidence.

The evidence must improve before the score improves.

## Re-audit and diff

After verification, perform a fresh audit using the same `rubric_version`:

```bash
python3 <skill-directory>/scripts/render_diff.py \
  --before .evidock/before.audit.json \
  --after .evidock/after.audit.json \
  --output .evidock/diff.svg
```

Report both wins and unresolved failures. A truthful zero-delta fix is better than manufactured progress.
