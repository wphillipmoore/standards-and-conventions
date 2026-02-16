# Documentation Toolchain

## Table of Contents

- [Decision](#decision)
- [Status](#status)
- [Context](#context)
- [Comparison](#comparison)
- [Rationale](#rationale)
- [Required Configuration](#required-configuration)
- [CI Workflow Pattern](#ci-workflow-pattern)
- [Shared Fragment Architecture](#shared-fragment-architecture)

## Decision

All repositories use **MkDocs Material** with **mike** versioning as the
documentation toolchain. This applies to documentation-only repositories,
application repositories, and library repositories across all languages.

## Status

**Adopted** — February 2026.

- standards-and-conventions: MkDocs Material + mike (documentation-only repo)
- mq-rest-admin-java: MkDocs Material + mike (adopted at project inception)
- mq-rest-admin-python: MkDocs Material + mike (migrated from Sphinx+MyST+Furo)
- mq-rest-admin-go: MkDocs Material + mike (adopted at project inception)

## Context

A consistent documentation toolchain across all repositories provides a uniform
reading experience, versioned documentation tied to releases, searchable
published sites, and the ability to share documentation fragments between
repositories that use common content.

The Python ecosystem originally used Sphinx with MyST-Parser and the Furo theme.
Standardizing on MkDocs Material eliminated the toolchain divergence and enabled
documentation fragment sharing via `pymdownx.snippets`.

## Comparison

| Capability | Sphinx + MyST + Furo | MkDocs Material |
| --- | --- | --- |
| Markdown native | Via MyST-Parser | Native |
| Snippet includes | Not built-in | `pymdownx.snippets` |
| API autodoc (Python) | `sphinx.ext.autodoc` | `mkdocstrings[python]` |
| API autodoc (Java) | Not applicable | Javadoc (external) |
| Theme quality | Furo (excellent) | Material (excellent) |
| Dark/light toggle | Built-in | Built-in |
| Search | Built-in | Built-in |
| Code highlighting | Pygments | `pymdownx.highlight` |
| Tabbed content | `sphinx-design` | `pymdownx.tabbed` |
| Admonitions | Built-in | Built-in |
| Build speed | Moderate | Fast |
| Config complexity | `conf.py` + extensions | Single `mkdocs.yml` |
| Versioned docs | `sphinx-multiversion` | mike |

## Rationale

1. **Consistent experience**: Identical theme, navigation structure, and
   feature set across all documentation sites regardless of repository type
   or language.

2. **Versioned documentation**: mike provides versioned documentation tied
   to branches and releases, with a version selector in the published site.

3. **Shared content**: `pymdownx.snippets` enables repositories to include
   narrative fragments from shared repositories without duplication.

4. **Simpler maintenance**: One `mkdocs.yml` per repo versus Sphinx's
   `conf.py` plus multiple extension configurations.

5. **No capability loss**: `mkdocstrings[python]` provides equivalent
   autodoc functionality for Python. Java uses Javadoc separately.
   Every Sphinx feature used has a direct MkDocs Material equivalent.

## Required Configuration

### Repository layout patterns

Two layout patterns exist based on repository type:

| Repository type | mkdocs.yml location | docs_dir | Content path |
| --- | --- | --- | --- |
| Documentation-only | repo root | `docs` | `docs/` |
| Code repositories | `docs/site/mkdocs.yml` | `docs` | `docs/site/docs/` |

Documentation-only repositories (like standards-and-conventions) place
`mkdocs.yml` at the repository root with content in `docs/`. Code repositories
nest the MkDocs configuration under `docs/site/` to keep documentation
separate from source code.

### mike configuration (all repos)

Every repository must include these settings in `mkdocs.yml`:

```yaml
strict: true

extra:
  version:
    provider: mike

plugins:
  - search
```

- `strict: true` causes the build to fail on warnings, catching broken links
  and missing references in CI.
- `extra.version.provider: mike` enables the version selector in the Material
  theme.
- `plugins: [search]` explicitly enables search (required when specifying the
  plugins list).

### Theme

```yaml
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - content.code.copy
    - search.highlight
    - search.suggest
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

### Required extensions

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.snippets
  - tables
  - toc:
      permalink: true
```

Repositories that share documentation fragments via `pymdownx.snippets` add
`base_path` entries to resolve fragment locations in both CI and local contexts.

### Language-specific plugins

**Python repos** add `mkdocstrings` for API autodoc:

```yaml
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
          options:
            show_source: true
            show_inheritance_diagram: false
            show_bases: true
            members_order: source
```

**Java repos** use Javadoc generated separately (no mkdocstrings equivalent).

**Go repos** use standard Go doc tooling (no mkdocstrings equivalent).

## CI Workflow Pattern

All repositories use a GitHub Actions workflow that deploys documentation with
mike. The workflow structure adapts to the repository's branching model.

### Standard workflow structure

```yaml
name: Documentation

on:
  push:
    branches: [develop, main]
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: docs
  cancel-in-progress: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install mkdocs-material mike
      - name: Configure git identity
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
      - name: Determine version
        id: version
        run: |
          # Version determination varies by branching model (see below)
      - name: Deploy with mike
        env:
          VERSION: ${{ steps.version.outputs.version }}
          ALIAS: ${{ steps.version.outputs.alias }}
        run: |
          mike deploy --push --update-aliases \
            "$VERSION" "$ALIAS"
          mike set-default --push latest
```

Key requirements:

- `fetch-depth: 0` is required for mike to access the `gh-pages` branch
  history.
- Git identity must be configured before mike can push.
- `concurrency` prevents parallel deployments from conflicting.

### Version determination by branching model

#### docs-single-branch

Documentation-only repositories use `develop` as the single eternal branch.
Since there is no `main` branch, `develop` represents the canonical state:

```yaml
- name: Determine version
  id: version
  run: |
    echo "version=dev" >> "$GITHUB_OUTPUT"
    echo "alias=latest" >> "$GITHUB_OUTPUT"
```

The workflow triggers only on `develop` pushes. The `dev` version always
receives the `latest` alias since it is the only published version.

#### application-promotion and library-release

Repositories with both `develop` and `main` branches determine the version
from the branch:

```yaml
- name: Determine version
  id: version
  run: |
    if [ "${{ github.ref_name }}" = "main" ]; then
      VERSION=$(cat VERSION)
      echo "version=${VERSION}" >> "$GITHUB_OUTPUT"
      echo "alias=latest" >> "$GITHUB_OUTPUT"
    else
      echo "version=dev" >> "$GITHUB_OUTPUT"
      echo "alias=" >> "$GITHUB_OUTPUT"
    fi
```

- `main` branch: version from `VERSION` file, aliased as `latest`.
- `develop` branch: version `dev`, no alias.

The workflow triggers on both `develop` and `main` pushes.

## Shared Fragment Architecture

Repositories that share documentation content use `pymdownx.snippets` to
include fragments from a common repository. Fragments are pure Markdown with
no toolchain-specific syntax, ensuring they work in any repository's
documentation build.

Shared fragment inclusion:

```markdown
--8<-- "shared-architecture-intro.md"
```

The `pymdownx.snippets` base paths resolve in two contexts:

- **CI**: Common repository checked out at a known path in the workspace.
- **Local**: Common repository as a sibling directory.

Repositories that do not share fragments omit the `base_path` configuration
from `pymdownx.snippets`.
