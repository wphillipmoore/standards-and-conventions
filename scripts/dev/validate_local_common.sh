#!/usr/bin/env bash
# Managed by standard-tooling — DO NOT EDIT in downstream repos.
# Canonical source: https://github.com/wphillipmoore/standard-tooling
# validate_local_common.sh — shared checks run for ALL repos.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

run() {
  echo "Running: $*"
  "$@"
}

# -- required tools ----------------------------------------------------------

missing=()
command -v shellcheck >/dev/null 2>&1 || missing+=("shellcheck")
command -v markdownlint >/dev/null 2>&1 || missing+=("markdownlint")
command -v repo-profile >/dev/null 2>&1 || missing+=("repo-profile (standard-tooling)")
command -v markdown-standards >/dev/null 2>&1 || missing+=("markdown-standards (standard-tooling)")

if [[ ${#missing[@]} -gt 0 ]]; then
  echo "ERROR: required tools not found: ${missing[*]}" >&2
  exit 1
fi

# -- repo profile validation -------------------------------------------------

run repo-profile

# -- markdown lint -----------------------------------------------------------

run markdown-standards

# -- shellcheck on all shell scripts -----------------------------------------

shell_files=()
while IFS= read -r f; do
  shell_files+=("$f")
done < <(find "$repo_root/scripts" -type f -name '*.sh' 2>/dev/null)

if [[ ${#shell_files[@]} -gt 0 ]]; then
  run shellcheck "${shell_files[@]}"
fi
