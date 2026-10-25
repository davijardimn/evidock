# Evidock Badge

The badge is a compact, shareable Launch Score artifact for repository READMEs.

## Source of truth

The badge must be rendered from a **validated `audit.json`**. It never re-scores, rounds upward, changes Launch Status, or hides `provisional=true`.

```bash
python3 <skill-directory>/scripts/render_badge.py \
  --audit .evidock/audit.json \
  --output .evidock/badge.svg \
  --markdown-output .evidock/badge.md
```

By default the generated Markdown links to the Evidock repository so someone who sees the badge can discover the tool. Use `--target-url` when another explicit destination is more appropriate. `--asset-path` defaults to `.evidock/badge.svg`.

The badge displays Evidock identity, Launch Score, Launch Status, and `PROVISIONAL` when the audit is provisional. It is **not** a certification of code quality, security, product quality, production readiness, or compatibility.

Do not hand-edit the badge to show a better score/status. If the repository changes materially, re-audit and regenerate it. Evidock does not require a hosted badge service, tracking pixel, analytics endpoint, or external account.
