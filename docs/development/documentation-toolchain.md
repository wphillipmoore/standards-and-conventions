# Documentation Toolchain

## Table of Contents

- [Decision](#decision)
- [Status](#status)
- [Context](#context)
- [Comparison](#comparison)
- [Rationale](#rationale)
- [Required Configuration](#required-configuration)
- [Shared Fragment Architecture](#shared-fragment-architecture)

## Decision

All library repositories in the mq-rest-admin family use **MkDocs Material** as
the documentation toolchain. This applies to every language port (Python, Java,
Go, and any future additions).

## Status

**Adopted** — February 2026.

- mq-rest-admin-java: MkDocs Material (adopted at project inception)
- mq-rest-admin-python: MkDocs Material (migrated from Sphinx+MyST+Furo)
- mq-rest-admin-go: MkDocs Material (adopted at project inception)

## Context

The mq-rest-admin library family spans multiple languages. Each repo contains
substantial narrative documentation (architecture, mapping pipeline, ensure/sync
methods, design rationale) that is largely identical across repos. Sharing this
content requires a common documentation toolchain with a snippet inclusion
mechanism.

The Python repo originally used Sphinx with MyST-Parser and the Furo theme.
The Java repo adopted MkDocs Material from inception. This divergence prevented
sharing documentation fragments via the `mq-rest-admin-common` repository.

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
| Cross-repo sharing | Manual duplication | `pymdownx.snippets` base paths |

## Rationale

1. **Shared content**: `pymdownx.snippets` enables all repos to include
   narrative fragments from `mq-rest-admin-common/fragments/` without
   duplication. This is the primary driver.

2. **Consistent experience**: Identical theme, navigation structure, and
   feature set across all library documentation sites.

3. **Simpler maintenance**: One `mkdocs.yml` per repo versus Sphinx's
   `conf.py` plus multiple extension configurations.

4. **No capability loss**: `mkdocstrings[python]` provides equivalent
   autodoc functionality for Python. Java uses Javadoc separately.
   Every Sphinx feature used by the Python docs has a direct MkDocs
   Material equivalent.

## Required Configuration

### mkdocs.yml structure

All repos use `docs/site/mkdocs.yml` with `docs_dir: docs` (content lives
in `docs/site/docs/`).

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
  - pymdownx.snippets:
      base_path:
        - docs
        - ../../.mq-rest-admin-common/fragments
        - ../../../mq-rest-admin-common/fragments
  - tables
  - toc:
      permalink: true
```

The `pymdownx.snippets` base paths resolve in two contexts:

- **CI**: `../../.mq-rest-admin-common/fragments` (common repo checked out
  at `.mq-rest-admin-common` in the workspace root)
- **Local**: `../../../mq-rest-admin-common/fragments` (sibling directory
  at `~/dev/github/mq-rest-admin-common`)

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

### CI workflow

All repos check out `mq-rest-admin-common` in the docs workflow:

```yaml
- name: Checkout mq-rest-admin-common
  uses: actions/checkout@v4
  with:
    repository: wphillipmoore/mq-rest-admin-common
    ref: develop
    path: .mq-rest-admin-common
```

## Shared Fragment Architecture

Narrative content shared across repos lives in
`mq-rest-admin-common/fragments/`. Each repo includes these fragments
using `pymdownx.snippets`:

```markdown
--8<-- "shared-architecture-intro.md"
```

Fragments are pure Markdown with no toolchain-specific syntax. This ensures
they work in any repo's documentation build.
