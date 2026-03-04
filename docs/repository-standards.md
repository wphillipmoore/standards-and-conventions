# Standards and Conventions Repository Standards

## Table of Contents

- [AI co-authors](#ai-co-authors)
- [Repository profile](#repository-profile)
- [Validation policy](#validation-policy)
- [External tooling dependencies](#external-tooling-dependencies)
- [CI gates](#ci-gates)
- [Local deviations](#local-deviations)

## AI co-authors

- Co-Authored-By: wphillipmoore-codex <255923655+wphillipmoore-codex@users.noreply.github.com>
- Co-Authored-By: wphillipmoore-claude <255925739+wphillipmoore-claude@users.noreply.github.com>

## Repository profile

- repository_type: documentation
- versioning_scheme: library
- branching_model: library-release
- release_model: artifact-publishing
- supported_release_lines: 1.1
- primary_language: none

## Validation policy

- canonical_local_validation_command: markdown-standards
- validation_required: yes (markdownlint required)

## External tooling dependencies

- markdownlint (markdownlint-cli)

## CI gates

Hard gates (required status checks on `develop`):

- Standards compliance (`.github/workflows/ci.yml` via `standard-actions`):
  - Repository profile validation (`repo-profile`)
  - Markdownlint (`markdown-standards`)
  - Issue linkage validation (`pr-issue-linkage`)

Local hard gates (pre-commit hooks from `standard-tooling`):

- Branch naming enforcement: branching-model-aware prefix validation.

## Local deviations

- None.
