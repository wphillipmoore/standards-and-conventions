# Deprecation Warning Policy

## Purpose

Define a consistent policy for triaging and resolving deprecation warnings so
they do not accumulate silently or trigger ad hoc upgrades.

## Scope

Applies to deprecation warnings emitted by runtimes, libraries, tooling, or
frameworks during development, testing, or execution.

## Definitions

- Deprecation warning: A notice that a behavior or API will be removed or
  changed in a future release.
- Development cycle: Starts when a release is promoted to test and the
  application `MAJOR` or `MINOR` version is incremented, and ends when the
  next version is promoted to test.
- User-visible warning: A warning surfaced to end users of the product UI.
  Developer, administrator, or operator warnings are not user-visible.

## Triage workflow

When a deprecation warning is encountered:

1. Search the project repository's GitHub issues for an existing issue that
   matches the warning text, warning code, and location.
2. If an issue already exists and the warning is encountered mid-cycle, do not
   fix it immediately; defer it to the dependency upgrade at the start of the
   next cycle.
3. If no issue exists, create a GitHub issue with the warning details and
   initial investigation notes.
4. Attempt to remove the warning by code changes if the fix does not require a
   dependency upgrade.
5. If removing the warning requires a dependency upgrade, defer it to the
   start-of-cycle dependency update.
6. When revisiting an open warning issue, update it with the latest attempt and
   outcome; close it when the warning is resolved.

## Dependency upgrade handling

Dependency upgrades must proceed independently of unresolved warnings.

After the upgrade process:

- Re-test existing warnings to confirm whether they still reproduce.
- If a warning persists, attempt to resolve it using the triage workflow.

New warnings may not surface during the upgrade test run, which is why the
mid-cycle warning policy exists.

## Warning suppression policy

- AI tooling must not suppress warnings by default.
- If a warning is user-visible and deferred, suppress it to avoid exposing
  end users to internal warnings.
- Do not suppress warnings for developers, administrators, or operators.
- Suppression must be documented in the deprecation issue and removed when the
  warning is resolved.

## Issue template

Use a consistent issue template so warnings are searchable and comparable.

```text
Title: Deprecation: <dependency or component> - <short description>

Warning text:
<full warning message>

Location:
- file/module:
- call site:
- environment (dev/test/prod):

Reproduction:
- minimal command or steps:
- notes on reproducibility:

First seen:
- date:
- version:

Impact assessment:
- user-visible: yes/no
- behavior risk:

Attempted fixes:
- code changes tried:
- result:

Upgrade assessment:
- required dependency version:
- upgrade scope:

Decision:
- fix now / defer to next cycle
- rationale:

Suppression (if any):
- suppression method:
- removal criteria:
```

## Related documents

- Python dependency management: [dependency-management.md](python/dependency-management.md)
- Application versioning scheme: [application-versioning-scheme.md](../code-management/versioning/application-versioning-scheme.md)
