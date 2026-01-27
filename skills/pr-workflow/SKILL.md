---
name: pr-workflow
description: Guide pull request creation, submission, and finalization using the canonical PR workflow, including the docs-only exception.
---

# PR workflow

## Table of Contents
- [Overview](#overview)
- [Preflight](#preflight)
- [Docs-only determination](#docs-only-determination)
- [Pre-submission steps](#pre-submission-steps)
- [Submission and finalization](#submission-and-finalization)
- [Resources](#resources)

## Overview
Execute the pull request workflow with required validations and checkpoints.
Follow local overrides (AGENTS or repo-specific standards) when present.

## Preflight
- Confirm you are working on a short-lived branch per branching rules.
- If no primary issue exists, create one immediately using best-effort
  assumptions and note them in the issue body. Do not ask for an issue number
  unless acceptance criteria are materially ambiguous.
- Locate the pull request template at `.github/pull_request_template.md`.
- Ensure commit message format and AI co-authorship requirements are met per
  the commit standards and the repo's approved AI identity list.

## Docs-only determination
- Identify whether the change set is "docs-only" as defined by the repository.
- If the repository does not define a docs-only rule, ask for it before
  applying the exception.
- When using the docs-only exception, include `Docs-only: tests skipped` in the
  PR description and list the files changed.

## Pre-submission steps
1. Run the repository's canonical validation command if documented.
2. If no canonical command exists, ask for the required validation steps.
3. If any check fails, do not submit the PR; fix and rerun the full checks.
4. Populate the pull request template fields.
5. Include issue linkage when required.

## Submission and finalization
- Submit the PR only after all required checks pass (unless docs-only
  exception applies).
- Follow repository-specific confirmation checkpoints if defined in AGENTS.
- Auto-merge is the default unless the PR has a `manual-merge` label or the
  repository disables auto-merge.
- If auto-merge is enabled, do not attempt manual merge. Wait for required
  checks to pass and for the merge to complete.
- After merge approval or completion, finalize in order:
  1. Merge the PR and delete the remote branch (or confirm auto-merge completed).
  2. Update the local copy of the target branch.
  3. Synchronize the local environment with dependency specifications.
  4. Delete the local feature branch and prune stale remotes.
  5. Run final validation (skip for docs-only PRs).

## Resources
- `docs/code-management/pull-request-workflow.md`
- `docs/code-management/branching-and-deployment.md`
- `docs/code-management/commit-messages-and-authorship.md`
- `docs/standards-and-conventions.md`
