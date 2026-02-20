# GitHub Issue Standards

## Purpose

Define a consistent, enforced workflow for GitHub issues so all changes are
tracked, reviewable, and auditable.

## Scope

Applies to all repositories that use GitHub issues and pull requests.

## Definitions

- Issue: The unit of tracked work in GitHub.
- Primary issue: The single issue a pull request is intended to close.
- Sub-issue: A scoped unit of work that contributes to a parent issue but does
  not complete it.

## Core rules

- Every pull request must have a primary GitHub issue. No exceptions.
- Work must not begin until the issue exists.
- One primary issue per pull request. If a PR must close multiple issues,
  document why in the PR description.

## Acceptance criteria

Every issue must specify acceptance criteria if they are not intuitively
obvious. If acceptance criteria are ambiguous, get explicit human confirmation
before proceeding.

Examples:

- Docs-only issues: satisfied when documentation changes are merged.
- Bug reports: may require reporter confirmation or verified reproduction and
  resolution steps.

## Issue templates

Repositories must use GitHub Issue Forms and disable blank issues so all issues
capture the required structure.

Minimum required fields:

- Summary
- Problem or goal
- Acceptance criteria
  - include an explicit "criteria are obvious" option
  - require explicit criteria when not obvious
- Validation or evidence

Required configuration:

- `.github/ISSUE_TEMPLATE/issue.yml` (or equivalent form name)
- `.github/ISSUE_TEMPLATE/config.yml` with `blank_issues_enabled: false`

## Issue creation and linking

- If a human already specified an issue, use it as the primary issue.
- If no issue exists, create one before creating a branch or changing files.
- If no issue exists, create it immediately using best-effort assumptions and
  explicitly note those assumptions in the issue body. Do not delay work by
  asking for an issue number unless acceptance criteria are materially
  ambiguous.
- The PR description must link to the primary issue.
- If an issue has no special acceptance criteria, include a closing keyword in
  the PR description so the issue auto-closes on merge.
- If acceptance criteria are specified, use a non-closing reference in the PR
  description and close the issue only when the criteria are satisfied.

## Sub-issues

Create a sub-issue when:

- the parent issue is too large for a single PR
- the PR will not fully resolve the parent issue
- the work can be reviewed and merged independently

Sub-issue rules:

- Link each sub-issue to its parent using the sub-issues API (see below).
- The PR should close the sub-issue, not the parent, unless the PR completes
  the parent’s full scope.

### Linking a sub-issue via the API

Creating a sub-issue relationship is a two-step process:

1. **Get the child issue’s database ID** (this is the numeric ID, not the
   issue number):

   ```bash
   gh api repos/{owner}/{repo}/issues/{child_number} --jq ‘.id’
   ```

2. **Link the child to the parent**:

   ```bash
   gh api repos/{owner}/{repo}/issues/{parent_number}/sub_issues \
     --method POST -F sub_issue_id={database_id}
   ```

Use `-F` (not `-f`) for `sub_issue_id` — the API requires an integer, and
`-f` sends a string.

## Closing behavior

- Default: auto-close issues via PR closing keywords.
- If acceptance criteria are specified, do not auto-close. The agent
  finalizing the PR is responsible for determining closure once the criteria
  are met.
- If auto-closing is disabled or the PR targets a non-default branch, close
  the issue manually after merge only when acceptance criteria are satisfied.
- A closed issue must reflect completed work. If work is deferred, keep the
  issue open or create a follow-up issue and link it explicitly.

## Related documents

- Pull request workflow: [pull-request-workflow.md](pull-request-workflow.md)
- Branching and deployment model: [branching-and-deployment.md](branching/branching-and-deployment.md)
