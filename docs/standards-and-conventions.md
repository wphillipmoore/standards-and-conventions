# Standards and Conventions Reference

## Table of Contents
- [Purpose](#purpose)
- [Requirement](#requirement)
- [Canonical references](#canonical-references)
- [Project-specific overlay](#project-specific-overlay)
- [Template](#template)
- [Maintenance](#maintenance)

## Purpose
Provide a required, repository-local entry point that references the canonical
standards and documents project-specific details that do not belong upstream.

## Requirement
Every repository must include `docs/standards-and-conventions.md`.

This file must:
- reference the canonical standards in this repository using GitHub URLs
- document project-specific information and deviations
- avoid duplicating canonical standards verbatim

If the canonical standards cannot be retrieved, treat it as a fatal exception
and notify the user.

## Canonical references
Include links to the canonical documents that apply to the repository. Use
GitHub URLs pointing to this repository.

## Project-specific overlay
Record project-specific details here, such as:
- approved AI co-author identities for commit trailers
- local terminology or naming conventions
- approved deviations from canonical standards

Project-specific content must be explicit and scoped. Do not restate canonical
rules unless a deviation exists.

## Template
```
# <Repository> Standards and Conventions

This repository follows the canonical standards at:
https://github.com/<org>/<standards-repo>

## Table of Contents
- [Canonical references](#canonical-references)
- [Project-specific overlay](#project-specific-overlay)

## Canonical references
- <link to relevant canonical docs>

## Project-specific overlay
- AI co-authors:
  - Co-Authored-By: ai-tool <id+ai-tool@users.noreply.github.com>
- Local deviations:
  - <explicit deviation, if any>
```

## Maintenance
Keep this file short and current. Update it whenever a project-specific rule
changes or a deviation is introduced or removed.
