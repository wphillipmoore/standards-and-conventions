# EU and Canada alternatives to GitHub and AWS (non-US ownership)

## Table of Contents

- [Purpose](#purpose)
- [Scope and constraints](#scope-and-constraints)
- [Evaluation criteria](#evaluation-criteria)
- [Findings](#findings)
  - [Sovereignty drivers and policy signal](#sovereignty-drivers-and-policy-signal)
  - [US jurisdiction exposure and transfer risk](#us-jurisdiction-exposure-and-transfer-risk)
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
- Jurisdictional exposure and transfer mechanisms; validate legal exposure and
  exit options.
- Contract transparency and switching expectations under the EU Data Act.

## Findings

### Sovereignty drivers and policy signal

- The European Commission launched a EUR 180 million tender (10 October 2025)
  to procure sovereign cloud services for EU institutions under a Cloud
  Sovereignty Framework. This is a clear policy signal and likely to shape
  public-sector vendor requirements.[1]
- The European Alliance for Industrial Data, Edge and Cloud is an EU-backed
  initiative to strengthen European cloud and edge capabilities and define
  investment roadmaps, reinforcing the political priority of EU-based
  infrastructure.[2]
- The EU Data Act (Regulation (EU) 2023/2854) applies from 12 September 2025
  and introduces switching expectations for cloud services, including minimum
  cloud contract requirements and safeguards against unlawful third-country
  access to non-personal data held in the EU.[3] [4]
- In the current political climate, European governments are actively reducing
  reliance on U.S. tech providers. France announced that 2.5 million civil
  servants will move off U.S. video-conferencing tools by 2027 in favor of a
  domestic platform, and other public bodies are shifting to open-source
  alternatives to reduce dependency.[5]

### US jurisdiction exposure and transfer risk

- The U.S. CLOUD Act allows U.S. courts to compel U.S. providers to disclose
  data in their possession, custody, or control regardless of where it is
  stored. US-owned vendors therefore create jurisdictional exposure even with
  EU or Canadian data residency.[6]
- The EU-U.S. Data Privacy Framework adequacy decision (2023/1795) allows
  transfers of EU personal data to U.S. organizations on the DPF list and
  requires ongoing Commission monitoring. The EDPB welcomed improvements but
  flagged concerns about scope, onward transfers, bulk collection, and
  redress.[7] [8]

### Git hosting

- Codeberg is operated by Codeberg e.V., a registered nonprofit association
  based in Berlin, Germany, and is community-owned. Its FAQ states that most
  services run on their own hardware in Berlin, with some tasks offloaded to
  netcup and Hetzner for redundancy and backups, and that they avoid large
  cloud providers where possible. It is Forgejo-based and offers additional
  services like hosted CI. This fits the non-US-ownership requirement.[9] [10]
- Codeberg offers Forgejo Actions but hosts Actions only in limited fashion
  due to security and staffing constraints. It recommends Woodpecker CI if
  you need hosted CI, and supports connecting your own runners.[11]
- Forgejo Actions is designed to be familiar to GitHub Actions but is not
  compatible; minor workflow changes are expected.[12]
- Worktree stores data in Canada and documents that Git, LFS, attachments,
  packages, and related services run on OVH bare metal in Montreal, with
  backups in OVH Toronto. It lists Actions as running on AWS Montreal.[13]
  The Worktree Actions launch post says workflows run on DigitalOcean Toronto.
  Both AWS and DigitalOcean are US-owned, so hosted Actions currently conflict
  with the non-US-ownership requirement.[13] [14]

### CI and CD

- Codeberg can run CI with Woodpecker or with self-hosted Forgejo Actions
  runners; hosted Actions are limited.[11]
- Worktree Actions is GitHub Actions-compatible, but the documented execution
  layer is on US-owned infrastructure (AWS Montreal and/or DigitalOcean
  Toronto), so self-hosted runners or an alternate CI system are required
  to meet the ownership constraint.[13] [14]

### Managed PostgreSQL and API hosting

- Scaleway provides a managed PostgreSQL service and is a Paris-registered
  company. Managed PostgreSQL is available in the Paris, Amsterdam, and
  Warsaw regions.[15] [16] [17]
- OVHcloud offers managed PostgreSQL (DBaaS) on its public cloud, with a
  Canada-specific offering documented on its OVHcloud Canada site. Use this if
  you need DBaaS convenience, and verify ownership and region availability as
  part of due diligence.[18]
- IONOS provides DBaaS for PostgreSQL with managed features (backups, scaling,
  monitoring) and states that DBaaS is offered in all IONOS Cloud locations.[19]
- ThinkOn positions itself as a 100% Canadian-owned and operated sovereign
  cloud. It is a strong fit for Canadian ownership but does not document a
  managed PostgreSQL service in the referenced material.[20]

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

- If any US-owned services remain in the stack, document CLOUD Act exposure and
  apply strong contractual and technical controls (encryption, key ownership).[6]
- Codeberg hosted Actions are limited; use Woodpecker or self-hosted runners
  if you need stable CI capacity.[11]
- Worktree hosted Actions currently run on US-owned infrastructure (AWS or
  DigitalOcean). This conflicts with the non-US-ownership requirement unless
  you run your own runners.[13] [14]
- Codeberg storage limits exist; confirm that repository and LFS usage fits
  within current quotas or request exceptions.[21]
- Validate vendor subprocessors (billing, monitoring, support) before
  commitment, since ownership and data residency can be affected by them.
- Ensure vendor contracts and exit plans reflect EU Data Act requirements on
  switching and contract transparency; obligations apply from 12 September
  2025.[3] [4]
- If you rely on the EU-U.S. Data Privacy Framework for any data transfers,
  confirm vendor certification status and track regulatory changes, as the
  framework is subject to ongoing monitoring and has unresolved concerns.[7] [8]

## References

[1]: <https://commission.europa.eu/news-and-media/news/commission-moves-forward-cloud-sovereignty-eur-180-million-tender-2025-10-10_en>
[2]: <https://digital-strategy.ec.europa.eu/en/policies/cloud-alliance>
[3]: <https://eur-lex.europa.eu/eli/reg/2023/2854>
[4]: <https://digital-strategy.ec.europa.eu/en/news/european-data-act-enters-force-putting-place-new-rules-fair-and-innovative-data-economy>
[5]: <https://apnews.com/article/europe-digital-sovereignty-big-tech-9f5388b68a0648514cebc8d92f682060>
[6]: <https://www.congress.gov/crs-product/LSB10125>
[7]: <https://eur-lex.europa.eu/eli/dec_impl/2023/1795/>
[8]: <https://www.edpb.europa.eu/news/news/2023/edpb-welcomes-improvements-under-eu-us-data-privacy-framework-concerns-remain_en>
[9]: <https://docs.codeberg.org/getting-started/what-is-codeberg/>
[10]: <https://docs.codeberg.org/getting-started/faq/>
[11]: <https://docs.codeberg.org/ci/actions/>
[12]: <https://forgejo.org/docs/v12.0/user/actions/github-actions/>
[13]: <https://docs.worktree.ca/sovereignty/>
[14]: <https://about.worktree.ca/blog/2025-03-07-worktree-actions/>
[15]: <https://www.scaleway.com/en/legal-notice/>
[16]: <https://www.scaleway.com/en/docs/managed-databases-for-postgresql-and-mysql/>
[17]: <https://www.scaleway.com/en/developers/api/managed-databases-for-postgresql-and-mysql/>
[18]: <https://www.ovhcloud.com/fr-ca/public-cloud/postgresql/>
[19]: <https://docs.ionos.com/cloud/databases/postgresql/overview>
[20]: <https://thinkon.com/resources/data-sovereignty-myth/>
[21]: <https://blog.codeberg.org/new-storage-limits-on-codeberg-what-you-need-to-know.html>
