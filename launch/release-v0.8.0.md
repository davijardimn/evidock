# RepoReel v0.8.0: Close the launch loop

**Your code might be ready. Your repo probably isn't.**

RepoReel is an evidence-first Agent Skill for auditing how launch-ready a software repository is before you put it in front of GitHub, Reddit, Hacker News, or users.

v0.8.0 closes the core product loop:

```text
GitHub URL / local repo
        ↓
      ROAST
        ↓
       FIX
        ↓
      VERIFY
        ↓
     RE-AUDIT
        ↓
   DIFF + BADGE
```

## New in v0.8.0

### GitHub URL Roast

You can now give RepoReel a repository URL directly:

```text
Use RepoReel to roast https://github.com/owner/repo
```

The bundled `inspect_github.py` collector is read-only, standard-library-only, bounded, and restricted to GitHub. It records the exact ref/commit inspected and never turns remote static inspection into fake runtime proof.

### Evidence-preserving Fix Mode

Fix Mode now follows a strict loop:

- preserve baseline audit
- map fixes to blockers/failed criteria
- apply minimal launch-surface patches
- verify changed surfaces
- re-audit with the same rubric version
- render the before/after diff

RepoReel cannot raise the score by relaxing criteria, hiding failures, marking failures `N_A`, fabricating proof, or silently implementing missing product features solely to improve Launch Score.

### RepoReel Badge

`render_badge.py` generates a static SVG and ready-to-paste Markdown from validated `audit.json`:

```bash
python skills/reporeel/scripts/render_badge.py \
  --audit .reporeel/audit.json \
  --output .reporeel/badge.svg \
  --markdown-output .reporeel/badge.md
```

The badge displays Launch Score, Launch Status, and PROVISIONAL state when applicable. It is a launch-readiness snapshot, not a security or code-quality certification.

## Still included

- Front Door audit
- Claim Verification: VERIFIED / INFERRED / UNKNOWN / CONTRADICTED
- scoped Proof Mode
- deterministic 100-point Launch Score using PASS / FAIL / N_A / UNKNOWN
- Launch Status + prioritized blockers
- card.svg, report.html and before/after diff.svg
- 32-pattern Launch Pattern Library
- behavioral evals, smoke tests and cross-platform CI
- Claude Code marketplace metadata + packaged Skill ZIP

The stable audit/rubric schema remains v0.6 so compatible historical audits can still be compared.

## Install with Claude Code

```text
/plugin marketplace add davijardimn/reporeel
/plugin install reporeel@reporeel
```

Then:

```text
Use RepoReel to roast this repository.
Fix the launch blockers that are safe to fix.
Verify the changes, re-audit, and generate the diff and badge.
```

Or:

```text
Use RepoReel to roast https://github.com/owner/repo
```

## Philosophy

> Market the evidence. Never manufacture it.

Launch Score measures repository launch readiness. It does not measure code quality, product quality, security, compatibility, or product completeness.

Repository: https://github.com/davijardimn/reporeel
