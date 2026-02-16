# Skills overview

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Skill list](#skill-list)
- [Usage conventions](#usage-conventions)
- [Dependency policy](#dependency-policy)
- [Downstream references](#downstream-references)

## Purpose
Provide a canonical, repository-managed set of Codex skills derived from the
standards in this repository.

## Scope
These skills are shared across repositories that adopt the standards here.
Skill bodies must remain aligned with the canonical documents they reference.

## Skill list
- `summarize` (`skills/summarize/SKILL.md`): multi-mode summarization for
  decisions, operations, and SOC capture.
- `summarize-decisions` (`skills/summarize-decisions/SKILL.md`): wrapper for
  decisions summaries (autocomplete-friendly).
- `summarize-operations` (`skills/summarize-operations/SKILL.md`): wrapper for
  operations summaries (autocomplete-friendly).
- `summarize-soc` (`skills/summarize-soc/SKILL.md`): wrapper for SOC capture
  summaries (autocomplete-friendly).
- `pr-workflow` (`skills/pr-workflow/SKILL.md`): pull request workflow with
  docs-only exception handling.
- `dependency-update` (`skills/dependency-update/SKILL.md`): dependency update
  workflow with failure handling and anchor rules.
- `deprecation-triage` (`skills/deprecation-triage/SKILL.md`): deprecation
  warning triage workflow and issue template.
- `publish` (`skills/publish/SKILL.md`): library and documentation publish
  workflow with post-publish dependency updates.
- `rtfm` (`skills/rtfm/SKILL.md`): RTFM forced interruption handling with
  failure context capture and issue tracking.

## Usage conventions
- Keep skills minimal and procedural; defer rationale to the standards.
- Update skills when the referenced standards change.
- Do not duplicate standards verbatim; link to canonical docs instead.
- Autocomplete favors distinct skill names; summarize wrappers exist so teams
  can select a mode without typing additional arguments.

## Dependency policy
- Treat this directory as a reference library.
- Copy shared skills into the target repository's `skills/` directory before
  using them.
- Do not rely on symlinks or external paths for required skills.
- Skills are not auto-registered; restart the agent session after adding them.

## Downstream references
Add a short reference to these skills in downstream `AGENTS.md` files using
placeholders for the local path to the standards repository.

Example snippet (replace placeholders):
```
## Shared skills
- Load all skills from: <standards-repo-path>/skills/**/SKILL.md
- Treat every skill found under that directory as available and active.
```
