#!/usr/bin/env python3
"""Resolve context-bootstrap include paths and emit ordered path list."""

from __future__ import annotations

import argparse
import os
import sys
STANDARDS_PREFIX = "../standards-and-conventions/"


class MissingInclude(Exception):
    def __init__(self, path: str, source: str | None = None) -> None:
        self.path = path
        self.source = source
        message = f"Missing include: {path}"
        if source:
            message = f"{message} (referenced from: {source})"
        super().__init__(message)


def is_absolute(path: str) -> bool:
    return path.startswith("/") or path.startswith("~")


def strip_include(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("\"") and raw.endswith("\""):
        return raw[1:-1]
    if raw.startswith("<") and raw.endswith(">"):
        return raw[1:-1]
    return raw


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def resolve_include(repo_root: str, include_path: str) -> str | None:
    if not include_path:
        return None

    if is_absolute(include_path):
        return os.path.abspath(os.path.expanduser(include_path))

    if include_path.startswith(STANDARDS_PREFIX):
        local_path = os.path.abspath(os.path.join(repo_root, include_path))
        if os.path.isfile(local_path):
            return local_path
        return None

    repo_candidate = os.path.abspath(os.path.join(repo_root, include_path))
    if os.path.isfile(repo_candidate):
        return repo_candidate

    standards_candidate = os.path.abspath(
        os.path.join(repo_root, "../standards-and-conventions", include_path)
    )
    if os.path.isfile(standards_candidate):
        return standards_candidate
    return None


def iter_includes(content: str) -> list[str]:
    includes: list[str] = []
    for line in content.splitlines():
        if line.startswith("#include ") or line.startswith("#include\t"):
            include_path = strip_include(line[len("#include") :])
            includes.append(include_path)
    return includes


def resolve_chain(repo_root: str) -> list[tuple[str, str]]:
    ordered: list[tuple[str, str]] = []
    seen: set[str] = set()
    standards_repo_present = os.path.isdir(
        os.path.abspath(os.path.join(repo_root, "../standards-and-conventions"))
    )
    if not standards_repo_present:
        raise MissingInclude(os.path.abspath(os.path.join(repo_root, "../standards-and-conventions")))

    def process(path: str, source: str | None = None) -> None:
        if path in seen:
            return
        seen.add(path)
        try:
            content = read_text(path)
        except FileNotFoundError:
            raise MissingInclude(path, source=source)
        ordered.append((path, content))
        for include_path in iter_includes(content):
            resolved = resolve_include(repo_root, include_path)
            if resolved is None:
                raise MissingInclude(include_path, source=path)
            process(resolved, source=path)

    home_agents = os.path.expanduser("~/AGENTS.md")
    if os.path.isfile(home_agents):
        process(os.path.abspath(home_agents))

    repo_agents = os.path.abspath(os.path.join(repo_root, "AGENTS.md"))
    if os.path.isfile(repo_agents):
        process(repo_agents)

    return ordered


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve context-bootstrap includes and emit ordered path list."
    )
    parser.add_argument(
        "--repo-root",
        default=os.getcwd(),
        help="Repository root for resolving relative includes (default: current working directory).",
    )
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.expanduser(args.repo_root))

    try:
        ordered = resolve_chain(repo_root)
    except MissingInclude as exc:
        raise SystemExit(str(exc))

    for path, _content in ordered:
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
