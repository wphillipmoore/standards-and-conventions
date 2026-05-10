# Skills overview

## Table of Contents
- [Purpose](#purpose)
- [Scope](#scope)
- [Skill list](#skill-list)
- [Usage conventions](#usage-conventions)
- [Local installation](#local-installation)
- [Downstream references](#downstream-references)

## Purpose
Provide a canonical, repository-managed set of Codex skills derived from the
standards in this repository.

## Scope
These skills are shared across repositories that adopt the standards here.
Skill bodies must remain aligned with the canonical documents they reference.

## Skill list

- `rtfm` (`skills/rtfm/SKILL.md`): RTFM forced interruption handling with
  failure context capture and issue tracking.
- `project-issue` (`skills/project-issue/SKILL.md`): guided project issue
  creation with required attribute collection and project assignment.
- `branch-workflow` (`skills/branch-workflow/SKILL.md`): issue-linked branch
  creation with existing branch detection.

Skills previously hosted here (summarize, pr-workflow, dependency-update,
deprecation-triage, publish) have been migrated to the standard-tooling
plugin.

## Usage conventions
- Keep skills minimal and procedural; defer rationale to the standards.
- Update skills when the referenced standards change.
- Do not duplicate standards verbatim; link to canonical docs instead.
- Autocomplete favors distinct skill names; summarize wrappers exist so teams
  can select a mode without typing additional arguments.

## Local installation

Claude Code discovers slash commands by scanning `~/.claude/skills/` for
directories containing a `SKILL.md` file. To make skills from this repository
available as `/commands` in all projects, create symlinks:

```bash
ln -s /path/to/standards-and-conventions/skills/<skill-name> ~/.claude/skills/<skill-name>
```

**When adding a new skill**: always create the corresponding symlink in
`~/.claude/skills/` after merging. The skill will not be available as a slash
command until the symlink exists and the agent session is restarted.

## Downstream references
Add a short reference to these skills in downstream `AGENTS.md` files using
placeholders for the local path to the standards repository.

Example snippet (replace placeholders):
```
## Shared skills
- Load all skills from: <standards-repo-path>/skills/**/SKILL.md
- Treat every skill found under that directory as available and active.
```
