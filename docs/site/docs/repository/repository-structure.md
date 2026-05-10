# Repository Structure Standards

## Purpose

Provide a default repository layout that is explicit, discoverable, and easy to
maintain over time.

## Core Principles

- Favor boring, explicit structure over cleverness.
- Preserve survivability without original authorship.
- Keep top-level organization shallow (no more than three levels deep at the
  root, excluding language package internals).
- Separate source code, tests, documentation, and tooling.

## Top-Level Layout

Use the following directories by default:

- `docs/`: documentation and standards
- `docs/decisions/`: Architecture Decision Records (ADRs)
- `src/`: production source code (when applicable)
- `tests/`: tests that mirror the source layout
- `scripts/`: developer tooling and automation
- `skills/`: repository-local agent skills (when applicable)
- `.github/`: CI/CD workflows and repository configuration

Additional directories (for example, `infra/` or `deploy/`) are allowed when
they are essential and clearly scoped.

## Tests

Tests should mirror the `src/` layout as closely as practical. If the language
uses a different convention, document the rationale and keep it consistent.

## Documentation and Decision Records

Documentation lives under `docs/`.

Use `docs/decisions/` for ADRs. Naming and structure:

- Filenames: `NNNN-short-title.md` (zero-padded numeric prefix)
- Required sections: Status, Context, Decision, Consequences
- Keep the decision record immutable once accepted; revisions require a new
  ADR that references the original

Each repository must include `docs/repository-standards.md` that:

- documents the repository profile attributes
- documents project-specific overlays and deviations from shared standards

## Examples

```text
repo/
├── docs/
│   ├── decisions/
│   │   └── 0001-repo-structure.md
│   └── overview.md
├── src/
│   └── <package_or_app>/
├── tests/
│   └── <package_or_app>/
├── scripts/
├── skills/
├── .github/
│   └── workflows/
└── README.md
```

## Revisiting the Structure

If the repository structure becomes unclear or burdensome, record the change
as a new ADR. Structure changes should be deliberate, not ad hoc.
