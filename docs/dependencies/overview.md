# Dependency Anchor Records

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Required layout](#required-layout)
- [Record format](#record-format)
- [Maintenance](#maintenance)
- [Related documents](#related-documents)

## Purpose

Provide a durable record of why a dependency is anchored below the latest
acceptable range, including the evidence from each failed upgrade attempt.

## Scope

These records apply to any dependency that is pinned or constrained because
newer releases fail validation or break compatibility.

## Required layout

- Create one file per anchored dependency under `docs/dependencies/`.
- Use the dependency name for the filename (`<dependency-name>.md`) and keep
  it stable across updates.
- Each record must use the Markdown standards, including a Table of Contents.

## Record format

Each dependency record must include, at minimum:

- Summary of why the dependency is anchored.
- Current constraint and the version range in effect.
- Failure history with evidence for each failed upgrade attempt.
- Exit criteria for removing the anchor.

Suggested template:

```text
# <Dependency name>

## Table of Contents
- [Summary](#summary)
- [Current constraint](#current-constraint)
- [Failure history](#failure-history)
- [Exit criteria](#exit-criteria)

## Summary
Explain the reason for the anchor and the impact.

## Current constraint
State the constraint and when it was last verified.

## Failure history
- YYYY-MM-DD: attempted <version>; test command; error excerpt; conclusion.
- YYYY-MM-DD: attempted <version>; test command; error excerpt; conclusion.

## Exit criteria
Define what will allow the anchor to be removed.
```

## Maintenance

- Append new failure entries for each re-test; do not overwrite prior evidence.
- Keep the record aligned with the current constraint and latest attempted
  version.

## Related documents

- Dependency update workflow: [dependency-update-workflow.md](dependency-update-workflow.md)
