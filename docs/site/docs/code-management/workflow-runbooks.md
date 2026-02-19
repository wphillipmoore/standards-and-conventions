# Workflow runbooks

## Purpose

Provide deterministic, step-by-step workflows that remove ambiguity in common
operations.

## Scope

Applies to all repositories governed by these standards.

## Session startup runbook

1. Run the standards bootstrap protocol.
2. Record the standards snapshot before any action.
3. Check for open pull requests targeting the primary integration branch. If
   any are merged but not finalized, finalize them before starting new work.
4. If a prompt starts with `RTFM`, invoke the `rtfm` skill and suspend normal
   work.

## Issue creation runbook

1. Confirm whether a primary issue already exists for the work.
2. If no issue exists, create one immediately using best-effort assumptions.
3. If acceptance criteria are ambiguous, pause and ask for explicit criteria.
4. Record validation or evidence expectations in the issue body.

## Branching runbook

1. Check the current branch.
2. If on an eternal branch, create a short-lived branch using an approved
   prefix.
3. If already on a short-lived branch, continue.
4. Re-check the branch before any edit or commit.

## Change execution runbook

1. Read any additional standards required for the task before editing.
2. Make the smallest set of focused changes needed to satisfy the issue.
3. Keep documentation generic and update tables of contents when headings
   change.
4. If a required standard conflicts with a local override, stop and ask.

## Validation runbook

1. Identify the canonical local validation command from repository standards.
2. If a command is documented, run it.
3. If no command is documented, ask the user for the required validation.
4. If any hard-gate check fails, fix it before proceeding.

## Pull request submission runbook

1. Ensure the branch contains all intended commits.
2. Push the branch to the remote.
3. Create the pull request using the repository template.
4. Link the primary issue in the PR description.
5. If the work is docs-only, state "Docs-only: tests skipped" and list changed
   files.
6. Enable auto-merge unless the repository requires manual merge.

## Pull request finalization runbook

1. Wait for all required checks to complete and pass.
2. If auto-merge is enabled, wait for the merge to complete before cleanup.
3. Merge the pull request (if not already merged) and delete the remote branch.
4. Run `scripts/dev/finalize_repo.sh` to update the local target branch, delete
   merged branches, and prune remotes. If the script is not available, perform
   steps 5-6 manually.
5. Delete the local feature branch and prune remotes.
6. Run final validation unless the docs-only exception applies.

## Docs-only exception runbook

1. Determine whether the diff qualifies as docs-only per repository standards.
2. If docs-only, run markdownlint and skip other test or validation suites.
3. If not docs-only, run the full required validation set.

## Maintenance

Update these runbooks when workflow rules or validation requirements change.
