# Repository Types and Attributes

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Core concepts](#core-concepts)
- [Repository types](#repository-types)
  - [Application repositories](#application-repositories)
  - [Library repositories](#library-repositories)
  - [Documentation repositories](#documentation-repositories)
- [Required repository attributes](#required-repository-attributes)
- [Declaration requirement](#declaration-requirement)
- [Change control](#change-control)
- [Related documents](#related-documents)

## Purpose
Define the repository classifications and metadata needed to select the correct
branching, release, and versioning standards.

## Scope
Applies to every repository using these standards.

## Core concepts
- A repository type selects the default workflow rules.
- Repository attributes document deviations or additional constraints.
- When a repository does not fit an existing type, define a new type before
  inventing ad hoc rules.

## Repository types

### Application repositories
An application repository:
- deploys infrastructure-backed services or APIs
- promotes linearly across environments
- runs one active version per environment

Use:
- Branching and deployment model: [branching-and-deployment.md](branching-and-deployment.md)
- Application versioning scheme: [application-versioning-scheme.md](application-versioning-scheme.md)

### Library repositories
A library repository:
- produces reusable artifacts published to a package registry or consumed via
  tagged distribution (for example, GitHub Actions)
- has no environment-bound infrastructure
- may support multiple concurrent release lines

Use:
- Library branching and release model: [library-branching-and-release.md](library-branching-and-release.md)
- Library versioning scheme: [library-versioning-scheme.md](library-versioning-scheme.md)

### Documentation repositories
A documentation repository:
- contains documentation, templates, or example snippets only
- has no deployable application or package artifact
- does not require formal releases or versioning

Use:
- Documentation branching model: [documentation-branching-model.md](documentation-branching-model.md)

## Required repository attributes
Each repository must declare, at minimum:
- `repository_type`: `application`, `library`, or `documentation`
- `versioning_scheme`: `application`, `library`, `ecosystem-specific`, or `none`
- `branching_model`: `application-promotion`, `library-release`, or `docs-single-branch`
- `release_model`: `environment-promotion`, `artifact-publishing`, or `none`
- `supported_release_lines`: a single active line for applications; one or more
  `MAJOR.MINOR` lines for libraries; `none` for documentation

## Declaration requirement
Record repository type and attributes in the repository's
`docs/standards-and-conventions.md` under the project-specific overlay.

## Change control
Changing a repository type or its declared attributes is a governance change.
Treat it as a deliberate migration with explicit review and updated standards
references.

## Related documents
- Branching and deployment model: [branching-and-deployment.md](branching-and-deployment.md)
- Library branching and release model: [library-branching-and-release.md](library-branching-and-release.md)
- Documentation branching model: [documentation-branching-model.md](documentation-branching-model.md)
- Release and versioning policy: [release-versioning.md](release-versioning.md)
- Application versioning scheme: [application-versioning-scheme.md](application-versioning-scheme.md)
- Library versioning scheme: [library-versioning-scheme.md](library-versioning-scheme.md)
