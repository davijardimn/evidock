#!/usr/bin/env python3
"""Collect read-only GitHub repository evidence for RepoReel URL Roast.

Standard library only. The script only contacts api.github.com and never writes
or prints the value of GITHUB_TOKEN.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"
NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
MAX_TREE_FILES = 20000
DEFAULT_MAX_CONTENT_FILES = 8
DEFAULT_MAX_FILE_BYTES = 128 * 1024

FRONT_DOOR_NAMES = (
    "README.md", "README.rst", "README.txt", "README",
    "CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md", "CHANGELOG.md",
    "CODE_OF_CONDUCT.md", "LICENSE", "LICENSE.md",
)
MANIFEST_NAMES = (
    "pyproject.toml", "package.json", "requirements.txt", "setup.py",
    "setup.cfg", "Cargo.toml", "go.mod", "Gemfile", "composer.json",
    "pom.xml", "build.gradle", "build.gradle.kts",
)


def parse_repo(value: str) -> tuple[str, str]:
    """Parse owner/repo or a github.com URL. Extra URL path is ignored."""
    raw = value.strip()
    if not raw:
        raise ValueError("repository value is empty")
    if "://" not in raw:
        parts = [p for p in raw.strip("/").split("/") if p]
        if len(parts) != 2:
            raise ValueError("expected owner/repo or https://github.com/owner/repo")
        owner, repo = parts
    else:
        u = urlsplit(raw)
        if u.scheme != "https" or (u.hostname or "").lower() not in {"github.com", "www.github.com"}:
            raise ValueError("only https://github.com repository URLs are supported")
        parts = [p for p in u.path.split("/") if p]
        if len(parts) < 2:
            raise ValueError("GitHub URL must include owner and repository")
        owner, repo = parts[0], parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not NAME_RE.fullmatch(owner) or not NAME_RE.fullmatch(repo):
        raise ValueError("owner/repository contains unsupported characters")
    if owner in {".", ".."} or repo in {".", ".."}:
        raise ValueError("invalid owner/repository")
    return owner, repo


def _api_get(path: str, token: str | None = None, optional: bool = False):
    if not path.startswith("/"):
        raise ValueError("API path must be absolute")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "RepoReel/0.8",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(API_ROOT + path, headers=headers, method="GET")
    try:
        with urlopen(req, timeout=20) as response:
            return json.load(response)
    except HTTPError as exc:
        if optional and exc.code in {403, 404, 409, 422}:
            return None
        detail = ""
        try:
            payload = json.loads(exc.read().decode("utf-8", "replace"))
            detail = str(payload.get("message") or "")
        except Exception:
            pass
        suffix = f": {detail}" if detail else ""
        raise RuntimeError(f"GitHub API returned HTTP {exc.code}{suffix}") from None
    except URLError as exc:
        raise RuntimeError(f"GitHub API connection failed: {exc.reason}") from None


def _selected_paths(tree: list[dict], max_files: int) -> list[str]:
    blobs = [x.get("path", "") for x in tree if x.get("type") == "blob"]
    by_lower = {p.lower(): p for p in blobs}
    selected: list[str] = []

    def add(path: str | None) -> None:
        if path and path not in selected and len(selected) < max_files:
            selected.append(path)

    for name in FRONT_DOOR_NAMES:
        add(by_lower.get(name.lower()))
    for name in MANIFEST_NAMES:
        add(by_lower.get(name.lower()))
    return selected


def _read_content(owner: str, repo: str, path: str, ref: str, token: str | None, max_bytes: int) -> dict:
    encoded_path = "/".join(quote(part, safe="") for part in path.split("/"))
    data = _api_get(
        f"/repos/{quote(owner, safe='')}/{quote(repo, safe='')}/contents/{encoded_path}?ref={quote(ref, safe='')}",
        token,
        optional=True,
    )
    item = {"path": path, "content": None, "truncated": False, "unavailable": False}
    if not isinstance(data, dict) or data.get("type") != "file":
        item["unavailable"] = True
        return item
    if data.get("encoding") != "base64" or not isinstance(data.get("content"), str):
        item["unavailable"] = True
        return item
    raw = base64.b64decode(data["content"], validate=False)
    if len(raw) > max_bytes:
        raw = raw[:max_bytes]
        item["truncated"] = True
    item["content"] = raw.decode("utf-8", "replace")
    item["size"] = int(data.get("size") or len(raw))
    return item


def inspect(repo_value: str, ref: str | None, max_content_files: int, max_file_bytes: int) -> dict:
    owner, repo = parse_repo(repo_value)
    token = os.environ.get("GITHUB_TOKEN") or None
    owner_q, repo_q = quote(owner, safe=""), quote(repo, safe="")
    meta = _api_get(f"/repos/{owner_q}/{repo_q}", token)
    resolved_ref = ref or meta.get("default_branch")
    if not resolved_ref:
        raise RuntimeError("repository has no resolvable default branch")
    commit = _api_get(f"/repos/{owner_q}/{repo_q}/commits/{quote(str(resolved_ref), safe='')}", token)
    tree_sha = (((commit or {}).get("commit") or {}).get("tree") or {}).get("sha")
    if not tree_sha:
        raise RuntimeError("could not resolve repository tree")
    tree_data = _api_get(f"/repos/{owner_q}/{repo_q}/git/trees/{tree_sha}?recursive=1", token)
    tree = tree_data.get("tree") if isinstance(tree_data, dict) else []
    if not isinstance(tree, list):
        tree = []
    tree_was_truncated = bool(tree_data.get("truncated")) if isinstance(tree_data, dict) else False
    if len(tree) > MAX_TREE_FILES:
        tree = tree[:MAX_TREE_FILES]
        tree_was_truncated = True

    paths = [x.get("path") for x in tree if x.get("path")]
    selected = _selected_paths(tree, max_content_files)
    files = [_read_content(owner, repo, p, str(resolved_ref), token, max_file_bytes) for p in selected]
    releases = _api_get(f"/repos/{owner_q}/{repo_q}/releases?per_page=5", token, optional=True)
    workflows = _api_get(f"/repos/{owner_q}/{repo_q}/actions/workflows?per_page=100", token, optional=True)

    workflow_items = []
    if isinstance(workflows, dict):
        for w in workflows.get("workflows") or []:
            workflow_items.append({"name": w.get("name"), "path": w.get("path"), "state": w.get("state")})

    release_items = []
    if isinstance(releases, list):
        for r in releases[:5]:
            release_items.append({
                "tag_name": r.get("tag_name"),
                "name": r.get("name"),
                "draft": bool(r.get("draft")),
                "prerelease": bool(r.get("prerelease")),
                "published_at": r.get("published_at"),
            })

    top_level = sorted({p.split("/", 1)[0] for p in paths if p})
    root_noise = sorted(
        p for p in paths
        if p in {".DS_Store", "Thumbs.db"}
        or p.split("/", 1)[0] in {".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}
    )[:100]

    return {
        "schema_version": "0.8",
        "source": {
            "kind": "github_url",
            "url": f"https://github.com/{owner}/{repo}",
            "owner": owner,
            "repository": repo,
            "ref": str(resolved_ref),
            "commit_sha": commit.get("sha") if isinstance(commit, dict) else None,
            "read_only": True,
        },
        "repository": {
            "name": meta.get("name"),
            "full_name": meta.get("full_name"),
            "description": meta.get("description"),
            "homepage": meta.get("homepage"),
            "topics": meta.get("topics") or [],
            "license": (meta.get("license") or {}).get("spdx_id") if isinstance(meta.get("license"), dict) else None,
            "default_branch": meta.get("default_branch"),
            "visibility": meta.get("visibility"),
            "archived": bool(meta.get("archived")),
            "fork": bool(meta.get("fork")),
            "stargazers_count": meta.get("stargazers_count"),
            "forks_count": meta.get("forks_count"),
            "open_issues_count": meta.get("open_issues_count"),
            "created_at": meta.get("created_at"),
            "updated_at": meta.get("updated_at"),
            "pushed_at": meta.get("pushed_at"),
            "file_count_observed": sum(1 for x in tree if x.get("type") == "blob"),
            "top_level": top_level,
            "root_noise": root_noise,
            "tree_truncated": tree_was_truncated,
        },
        "front_door_files": files,
        "signals": {
            "workflows": workflow_items,
            "recent_releases": release_items,
        },
        "limitations": [
            "GitHub URL inspection is static and read-only.",
            "Remote inspection does not prove runtime behavior or cross-platform compatibility.",
            "Only a bounded set of Front Door files is embedded in this evidence object.",
            "Anonymous GitHub API rate limits may apply; GITHUB_TOKEN is used when present and is never emitted.",
        ],
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Collect read-only evidence from a public/private GitHub repository URL.")
    ap.add_argument("--repo", required=True, help="owner/repo or https://github.com/owner/repo")
    ap.add_argument("--output", help="write JSON evidence here")
    ap.add_argument("--ref", help="branch/tag/commit; defaults to repository default branch")
    ap.add_argument("--max-content-files", type=int, default=DEFAULT_MAX_CONTENT_FILES)
    ap.add_argument("--max-file-bytes", type=int, default=DEFAULT_MAX_FILE_BYTES)
    ap.add_argument("--parse-only", action="store_true", help="validate/normalize the repository value without network access")
    args = ap.parse_args()
    try:
        owner, repo = parse_repo(args.repo)
        if args.parse_only:
            print(json.dumps({"owner": owner, "repository": repo, "url": f"https://github.com/{owner}/{repo}"}, indent=2))
            return
        if not args.output:
            ap.error("--output is required unless --parse-only is used")
        if not 1 <= args.max_content_files <= 20:
            ap.error("--max-content-files must be between 1 and 20")
        if not 1024 <= args.max_file_bytes <= 1024 * 1024:
            ap.error("--max-file-bytes must be between 1024 and 1048576")
        result = inspect(args.repo, args.ref, args.max_content_files, args.max_file_bytes)
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"RepoReel GitHub evidence: {result['source']['url']} @ {result['source']['ref']} -> {out}")
    except (ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
