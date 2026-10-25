# GitHub URL Roast

RepoReel v0.8 can audit a GitHub repository from a URL without requiring the user to download a ZIP first.

## Acquisition order

Use the strongest read-only source available:

1. A connected GitHub/repository tool that can read the target repository.
2. `scripts/inspect_github.py` when Python + network access are available.
3. User-provided repository files/archive when the URL cannot be accessed.

Do not pretend an inaccessible URL was inspected.

## Deterministic collector

```bash
python3 <skill-directory>/scripts/inspect_github.py \
  --repo https://github.com/owner/repo \
  --output <working-dir>/github-evidence.json
```

The collector is standard-library-only, read-only, and restricted to `https://github.com` / `api.github.com`. It records repository metadata, the resolved ref/commit, a bounded tree summary, selected Front Door files, workflow metadata, recent release metadata, and limitations.

It uses `GITHUB_TOKEN` when already present in the environment. Never ask the user to paste a token into chat, never echo the token, and never put it in an evidence artifact.

## Evidence boundary

A URL roast is **remote static inspection** unless a local copy is also available.

Remote evidence may support:
- repository description/topics/license
- README and top-level Front Door claims
- presence of CI workflow definitions
- release metadata
- file/tree structure
- deterministic documentation/metadata findings

Remote evidence does **not** by itself prove:
- that install/run commands succeed
- runtime behavior
- cross-platform compatibility
- performance/benchmarks
- production readiness

A public CI workflow being present is a process signal, not proof that the current repository state passed in every environment. If actual run status is accessible, cite the exact run/commit and keep the scope narrow.

If the returned tree or a Front Door file is truncated/unavailable, record that limitation. Do not convert uninspected scope into confirmed absence.

## Proof Mode

Do not call a remote URL inspection `Proof Mode`. Runtime proof requires a controlled executable copy of the relevant project and the normal Proof Mode safety contract. If only the remote repository is available, keep runtime claims UNKNOWN/INFERRED as appropriate.

## Score discipline

GitHub popularity signals such as stars/forks are context only. They never award Launch Score points and must not be used as a proxy for product quality or launch readiness.
