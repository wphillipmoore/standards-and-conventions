# Development Environment and Tooling

## Table of Contents
- [Purpose](#purpose)
- [Virtual Environment Requirement](#virtual-environment-requirement)
- [Python invocation and venv activation](#python-invocation-and-venv-activation)
- [External Tooling Dependencies](#external-tooling-dependencies)
- [Maintenance](#maintenance)

## Purpose
Define baseline expectations for development environments and external tooling.

## Virtual Environment Requirement
All development work and CLI commands must run with the project-specific
environment activated (for example, a virtual environment, toolchain manager,
or containerized dev shell).

Rationale:
- ensures consistent dependency resolution
- avoids system runtime drift
- prevents local versus CI mismatches

## Python invocation and venv activation
Rules:
- Use `python3` for all Python invocations. `python` is forbidden.
- Treat a repository as Python if it contains `pyproject.toml`,
  `requirements*.txt`, `setup.cfg`, `setup.py`, or documentation that declares
  Python usage.
- For Python repositories, activate the project-specific environment before
  running any Python command (application code, tests, utility scripts, or
  ad hoc invocations).
- If a Python repository does not define a project-specific environment, stop
  and establish one before running Python commands.
- For non-Python repositories, do not assume Python is available. If Python is
  required for tooling, create a dedicated environment and document it in the
  external tooling list.

## External Tooling Dependencies
Each repository must maintain a minimal, explicit list of required external
tools. Group dependencies by usage category to keep the list clear.

Recommended categories:
- required for daily workflow
- required for data or database operations
- required for deployment or release operations

Document versions where compatibility matters. Avoid adding tools without a
clear justification.

### Baseline automation assumptions
For AI-assisted workflows in this environment, assume the following are
pre-installed and ready to use:
- `git`
- GitHub CLI (`gh`)

Authentication for GitHub operations is assumed to be configured via
environment (for example, `GH_TOKEN`) so `gh` commands can run non-interactive.

Behavior rules:
- Do not preflight-check `gh` availability or auth status on every session.
- Run the intended `gh` command directly; if it fails, report the failure and
  then run targeted diagnostics (`gh --version`, `gh auth status`) before
  retrying.

## Maintenance
Review tooling lists periodically and remove unused entries. Keep the list
short and precise.
