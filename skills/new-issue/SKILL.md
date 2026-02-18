---
name: new-issue
description: Create a well-structured GitHub issue by collecting required attributes through guided questions.
---

# New issue

## Table of Contents

- [Overview](#overview)
- [Workflow](#workflow)
  - [Select project](#select-project)
  - [Select target repository](#select-target-repository)
  - [Collect issue type](#collect-issue-type)
  - [Collect priority](#collect-priority)
  - [Collect work type](#collect-work-type)
  - [Collect summary](#collect-summary)
  - [Collect problem or goal](#collect-problem-or-goal)
  - [Collect acceptance criteria](#collect-acceptance-criteria)
  - [Collect validation](#collect-validation)
  - [Confirm and create](#confirm-and-create)
  - [Report](#report)
- [Resources](#resources)

## Overview

Create a single GitHub issue by walking the human through a series of
questions that collect all fields required by the GitHub issue standards.
The skill enforces the minimum required structure (Summary, Problem/Goal,
Acceptance Criteria, Validation) and assigns the issue to a GitHub Project.

### Interaction modes

Each collection step uses one of two interaction modes:

- **Selection** — Use `AskUserQuestion` when the user picks from a fixed
  set of options (project, repository, issue type, priority, work type).
- **Free-text** — Ask via a plain conversational message and wait for the
  user's reply. Do NOT use `AskUserQuestion` for open-ended input such as
  the issue title, problem description, or acceptance criteria details.
  Simply prompt the user in your message and let them respond naturally.

## Workflow

### Select project

> Interaction mode: **selection**

List available GitHub Projects with `gh project list` and ask the user to
select one. Default to the project associated with the current repository
(determined from the working directory). If only one project exists, select
it automatically and confirm.

### Select target repository

> Interaction mode: **selection**

List the repositories linked to the selected project and ask the user which
repository the issue should be created in. Default to the current repository
(determined from the working directory) if it belongs to the project.

Resolve the local path for `gh` commands. If the repository is not
available locally, stop and inform the user.

### Collect issue type

> Interaction mode: **selection**

Ask the user for the issue type:

| Type         | GitHub label  | Title prefix |
| ------------ | ------------- | ------------ |
| Enhancement  | enhancement   | feat:        |
| Bug          | bug           | fix:         |
| Research     | research      | research:    |
| Chore        | chore         | chore:       |
| Docs         | documentation | docs:        |

If the selected label does not exist in the target repository, create it
with `gh label create`.

### Collect priority

> Interaction mode: **selection**

Ask the user for the priority:

| Priority | Meaning                        |
| -------- | ------------------------------ |
| P0       | Now — immediate work           |
| P1       | Next — next up after current   |
| P2       | Later — backlog                |

This is set as a project field after the issue is added to the project.

### Collect work type

> Interaction mode: **selection**

Ask the user for the work type:

| Work Type         | When to use                                  |
| ----------------- | -------------------------------------------- |
| feature           | New functionality                            |
| bugfix            | Fixing broken behavior                       |
| docs              | Documentation-only changes                   |
| research          | Investigation or spike                       |
| sync              | Cross-repo propagation                       |
| dependency-update | Dependency version bump                      |

This is set as a project field after the issue is added to the project.

### Collect summary

> Interaction mode: **free-text**

Ask the user for a short title describing the issue. Prefix the title
with the conventional type from the table above.

Example: `feat: add retry configuration to REST client`

### Collect problem or goal

> Interaction mode: **free-text**

Ask the user to describe the problem being solved or the goal being
achieved. This becomes the **Problem / Goal** section of the issue body.

### Collect acceptance criteria

> Interaction mode: **selection** for the initial question, then
> **free-text** if the user needs to provide explicit criteria.

Ask whether acceptance criteria are obvious from the summary.

- If obvious: record "Acceptance criteria are implicit from the summary."
- If not obvious: collect explicit criteria as a checklist (one item per
  line, each prefixed with `- [ ]`).

### Collect validation

> Interaction mode: **selection** (multi-select)

Ask how completion will be verified. Present the common options as a
multi-select list:

- CI passes
- Tests added
- Documentation updated
- Manual verification

The user may also provide a custom response via the "Other" option.
Record the response as the **Validation** section of the issue body.

### Confirm and create

Assemble the issue and present it to the user for review:

```
Project: <project-name>
Repository: <owner>/<repo>
Title: <type-prefix> <summary>
Labels: <label>
Priority: <P0|P1|P2>
Work Type: <work-type>

## Problem / Goal

<problem-or-goal text>

## Acceptance Criteria

<criteria or "Acceptance criteria are implicit from the summary.">

## Validation

<validation text>
```

After user approval, create the issue:

```bash
gh issue create --repo <owner>/<repo> --title "<title>" --label "<label>" --body-file <tempfile>
```

Then add the issue to the selected project and set project fields:

```bash
gh project item-add <project-number> --owner <owner> --url <issue-url>
gh project item-edit --project-id <project-id> --id <item-id> --field-id <priority-field-id> --single-select-option-id <option-id>
gh project item-edit --project-id <project-id> --id <item-id> --field-id <work-type-field-id> --single-select-option-id <option-id>
```

### Report

Display the issue URL and project assignment confirmation.

## Resources

- `docs/code-management/github-issues.md`
- `docs/code-management/github-projects.md`
- `docs/code-management/commit-messages-and-authorship.md`
