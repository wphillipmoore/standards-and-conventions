# Development Environment and Tooling

## Table of Contents
- [Purpose](#purpose)
- [Virtual Environment Requirement](#virtual-environment-requirement)
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

## External Tooling Dependencies
Each repository must maintain a minimal, explicit list of required external
tools. Group dependencies by usage category to keep the list clear.

Recommended categories:
- required for daily workflow
- required for data or database operations
- required for deployment or release operations

Document versions where compatibility matters. Avoid adding tools without a
clear justification.

## Maintenance
Review tooling lists periodically and remove unused entries. Keep the list
short and precise.
