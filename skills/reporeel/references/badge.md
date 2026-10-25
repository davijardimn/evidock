# RepoReel Badge

The v0.8 badge is a compact, shareable Launch Score artifact for repository READMEs.

## Source of truth

The badge must be rendered from a **validated `audit.json`**. It never re-scores, rounds upward, changes Launch Status, or hides `provisional=true`.

```bash
python3 <skill-directory>/scripts/render_badge.py \
  --audit .reporeel/audit.json \
  --output .reporeel/badge.svg \
  --markdown-output .reporeel/badge.md
```

By default the generated Markdown links to the RepoReel repository so someone who sees the badge can discover the tool. Use `--target-url` when another explicit destination is more appropriate.

`--asset-path` controls the image path written into the Markdown snippet. It defaults to `.reporeel/badge.svg`.

## Meaning

The badge displays:
- RepoReel identity
- Launch Score
- Launch Status
- `PROVISIONAL` when the audit is provisional

It is **not** a certification of code quality, security, product quality, production readiness, or compatibility. It is a snapshot of repository launch readiness under the stated audit scope and rubric version.

## Integrity

Do not hand-edit the badge to show a better score/status. If the repository changes materially, re-audit and regenerate it.

The badge is intentionally static and dependency-free. RepoReel does not require a hosted badge service, tracking pixel, analytics endpoint, or external account.
