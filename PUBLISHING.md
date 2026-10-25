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
5. Run `python tools/package_skill.py` and attach `dist/reporeel.zip` to the GitHub Release.
6. Tag the release `v0.8.0` and use `launch/release-v0.8.0.md` as the release-note baseline.
7. Verify Claude.ai/Desktop upload from the exact release ZIP.
8. Verify Claude Code installation from a clean environment:

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

9. Verify the v0.8 loop once end-to-end:
   - URL/local repo roast
   - baseline Launch Score
   - Fix Mode on launch-surface issues
   - re-audit
   - diff
   - badge generation
10. Publish only claims that the release itself proves. Do not manufacture usage/adoption metrics.

Repository: https://github.com/davijardimn/reporeel
