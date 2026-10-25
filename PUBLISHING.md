# Publishing checklist

Before public promotion of RepoReel v0.8.0:

1. Confirm `main` contains version `0.8.0` in the Skill and both Claude plugin manifests.
2. Confirm the repository topics remain: `agent-skills`, `claude`, `claude-code`, `developer-tools`, `github`, `readme`, `repository`, `open-source`, `audit`, `llm`, `ai-agents`.
3. Run:

```bash
python -m unittest discover -s tests -v
python tools/smoke_test.py
python tools/lint_evals.py
```

4. Confirm the full GitHub Actions matrix is green on Linux, Windows and macOS with Python 3.9 and latest.
5. Run `python tools/package_skill.py` locally when you want a local copy of `dist/reporeel.zip`.
6. Create/tag the GitHub Release as `v0.8.0` and use `launch/release-v0.8.0.md` as the release-note baseline.
7. After the Release is published, the `package-skill` workflow validates the Skill again and automatically attaches:
   - `reporeel-v0.8.0.zip`
   - `reporeel-v0.8.0.zip.sha256`
8. Confirm both release assets appear and the package workflow is green before sharing the Release URL.
9. Verify Claude.ai/Desktop upload from the exact Release ZIP.
10. Verify Claude Code installation from a clean environment:

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

11. Verify the v0.8 loop once end-to-end on a repository other than RepoReel itself:
   - URL/local repo roast
   - baseline Launch Score
   - Fix Mode on launch-surface issues
   - re-audit
   - diff
   - badge generation
12. Publish only claims that the release itself proves. Do not manufacture usage/adoption metrics.

Repository: https://github.com/davijardimn/reporeel
