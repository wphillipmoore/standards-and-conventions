# EU and Canada alternatives to GitHub and AWS (non-US ownership)

## Table of Contents

- [Purpose](#purpose)
- [Scope and constraints](#scope-and-constraints)
- [Evaluation criteria](#evaluation-criteria)
- [Findings](#findings)
  - [Git hosting](#git-hosting)
  - [CI and CD](#ci-and-cd)
  - [Managed PostgreSQL and API hosting](#managed-postgresql-and-api-hosting)
- [Recommendations](#recommendations)
  - [EU-based recommendation](#eu-based-recommendation)
  - [Canada-based recommendation](#canada-based-recommendation)
- [Migration path (next 12 months)](#migration-path-next-12-months)
- [Risks and open questions](#risks-and-open-questions)
- [References](#references)

## Purpose

Provide a concise, decision-ready report on non-US-owned alternatives to
GitHub and AWS, with final recommendations for both an EU-based and a
Canada-based stack.

## Scope and constraints

- Non-US-owned providers only.
- Canada or EU jurisdiction is acceptable.
- US-based infrastructure is acceptable for about 12 months, as long as there
  is a non-US-owned path and a non-US-based migration target.
- SaaS Git hosting is preferred.
- CI/CD can be reimplemented and does not need full GitHub Actions parity.
- Primary workloads are managed PostgreSQL and REST APIs.

## Evaluation criteria

- Ownership: non-US parent company.
- Data residency options in EU or Canada.
- Viable CI/CD path without US-owned hosted runners.
- Managed PostgreSQL availability.
- Low operational overhead.

## Findings

### Git hosting

- Codeberg is operated by Codeberg e.V., a registered nonprofit association
  based in Berlin, Germany, and is community-owned. Its FAQ states that most
  services run on their own hardware in Berlin, with some tasks offloaded to
  netcup and Hetzner for redundancy and backups, and that they avoid large
  cloud providers where possible. It is Forgejo-based and offers additional
  services like hosted CI. This fits the non-US-ownership requirement.
- Codeberg offers Forgejo Actions but hosts Actions only in limited fashion
  due to security and staffing constraints. It recommends Woodpecker CI if
  you need hosted CI, and supports connecting your own runners.
- Forgejo Actions is designed to be familiar to GitHub Actions but is not
  compatible; minor workflow changes are expected.
- Worktree stores data in Canada and documents that Git, LFS, attachments,
  packages, and related services run on OVH bare metal in Montreal, with
  backups in OVH Toronto. It lists Actions as running on AWS Montreal.
  The Worktree Actions launch post says workflows run on DigitalOcean Toronto.
  Both AWS and DigitalOcean are US-owned, so hosted Actions currently conflict
  with the non-US-ownership requirement.

### CI and CD

- Codeberg can run CI with Woodpecker or with self-hosted Forgejo Actions
  runners; hosted Actions are limited.
- Worktree Actions is GitHub Actions-compatible, but the documented execution
  layer is on US-owned infrastructure (AWS Montreal and/or DigitalOcean
  Toronto), so self-hosted runners or an alternate CI system are required
  to meet the ownership constraint.

### Managed PostgreSQL and API hosting

- Scaleway provides a managed PostgreSQL service and is a Paris-registered
  company. Managed PostgreSQL is available in the Paris, Amsterdam, and
  Warsaw regions.
- OVHcloud offers managed PostgreSQL (DBaaS) on its public cloud, with a
  Canada-specific offering documented on its OVHcloud Canada site. Use this if
  you need DBaaS convenience, and verify ownership and region availability as
  part of due diligence.
- IONOS provides DBaaS for PostgreSQL with managed features (backups, scaling,
  monitoring) and states that DBaaS is offered in all IONOS Cloud locations.
- ThinkOn positions itself as a 100% Canadian-owned and operated sovereign
  cloud. It is a strong fit for Canadian ownership but does not document a
  managed PostgreSQL service in the referenced material.

## Recommendations

### EU-based recommendation

#### Codeberg + Scaleway (EU-only deployment)

- Git hosting: Codeberg (Berlin-based nonprofit, EU-hosted core services).
- CI/CD: Use Codeberg with Woodpecker CI for hosted builds, or run Forgejo
  Actions with self-hosted runners on Scaleway if you need tighter control.
- Data and APIs: Scaleway Managed PostgreSQL in EU regions, with API hosting
  on Scaleway compute.

Why this fits:

- Non-US ownership end-to-end.
- EU-based infrastructure for Git, CI, and data.
- Low operational overhead (managed Postgres).
- Clear migration path without swapping vendors.

### Canada-based recommendation

#### Worktree (Git) + ThinkOn (compute and data) + self-hosted CI

- Git hosting: Worktree (data stored in Canada; Git/LFS/etc on OVH Montreal).
- CI/CD: Avoid Worktree hosted Actions for now; run self-hosted runners on
  ThinkOn (or another Canadian-owned provider). Use Forgejo Actions or
  Woodpecker, depending on how much you want to keep Action-like workflows.
- Data and APIs: Host APIs on ThinkOn. For PostgreSQL, either run your own
  managed-by-you cluster on ThinkOn, or use OVHcloud Managed PostgreSQL (Canada
  offering) if you need DBaaS convenience and are satisfied with the provider's
  ownership and region verification.

Why this fits:

- Non-US-owned infrastructure for compute and data via ThinkOn.
- Canadian data residency today, with a clear non-US-owned path when you move.
- CI/CD can be run on Canadian-owned infrastructure via self-hosted runners.

If you need strictly Canadian-owned infrastructure, use ThinkOn for compute
and storage and run PostgreSQL yourself (or verify ThinkOn for managed
PostgreSQL). This increases operational effort but meets the ownership bar.

## Migration path (next 12 months)

1. Stand up non-US-owned infrastructure now (EU or Canada) and run production
   there, even while you remain in the US, to avoid a later data migration.
2. Migrate Git repositories to Codeberg or Worktree, then rewire CI to
   self-hosted runners on the chosen provider.
3. Move PostgreSQL to the chosen managed service and deploy APIs on the same
   provider to keep data flow inside the target jurisdiction.

## Risks and open questions

- Codeberg hosted Actions are limited; use Woodpecker or self-hosted runners
  if you need stable CI capacity.
- Worktree hosted Actions currently run on US-owned infrastructure (AWS or
  DigitalOcean). This conflicts with the non-US-ownership requirement unless
  you run your own runners.
- Codeberg storage limits exist; confirm that repository and LFS usage fits
  within current quotas or request exceptions.
- Validate vendor subprocessors (billing, monitoring, support) before
  commitment, since ownership and data residency can be affected by them.

## References

- [Codeberg FAQ (hosting location and infrastructure)](https://docs.codeberg.org/getting-started/faq/)
- [Codeberg overview (organization and services)](https://docs.codeberg.org/getting-started/what-is-codeberg/)
- [Codeberg Actions (self-hosted runners and hosted Actions limits)](https://docs.codeberg.org/ci/actions/)
- [Forgejo Actions compatibility notes](https://forgejo.org/docs/v12.0/user/actions/github-actions/)
- [Worktree data sovereignty (provider list)](https://docs.worktree.ca/sovereignty/)
- [Worktree Actions launch (execution environment)](https://about.worktree.ca/blog/2025-03-07-worktree-actions/)
- [Scaleway legal notice](https://www.scaleway.com/en/legal-notice/)
- [Scaleway managed PostgreSQL docs](https://www.scaleway.com/en/docs/managed-databases-for-postgresql-and-mysql/)
- [Scaleway managed PostgreSQL regions (API)](https://www.scaleway.com/en/developers/api/managed-databases-for-postgresql-and-mysql/)
- [OVHcloud public cloud PostgreSQL (Canada)](https://www.ovhcloud.com/fr-ca/public-cloud/postgresql/)
- [IONOS PostgreSQL DBaaS overview](https://docs.ionos.com/cloud/databases/postgresql/overview)
- [ThinkOn data sovereignty overview (Canadian ownership)](https://thinkon.com/resources/data-sovereignty-myth/)
- [Codeberg storage limits (quotas)](https://blog.codeberg.org/new-storage-limits-on-codeberg-what-you-need-to-know.html)
