# Standards and Conventions Repository Standards

## Table of Contents

- [External tooling dependencies](#external-tooling-dependencies)
- [CI gates](#ci-gates)
- [Local deviations](#local-deviations)

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
