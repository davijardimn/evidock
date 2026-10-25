# Publishing checklist

Before public promotion of Evidock v0.9.2:

1. Confirm the GitHub repository is `davijardimn/evidock`.
2. Use the repository description: `Evidence-first Agent Skill that audits, proves, scores, and fixes how launch-ready software repositories are.`
3. Keep topics such as `agent-skills`, `claude`, `claude-code`, `developer-tools`, `github`, `readme`, `repository`, `open-source`, `audit`, `llm`, `ai-agents`.
4. Run `python -m unittest discover -s tests -v`, `python tools/smoke_test.py`, and `python tools/lint_evals.py`.
5. Confirm the full GitHub Actions matrix is green on Linux, Windows and macOS.
6. Create GitHub Release `v0.9.2` and confirm the package workflow attaches `evidock-v0.9.2.zip` plus its SHA-256 file.
7. Verify the exact Release ZIP and confirm only the intentional legacy alias in `SKILL.md` still mentions RepoReel.
8. Verify Claude Code installation from a clean environment:

```text
/plugin marketplace add davijardimn/evidock
/plugin install evidock@evidock
```

9. Verify the exact Release ZIP in Claude.ai or Claude Desktop.
10. Run the complete loop on an unrelated repository: URL/local roast → baseline Launch Score → Fix Mode → re-audit → diff → badge.
11. Publish only claims the release itself proves. Do not manufacture adoption metrics.

Repository: https://github.com/davijardimn/evidock
