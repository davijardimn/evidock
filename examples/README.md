# Examples

The bundled examples are synthetic so they can be shared safely.

- `before.audit.json` — a repository with almost no launch surface
- `after.audit.json` — the same fictional project after documentation/proof/trust improvements

The rendered before/after artifacts used in the main README live under `docs/images/`.

Generate them yourself:

```bash
python skills/reporeel/scripts/render_card.py --audit examples/before.audit.json --output /tmp/card.svg
python skills/reporeel/scripts/render_diff.py --before examples/before.audit.json --after examples/after.audit.json --output /tmp/diff.svg
```
