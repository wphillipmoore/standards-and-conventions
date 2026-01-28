# Standards and Conventions Reference

## Table of Contents

- [Purpose](#purpose)
- [Requirement](#requirement)
- [Includes](#includes)
- [Project-specific overlay](#project-specific-overlay)
- [Template](#template)
- [Maintenance](#maintenance)

## Purpose

Provide a required, repository-local entry point that references the canonical
standards and documents project-specific details that do not belong upstream.

## Requirement

Every repository must include `docs/standards-and-conventions.md`.

This file must:

- reference the canonical standards in this repository using GitHub URLs or
  by including the canonical standards entry point with `#include`
- make the required canonical references discoverable via a direct list or an
  include chain
- document project-specific information and deviations inline or via
  `docs/repository-standards.md` (included from `AGENTS.md`)
- include a complete repository profile with concrete values
- avoid duplicating canonical standards verbatim

If the canonical standards cannot be retrieved, treat it as a fatal exception
and notify the user.

Repository profiles must explicitly declare `repository_type` and must not
contain placeholder values (for example, `<application|library|documentation>`).
If any required attribute is missing or left as a placeholder, treat it as a
fatal exception and stop.

## Includes

This list is the authoritative include chain for the shared standards corpus.

#include docs/foundation/overview.md
#include docs/foundation/markdown-standards.md
#include docs/foundation/architecture-standards.md
#include docs/foundation/interaction-contract.md
#include docs/foundation/interaction-contract-brief.md
#include docs/foundation/ai-assisted-development-loop.md
#include docs/foundation/ai-code-review-guidelines.md
#include docs/foundation/agent-skills.md
#include docs/foundation/agent-boot-banner.md
#include docs/foundation/agent-pre-response-checklist.md
#include docs/foundation/cognitive-drift-log.md
#include docs/foundation/cognitive-regression-tests.md
#include docs/foundation/summarize-decisions-protocol.md
#include docs/foundation/summarize-operations-protocol.md
#include docs/foundation/summarize-stream-of-consciousness-protocol.md

#include docs/code-management/overview.md
#include docs/code-management/repository-types-and-attributes.md
#include docs/code-management/commit-messages-and-authorship.md
#include docs/code-management/github-issues.md
#include docs/code-management/pull-request-workflow.md
#include docs/code-management/source-control-guidelines.md
#include docs/code-management/documentation-branching-model.md
#include docs/code-management/branching-and-deployment.md
#include docs/code-management/application-versioning-scheme.md
#include docs/code-management/library-branching-and-release.md
#include docs/code-management/library-versioning-scheme.md
#include docs/code-management/release-versioning.md
#include docs/code-management/hotfix-policy.md
#include docs/code-management/shared-actions-library.md

#include docs/repository/overview.md
#include docs/repository/repository-structure.md

#include docs/dependencies/overview.md
#include docs/dependencies/dependency-update-workflow.md

#include docs/development/overview.md
#include docs/development/environment-and-tooling.md
#include docs/development/deprecation-warnings.md
#include docs/development/database/overview.md
#include docs/development/database/conventions.md
#include docs/development/python/overview.md
#include docs/development/python/naming-conventions.md
#include docs/development/python/type-hints.md
#include docs/development/python/import-time-side-effects.md
#include docs/development/python/testing-and-coverage.md
#include docs/development/python/dependency-management.md
#include docs/development/python/version-management.md
#include docs/development/python/local-validation-scripts.md
#include docs/development/python/ty-migration-plan.md

## Project-specific overlay

Record project-specific details here, such as:

- approved AI co-author identities for commit trailers
- local terminology or naming conventions
- approved deviations from canonical standards
- repository type and attributes

Project-specific content must be explicit and scoped. Do not restate canonical
rules unless a deviation exists.

Project-specific content must live in `docs/repository-standards.md` and be
included from `AGENTS.md` only. Do not include it here.

## Template

```text
# <Repository> Standards Bootstrap

  #include docs/standards-and-conventions.md
```

```text
# <Repository> Standards and Conventions

## Table of Contents
- [Canonical references](#canonical-references)
- [Project-specific overlay](#project-specific-overlay)

## Canonical references
  #include ../standards-and-conventions/docs/standards-and-conventions.md

## Project-specific overlay
  See `docs/repository-standards.md` (included from `AGENTS.md`).
```

```text
# <Repository> Repository Standards

## Table of Contents
- [AI co-authors](#ai-co-authors)
- [Repository profile](#repository-profile)
- [Local deviations](#local-deviations)

## AI co-authors
- Co-Authored-By: ai-tool <id+ai-tool@users.noreply.github.com>

## Repository profile
- repository_type: <application|library|documentation>
- versioning_scheme: <application|library|ecosystem-specific|none>
- branching_model: <application-promotion|library-release|docs-single-branch>
- release_model: <environment-promotion|artifact-publishing|none>
- supported_release_lines: <single|list of MAJOR.MINOR lines|none>

## Local deviations
- <explicit deviation, if any>
```

## Maintenance

Keep this file short and current. Update it whenever a project-specific rule
changes or a deviation is introduced or removed.
