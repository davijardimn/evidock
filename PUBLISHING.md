# Publishing checklist

Before the first public GitHub release:

1. Create the public repository `davijardimn/reporeel`.
2. Use this repository description: `Evidence-first Agent Skill that roasts, proves, scores, and improves how launch-ready software repositories are.`
3. Add topics: `agent-skills`, `claude`, `claude-code`, `developer-tools`, `github`, `readme`, `repository`, `open-source`, `audit`.
4. Run:

```bash
python -m unittest discover -s tests -v
python tools/smoke_test.py
python tools/lint_evals.py
```

5. Run `python tools/package_skill.py` and attach `dist/reporeel.zip` to the GitHub Release.
6. Tag the release `v0.7.0`.
7. Verify Claude.ai upload from the release ZIP.
8. Verify Claude Code installation with:

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

9. Capture one real end-to-end demo for the README without exposing private project data.
10. Publish only claims that the release itself proves.

Repository: https://github.com/davijardimn/reporeel
