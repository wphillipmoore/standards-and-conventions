# Rust Development Standards Overview

## Purpose

Define consistent Rust standards that emphasize safety, readability,
maintainability, and long-term survivability across repositories.

## Core Principles

- The Rust API Guidelines and standard library conventions are the default and
  highest priority.
- Safety and correctness override cleverness or brevity.
- Readability overrides micro-optimization.
- Exceptions must be explicit, documented, and justified.

## Tooling Expectations

- Formatting: rustfmt (canonical, zero configuration via `rust-toolchain.toml`).
- Linting: clippy (official Rust linter, 800+ lint rules).
- Type checking: `cargo check` (inherent in the Rust compiler).
- Dependency audit and license compliance: cargo-deny (advisories, licenses,
  bans, and sources in a single tool).
- Coverage: cargo-llvm-cov (LLVM instrumentation, cross-platform).
- Toolchain pinning: `rust-toolchain.toml` (auto-installs the correct toolchain
  via rustup).
- If a repository uses different tools, document the reason and equivalents.

## CI Gates

Every CI check is classified as a hard gate or soft gate.

Hard gate definition:

- Merge-blocking. A required status check must be configured on the target
  branch. Any failure blocks merge until a new commit passes.

Soft gate definition:

- Warning-only. The check can fail without blocking merge, but failures must be
  surfaced with rationale and follow-up tracking when applicable.

Hard gates (all are required status checks):

- `test: unit (current)`
- `test: integration`
- `ci: dependency-audit`

Soft gates:

- None (default to hard gate until documented).

Branch applicability:

- develop: all hard gates required
- release: all hard gates required
- main: all hard gates required

## Document Map

- Naming conventions: [naming-conventions.md](naming-conventions.md)
