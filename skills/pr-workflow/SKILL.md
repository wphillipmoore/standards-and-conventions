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
- [Submission](#submission)
- [Finalization](#finalization)
- [Resources](#resources)

## Overview

Execute the full pull request lifecycle: validate, submit, merge, and clean up.
This skill runs to completion without intermediate checkpoints. Auto-merge is
always enabled; CI gates are the sole merge authority.

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
5. Include issue linkage using `Fixes #N` (default; auto-closes issue on
   merge) or `Ref #N` (non-closing; use when acceptance criteria exist).
   These are the only accepted keywords — `Closes`, `Resolves`, and other
   GitHub keywords are rejected by CI.

## Submission

1. Push the branch and create the PR.
2. Enable auto-merge immediately. Do not attempt manual merge.
3. Wait for CI to pass and auto-merge to complete.

## Finalization

After the PR merges, finalize in order:

1. Update the local copy of the target branch.
2. Delete the local feature branch.
3. Prune stale remote-tracking references.
4. Synchronize the local environment with dependency specifications.
5. Run final validation (skip for docs-only PRs).

Finalization is mandatory. Do not stop after submission or ask for permission
to finalize.

## Resources

- `docs/code-management/pull-request-workflow.md`
- `docs/code-management/branching-and-deployment.md`
- `docs/code-management/commit-messages-and-authorship.md`
- `docs/standards-and-conventions.md`
