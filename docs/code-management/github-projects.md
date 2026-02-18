# GitHub Projects

## Purpose

Define how GitHub Projects is used to plan, prioritize, and track work across
repository collections.

## Scope

Applies to all repositories managed through GitHub Projects. GitHub Projects
provides the planning layer; the execution layer (branching, PRs, CI) is
unchanged.

## Definitions

- Project: A GitHub Projects (V2) board that aggregates issues and pull
  requests across one or more repositories.
- Collection: A logical grouping of repositories that share a common domain
  or purpose.
- View: A saved perspective on project data with specific layout, filters,
  grouping, and visible fields.

## Project structure

### One project per collection

Create one GitHub Project per repository collection, not one monolithic
project. Each collection has different workflow cadence, and context-switching
happens by collection, not by status.

| Collection    | Repositories                | Project       |
| ------------- | --------------------------- | ------------- |
| mq-rest-admin | go, python, java, rust,     | mq-rest-admin |
|               | ruby, common                |               |
| standards     | standards-and-conventions,  | standards     |
|               | standard-tooling,           |               |
|               | standard-actions            |               |
| mnemosys      | core, operations, ios       | mnemosys      |
| sandbox       | standalone and experimental | sandbox       |

### Project setup

1. Create a user-level project (not repo-level).
2. Use the **Team Planning** template.
3. Link all repositories in the collection to the project via Settings >
   Manage access.
4. Add custom fields (see below).
5. Configure workflows (see below).
6. Create views (see below).

## Custom fields

The Team Planning template provides built-in fields including Status
(Todo/In progress/Done), Priority (P0/P1/P2), Size, Estimate, Iteration,
Start date, and Target date.

Add these additional fields to each project:

| Field          | Type          | Options              |
| -------------- | ------------- | -------------------- |
| Collection     | Single select | mq-rest-admin,       |
|                |               | standards, mnemosys, |
|                |               | sandbox              |
| Work Type      | Single select | feature, bugfix,     |
|                |               | sync,                |
|                |               | dependency-update,   |
|                |               | docs, research       |
| Agent Eligible | Single select | yes, no              |
| Sync Status    | Single select | not-applicable,      |
|                |               | pending-sync, synced |

### Field usage guidelines

- **Priority**: Use P0 for immediate work, P1 for next up, P2 for
  backlog.
- **Work Type**: Set when creating or triaging an issue. Use `sync` for
  cross-repo propagation work.
- **Agent Eligible**: Set to `yes` when the issue has clear acceptance
  criteria and can be completed without human judgment calls.
- **Sync Status**: Only relevant for work that propagates across
  repositories (common in mq-rest-admin). Default to `not-applicable`
  for standalone work.

## Views

Each project should have these four views:

### Backlog (Table)

The default triage view. Shows all items grouped by Priority. Use this to
review and prioritize work before starting a session.

- **Layout**: Table
- **Group by**: Priority
- **Filter**: None (show everything)
- **Columns**: Title, Repository, Status, Priority, Work Type,
  Agent Eligible, Sync Status

### Active Work (Board)

A kanban-style board for items currently being worked. Use this during
active development sessions.

- **Layout**: Board
- **Column field**: Status
- **Filter**: Exclude Done items

### Sync Tracker (Table)

Tracks cross-repo propagation. Essential for collections like
mq-rest-admin where a change in one language implementation must be
replicated across others.

- **Layout**: Table
- **Group by**: Sync Status
- **Filter**: Work Type = sync
- **Columns**: Title, Repository, Status, Sync Status, Priority

### Agent Queue (Table)

Items that can be delegated to AI agents for autonomous execution.

- **Layout**: Table
- **Sort by**: Priority (ascending, P0 first)
- **Filter**: Agent Eligible = yes
- **Columns**: Title, Repository, Status, Priority, Work Type,
  Sync Status

## Workflows and automations

Configure these workflows in the project settings
(Settings > Workflows):

| Workflow            | Action                    |
| ------------------- | ------------------------- |
| Auto-add to project | Add issues from one       |
|                     | linked repo (free plan    |
|                     | limit: one per project)   |
| Auto-add sub-issues | Add sub-issues when       |
|                     | parent is in project      |
| Item closed         | Set Status to Done        |
| Pull request merged | Set Status to Done        |
| Auto-archive items  | Archive closed items      |
|                     | after 2 weeks             |
| Item reopened       | Set Status to Todo        |

The auto-archive filter is:
`is:issue is:closed updated:<@today-2w`

### Auto-add limitation

On the free GitHub plan, only one auto-add workflow is allowed per
project. Issues from other linked repos must be added to the project
manually (one click from the issue sidebar). If this becomes burdensome,
a GitHub Actions workflow can automate it.

## Integration with development workflow

GitHub Projects is the planning layer. The execution workflow is
unchanged:

```text
Planning (human)              Execution (human + AI)
────────────────              ──────────────────────
GitHub Project                feature/* branch
  → Issue created               → Agent or human works
  → Priority set                → PR created and linked
  → Agent Eligible flagged      → PR reviewed and merged
  → Sync Status tracked         → Issue auto-closes
                                → Dependency updates
```

