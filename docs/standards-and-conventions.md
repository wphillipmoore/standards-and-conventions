# Standards and Conventions Reference

## Table of Contents
- [Purpose](#purpose)
- [Requirement](#requirement)
- [Canonical references](#canonical-references)
  - [Core references (always required)](#core-references-always-required)
  - [Repository-type references (required for the declared type)](#repository-type-references-required-for-the-declared-type)
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
- list all required canonical references for the repository
- document project-specific information and deviations
- include a complete repository profile with concrete values
- avoid duplicating canonical standards verbatim

If the canonical standards cannot be retrieved, treat it as a fatal exception
and notify the user.

Repository profiles must explicitly declare `repository_type` and must not
contain placeholder values (for example, `<application|library|documentation>`).
If any required attribute is missing or left as a placeholder, treat it as a
fatal exception and stop.

## Canonical references
Include links to the canonical documents that apply to the repository. Use
GitHub URLs pointing to this repository. The lists below are required for this
repository and serve as the minimum baseline for other repositories.
Include only the repository-type references that match the declared
`repository_type`.

### Core references (always required)
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/foundation/markdown-standards.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/repository-types-and-attributes.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/commit-messages-and-authorship.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/github-issues.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/pull-request-workflow.md
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/source-control-guidelines.md

### Repository-type references (required for the declared type)
- https://github.com/wphillipmoore/standards-and-conventions/blob/develop/docs/code-management/documentation-branching-model.md

## Project-specific overlay
Record project-specific details here, such as:
- approved AI co-author identities for commit trailers
- local terminology or naming conventions
- approved deviations from canonical standards
- repository type and attributes

Project-specific content must be explicit and scoped. Do not restate canonical
rules unless a deviation exists.

- AI co-authors:
  - Co-Authored-By: wphillipmoore-codex <255923655+wphillipmoore-codex@users.noreply.github.com>
  - Co-Authored-By: wphillipmoore-claude <255925739+wphillipmoore-claude@users.noreply.github.com>
- Repository profile:
  - repository_type: documentation
  - versioning_scheme: none
  - branching_model: docs-single-branch
  - release_model: none
  - supported_release_lines: none

## Template
```
# <Repository> Standards and Conventions

This repository follows the canonical standards at:
https://github.com/<org>/<standards-repo>

## Table of Contents
- [Canonical references](#canonical-references)
- [Project-specific overlay](#project-specific-overlay)

## Canonical references
Include only the repository-type references that match the declared
`repository_type`.

### Core references (always required)
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/foundation/markdown-standards.md
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/repository-types-and-attributes.md
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/commit-messages-and-authorship.md
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/github-issues.md
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/pull-request-workflow.md
- https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/source-control-guidelines.md

### Repository-type references (required for the declared type)
- Documentation repositories: https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/documentation-branching-model.md
- Application repositories: https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/branching-and-deployment.md
- Application repositories: https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/application-versioning-scheme.md
- Library repositories: https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/library-branching-and-release.md
- Library repositories: https://github.com/<org>/<standards-repo>/blob/<default-branch>/docs/code-management/library-versioning-scheme.md

## Project-specific overlay
- AI co-authors:
  - Co-Authored-By: ai-tool <id+ai-tool@users.noreply.github.com>
- Repository profile:
  - repository_type: <application|library|documentation>
  - versioning_scheme: <application|library|ecosystem-specific|none>
  - branching_model: <application-promotion|library-release|docs-single-branch>
  - release_model: <environment-promotion|artifact-publishing|none>
  - supported_release_lines: <single|list of MAJOR.MINOR lines|none>
- Local deviations:
  - <explicit deviation, if any>
```

## Maintenance
Keep this file short and current. Update it whenever a project-specific rule
changes or a deviation is introduced or removed.
