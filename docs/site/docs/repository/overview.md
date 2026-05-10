# Repository Standards Overview

## Purpose

Define reusable repository structure standards that keep projects durable,
discoverable, and easy to operate without original authorship.

## Scope

These standards apply to repository layout, documentation structure, dependency
management, and shared tooling. They do not define language-specific coding
practices.

## Document Map

- Repository structure: [repository-structure.md](repository-structure.md)

## Dependency Anchor Records

Provide a durable record of why a dependency is anchored below the latest
acceptable range, including the evidence from each failed upgrade attempt.
These records apply to any dependency that is pinned or constrained because
newer releases fail validation or break compatibility.

### Required layout

- Create one file per anchored dependency under `docs/dependencies/`.
- Use the dependency name for the filename (`<dependency-name>.md`) and keep
  it stable across updates.
- Each record must use the Markdown standards, including a Table of Contents.

### Record format

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

### Maintenance

- Append new failure entries for each re-test; do not overwrite prior evidence.
- Keep the record aligned with the current constraint and latest attempted
  version.
