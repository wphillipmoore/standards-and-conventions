# Pull Request Workflow

## Table of Contents
- [Purpose](#purpose)
- [Docs-Only Exception](#docs-only-exception)
- [Issue linkage](#issue-linkage)
- [Pre-Submission Requirements](#pre-submission-requirements)
- [Pre-Submission Checklist](#pre-submission-checklist)
- [What to Do When Checks Fail](#what-to-do-when-checks-fail)
- [Pull Request Finalization](#pull-request-finalization)

## Purpose
Pull requests must pass all automated checks before submission. CI is a
backstop, not a substitute for developer diligence.

Submitting failing PRs wastes reviewer time, pollutes history, and undermines
confidence in the codebase.

## Docs-Only Exception
Documentation-only changes may skip the unit test suite and coverage checks
when the diff includes only documentation files.

Define "docs-only" for the repository (for example: files under `docs/` plus
top-level `README.md` and `CHANGELOG.md`).

When using this exception, explicitly state `Docs-only: tests skipped` in the
PR description and list the files changed.

## Issue linkage
When a pull request resolves a tracked issue, include a closing keyword in the
PR description so the issue auto-closes on merge (for example, `Fixes #123`).
If auto-close is not possible, the PR must still reference the issue and the
issue must be closed manually after merge. Work is not complete until the
issue is closed.

## Pre-Submission Requirements
Before creating a pull request, all of the following must be met unless the
docs-only exception applies:
1. 100 percent unit test success
2. Coverage must not decline (lines and branches)
3. All code quality checks must pass

Each repository must document its canonical local validation command. If one
exists, it is the required pre-submission run.

## Pre-Submission Checklist
Use the repository's canonical validation command when available.

If no single command exists, run:
- full test suite
- linting
- type checking
- coverage

Do not run only a subset of tests. Local validation should mirror CI hard
gates.

## What to Do When Checks Fail
If any check fails:
1. do not create the PR
2. fix the failing tests or checks
3. re-run the full checklist
4. proceed only when everything passes

Common mistakes to avoid:
- "I only changed one area, so I only ran those tests"
- "The test failures are pre-existing"
- "I will fix it in a follow-up PR"

## Pull Request Finalization
After merge approval, finalize the PR in this order:
1. merge the PR and delete the remote branch
2. update local copy of the target branch
3. synchronize the local environment with dependency specifications
4. delete the local feature branch and prune stale remotes
5. run final validation (skip for docs-only PRs)

Do not reuse old branch names.