### What changes

- Before starting work, check the project Backlog view for the next
  priority item.
- Issues are created in the specific repository, then the project
  aggregates them.
- Cross-repo work uses a parent issue with sub-issues per repo.

### What does not change

- CLAUDE.md and AGENTS.md remain the execution-time guidance for AI
  agents.
- Branch and PR workflows are unchanged.
- Skills (/publish, /dependency-update, /pr-workflow) work the same.
- Local validation still runs via scripts/lint.

### Cross-repo work pattern

For work that must propagate across repositories, use sub-issues:

```text
Parent: "Upgrade shared-tooling to v1.1.0"
  ├── Sub: "Sync to mq-rest-admin-go"
  ├── Sub: "Sync to mq-rest-admin-python"
  ├── Sub: "Sync to mq-rest-admin-java"
  ├── Sub: "Sync to mq-rest-admin-rust"
  ├── Sub: "Sync to mq-rest-admin-ruby"
  └── Sub: "Sync to mq-rest-admin-common"
```

Sub-issues can live in different repos than the parent. The project
aggregates them into a single view with progress tracking.

## User guide

### Creating an issue and tracking it

1. **Create the issue** in the appropriate repository. Use the
   repository's issue template.

2. **Add it to the project**. From the issue sidebar, click "Projects"
   and select the collection project. If the repo has auto-add enabled,
   this happens automatically.

3. **Set fields**. In the project view or from the issue sidebar, set:
   - Priority (P0, P1, or P2)
   - Work Type (feature, bugfix, sync, etc.)
   - Agent Eligible (yes or no)
   - Sync Status (if applicable)

4. **Work the issue**. Create a feature branch, make changes, open a PR
   linked to the issue. The project's Active Work board reflects the
   status.

5. **Close the issue**. When the PR merges, the issue auto-closes and
   the project status moves to Done. After 2 weeks, the item is
   auto-archived.

### Example: fixing a bug in mq-rest-admin-python

#### Step 1: Create the issue

In the `mq-rest-admin-python` repository, create an issue:

> **Title**: Fix connection timeout not respecting retry configuration
>
> **Problem**: When the retry count is set to 3, the client only retries
> once before raising a timeout error.
>
> **Acceptance criteria**: Client retries the configured number of times
> before raising an error. Unit test covers the retry behavior.

#### Step 2: Add to project

If auto-add is configured for this repo, the issue appears in the
project automatically. Otherwise, open the issue, click "Projects" in
the sidebar, and select `mq-rest-admin`.

#### Step 3: Set fields

| Field          | Value          |
| -------------- | -------------- |
| Priority       | P1             |
| Work Type      | bugfix         |
| Agent Eligible | yes            |
| Sync Status    | not-applicable |

The issue now appears in the Backlog view under P1 and in the Agent
Queue view.

#### Step 4: Work the issue

```bash
git checkout -b bugfix/fix-retry-timeout
# ... make changes, run tests ...
git add -A && git commit -m "fix: respect retry count"
git push -u origin bugfix/fix-retry-timeout
```

Create a PR linked to the issue. The project's Active Work board shows
the item as In Progress.

#### Step 5: Merge and close

After review, merge the PR. The issue auto-closes, the project status
moves to Done, and after 2 weeks the item is archived.

### Example: cross-repo sync

#### Step 1: Create the parent issue

In `standards-and-conventions`, create an issue:

> **Title**: Upgrade shared-tooling to v1.1.0
>
> **Acceptance criteria**: All mq-rest-admin repos updated and CI
> passing.

#### Step 2: Create sub-issues

Create a sub-issue in each mq-rest-admin repo:

> **Title**: Sync shared-tooling v1.1.0
>
> **Acceptance criteria**: shared-tooling updated, CI passing.

Link each as a sub-issue of the parent.

#### Step 3: Set fields on all issues

| Field       | Value        |
| ----------- | ------------ |
| Work Type   | sync         |
| Sync Status | pending-sync |

#### Step 4: Work each sub-issue

Work each repo independently. As each sub-issue's PR is merged:

- The sub-issue closes automatically.
- Update Sync Status to `synced` on the completed item.
- The parent issue's sub-issue progress bar updates.

#### Step 5: Close the parent

When all sub-issues are complete, close the parent issue.

## Known limitations

- **Auto-add workflow limit**: Free plan allows one auto-add workflow
  per project. Issues from other repos must be added manually.
- **View management**: Views cannot be created, deleted, or configured
  via the GitHub CLI or GraphQL API. All view configuration is UI-only.
- **Issue types**: Organization-level issue types (Bug, Feature, Task)
  are not available on personal accounts. The Work Type custom field
  serves as a workaround.
- **No checkbox field type**: GitHub Projects does not have a native
  checkbox field. Agent Eligible uses a single select (yes/no) instead.

## Related documents

- GitHub issue standards:
  [github-issues.md](github-issues.md)
- Pull request workflow:
  [pull-request-workflow.md](pull-request-workflow.md)
- Branching and deployment model:
  [branching-and-deployment.md](branching-and-deployment.md)
