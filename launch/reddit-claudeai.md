# r/ClaudeAI showcase draft

## Suggested title

I built an open-source Claude Skill that roasts whether a GitHub repo is actually ready to launch

## Post

I built **RepoReel**, a free/open-source Agent Skill for Claude that reviews a software repository from the perspective of someone discovering it for the first time.

The idea came from a problem I kept seeing in side projects: the code can be decent while the repository gives a stranger almost no reason to understand, trust, run, or share it.

RepoReel checks the repository “Front Door” first, then verifies claims in the README/docs against the implementation. When static inspection is not enough, its **Proof Mode** can run small non-destructive experiments and records exactly what environment was tested and what the result does *not* prove.

It then produces an auditable Launch Score from explicit PASS / FAIL / N_A / UNKNOWN criteria and can render a score card, HTML report, and before/after diff from the validated audit JSON.

Claude was part of the development loop too: I repeatedly ran the Skill against a Flask project, looked for places where the model became subjective or overclaimed evidence, then changed the rubric/scripts and reran the same test. That is how things like `N_A != PASS`, execution-scope limits, redaction rules, and artifact validation ended up in the project.

It is MIT licensed and completely free to try.

Claude Code install:

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

Then:

```text
Use RepoReel to roast this repository.
Use Proof Mode where it is safe and useful.
Generate the card and report too.
```

Repo: https://github.com/davijardimn/reporeel

I would especially like feedback on false positives/false negatives in the launch rubric and whether the resulting roast actually tells you what to fix first.
