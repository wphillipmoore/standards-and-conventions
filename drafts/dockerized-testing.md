# Dockerized Testing (Draft)

## Table of Contents
- [Status](#status)
- [Purpose](#purpose)
- [Scope](#scope)
- [Decisions](#decisions)
- [Workflow outline](#workflow-outline)
- [Image strategy](#image-strategy)
- [Determinism and parity](#determinism-and-parity)
- [Open items](#open-items)

## Status
Draft for validation in a working repository. This document will be replaced by
final guidance once the approach is proven.

## Purpose
Define a Docker-first testing workflow that provides deterministic results
across macOS, Windows, and Linux while aligning local and CI execution.

## Scope
Applies to repositories that run unit tests in a Linux container with a pinned
Python runtime and managed dependencies.

## Decisions
- Unit tests run only inside Docker containers; host virtual environments are
  unsupported for test execution.
- The test image is repository-specific.
- The Python runtime is pinned to an explicit patch version for the duration of
  a development cycle.

## Workflow outline
- Build or refresh the repository test image when the lockfile or runtime
  version changes.
- Run unit tests in a container with the repository mounted as a working
  directory.
- Use persistent caches for dependency installs to keep local runs fast.
- Keep the host Python install optional; it should not be required for tests.

## Image strategy
- Base the image on the pinned Python `x.y.z` runtime.
- Install dependencies from the lockfile and avoid ad hoc installs.
- Ensure the image can be rebuilt deterministically from repository state.

## Determinism and parity
- The same containerized workflow must be usable locally and in CI.
- Test execution must not depend on host OS Python behavior.
- Prefer Linux-based containers to match deployment environments.

## Open items
- Define how integration-test services (databases, caches, queues) will be
  orchestrated and versioned.
- Decide whether additional tooling (linters, formatters, type checkers) runs
  inside the same test image or a separate tooling image.
