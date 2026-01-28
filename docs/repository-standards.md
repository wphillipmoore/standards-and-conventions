# Standards and Conventions Repository Standards

## Table of Contents
- [AI co-authors](#ai-co-authors)
- [Repository profile](#repository-profile)
- [Validation policy](#validation-policy)
- [CI gates](#ci-gates)
- [Local deviations](#local-deviations)

## AI co-authors
- Co-Authored-By: wphillipmoore-codex <255923655+wphillipmoore-codex@users.noreply.github.com>
- Co-Authored-By: wphillipmoore-claude <255925739+wphillipmoore-claude@users.noreply.github.com>

## Repository profile
- repository_type: documentation
- versioning_scheme: none
- branching_model: docs-single-branch
- release_model: none
- supported_release_lines: none

## Validation policy
- canonical_local_validation_command: scripts/lint/markdown-standards.sh
- validation_required: yes (markdownlint required)

## CI gates
Hard gates (required status checks on `develop`):
- Standards compliance (`.github/workflows/standards-gates.yml`):
  - Repository profile validation (`scripts/lint/repo-profile.sh`)
  - Markdownlint (`scripts/lint/markdown-standards.sh`)
  - Commit message lint (`scripts/lint/commit-messages.sh`)
  - Issue linkage validation (`scripts/lint/pr-issue-linkage.sh`)

Local hard gates (pre-commit hooks):
- Branch naming enforcement (`scripts/git-hooks/pre-commit`): require `feature/*` or `bugfix/*`.
- Commit message lint (`scripts/git-hooks/commit-msg`): Conventional Commits required.

## Local deviations
- None.
