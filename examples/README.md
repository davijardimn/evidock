# Examples

The bundled examples are synthetic so they can be shared safely.

- `before.audit.json` — a repository with almost no launch surface
- `after.audit.json` — the same fictional project after documentation/proof/trust improvements
- `self.audit.json` — an Evidock self-audit fixture

Generate artifacts:

```bash
python skills/evidock/scripts/render_card.py --audit examples/before.audit.json --output /tmp/card.svg
python skills/evidock/scripts/render_diff.py --before examples/before.audit.json --after examples/after.audit.json --output /tmp/diff.svg
```
