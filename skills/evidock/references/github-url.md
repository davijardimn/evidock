# GitHub URL Roast

Evidock can audit a GitHub repository from a URL without requiring the user to download a ZIP first.

Use the strongest read-only source available: a connected repository tool; otherwise `scripts/inspect_github.py` when Python + network are available; otherwise user-provided files/archive. Do not pretend an inaccessible URL was inspected.

```bash
python3 <skill-directory>/scripts/inspect_github.py \
  --repo https://github.com/owner/repo \
  --output <working-dir>/github-evidence.json
```

The collector is standard-library-only, read-only, and restricted to GitHub. It records repository metadata, resolved ref/commit, a bounded tree summary, selected Front Door files, workflow metadata, recent release metadata, and limitations. It may use an already-configured `GITHUB_TOKEN`; never ask the user to paste a token into chat or put it in an evidence artifact.

A URL roast is **remote static inspection** unless a local copy is also available. Remote evidence may support repository metadata, Front Door claims, CI definitions, release metadata, file/tree structure, and deterministic documentation findings. It does **not** by itself prove install/run success, runtime behavior, cross-platform compatibility, performance, benchmarks, or production readiness.

A workflow definition is a process signal, not proof that the current state passed everywhere. If actual run status is accessible, cite the exact run/commit and keep scope narrow. Truncated/unavailable files remain uninspected scope, not confirmed absence.

Do not call remote URL inspection `Proof Mode`. GitHub popularity signals such as stars/forks are context only and never award Launch Score points.
