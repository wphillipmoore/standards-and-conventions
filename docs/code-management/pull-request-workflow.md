# Pull Request Workflow

## Purpose

Pull requests must pass all hard-gate automated checks before submission. CI
is a backstop, not a substitute for developer diligence. See
[CI gates](source-control-guidelines.md#ci-gates) for hard versus soft gate
definitions.

Submitting failing PRs wastes reviewer time, pollutes history, and undermines
confidence in the codebase.

## Docs-Only Exception

Documentation-only changes may skip the unit test suite and coverage checks
when the diff includes only documentation files.

Define "docs-only" for the repository (for example: files under `docs/` plus
top-level `README.md` and `CHANGELOG.md`).

When using this exception, explicitly state `Docs-only: tests skipped` in the
PR description and list the files changed.

Documentation repositories may define "docs-only" as the entire repository and
require markdownlint. Additional validation is optional unless the repository
documents a requirement. For documentation repositories with only markdownlint
required, do not ask for additional validation; proceed with PR submission.

CI workflows must implement the docs-only skip policy in
[source-control-guidelines.md](source-control-guidelines.md#docs-only-ci-skip-policy).
Markdownlint and any docs-only validation commands must still run even when
tests are skipped.

## Issue linkage

Every pull request must have a primary GitHub issue. If no issue exists,
create one before creating a branch or changing files.

If the issue has no special acceptance criteria, include a closing keyword in
the PR description so the issue auto-closes on merge (for example,
`Fixes #123`). If acceptance criteria exist, use a non-closing reference and
close the issue only after the criteria are satisfied. See
[GitHub Issue Standards](github-issues.md) for acceptance criteria rules and
sub-issue guidance.

## Pull request template

Every repository must install a pull request template at
`.github/pull_request_template.md` and keep it aligned with local workflow.

Minimum required template:

```text
# Pull Request

## Summary
- 

## Issue Linkage
- Fixes # (default; use when no acceptance criteria exist)
- Ref # (use when acceptance criteria exist)
- Work is not complete until the issue is closed.
- If no issue exists, open one before any work begins.

## Testing
- markdownlint
- <language-specific validation command, if applicable>
- <repo-specific validation command, if applicable>

## Notes
- 
```

The template must list markdownlint and any additional required validation
commands in the Testing section.

## Pre-Submission Requirements

Before creating a pull request, all of the following must be met unless the
docs-only exception applies:

1. 100 percent unit test success
2. Coverage must not decline (lines and branches)
3. All hard-gate code quality checks must pass
4. Soft-gate failures must be disclosed and tracked

Each repository must document its canonical local validation command(s).
Markdownlint is required for all repositories and must be part of the
pre-submission run. Additional commands are required when documented.

## Pre-Submission Checklist

Use the repository's canonical validation command(s) when available.

If no single command exists, run:

- markdownlint
- full test suite
- linting
- type checking
- coverage

Do not run only a subset of tests. Local validation should mirror CI hard
gates. Run soft-gate checks when documented.

## Pull request submission

Use the GitHub CLI for PR creation unless a repository documents an alternative.

Required sequence:

1. Ensure the feature branch exists locally and all commits are present.
2. Push the branch to the remote before creating the PR.
3. Create the PR only after the remote branch exists.

Recommended commands:

```bash
git status -sb
git push -u origin <feature-branch>
gh pr create --base <target-branch> --head <feature-branch>
```

Failure mode and fix:

- If PR creation fails because the head or base SHA is blank or the head ref is
  not a branch, the branch is not pushed. Push the branch to the remote and
  retry the PR creation command.

## What to Do When Checks Fail

If any hard-gate check fails:

1. do not create the PR
2. fix the failing tests or checks
3. re-run the full checklist
4. proceed only when everything passes

If a soft-gate check fails, either fix it immediately or document the failure
with rationale and follow-up tracking before submission.

Common mistakes to avoid:

- "I only changed one area, so I only ran those tests"
- "The test failures are pre-existing"
- "I will fix it in a follow-up PR"

## Auto-merge policy

Auto-merge is the default for all pull requests, including docs-only changes.

Opt out when a merge must be scheduled or reviewed by adding the label
`manual-merge` to the pull request. Do not enable auto-merge while that label
is present.

When asked to submit or finalize a PR, enable auto-merge using
`gh pr merge --auto --merge --delete-branch` without prompting for a merge
method unless `manual-merge` is present or auto-merge is disabled for the
repository.

If auto-merge is disabled for the repository, follow the manual merge steps and
wait for all required checks to pass before merging.

Auto-merge is asynchronous. Enabling it is not finalization; you must still
wait for required checks to complete. If any required check fails, fix the
issue immediately and re-run the checks before merging.

Never use `--admin` or other administrative overrides to bypass required
checks. If checks are pending, wait. If checks fail, fix them. There is no
shortcut.

If the user asks to finalize a PR, waiting for auto-merge to complete is
mandatory. Do not ask whether to wait unless the user explicitly requests a
deferral.

## Async finalization guardrail

Async submission requires a follow-up finalize step. To prevent "pending
finalization" work from being forgotten, apply the following guardrail at the
start of each work session or before declaring a development cycle complete:

1. Check for open pull requests targeting `develop`.
2. If any are merged but not finalized, finalize them immediately.
3. If any are open and awaiting checks, decide to wait or defer before starting
   new work.

Do not declare a development cycle complete while open PRs remain against
`develop`.

## Pull Request Finalization

Finalization begins only after all required CI gates have completed
successfully and the PR is ready to merge (manually or via auto-merge). If a
required check fails, resolve it immediately and re-run the checks before
merging.

When `scripts/dev/finalize_repo.sh` is available, run it after the merge
completes to automate steps 3-5 below.

Finalize the PR in this order:

1. wait for all required checks to complete and pass
2. merge the PR and delete the remote branch (or wait for auto-merge to do so)
3. update local copy of the target branch
4. synchronize the local environment with dependency specifications
5. delete the local feature branch and prune stale remotes
6. run final validation (skip for docs-only PRs)

Do not reuse old branch names.
