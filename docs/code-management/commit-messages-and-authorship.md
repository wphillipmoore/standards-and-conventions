# Commit Messages and Authorship

## Table of Contents
- [Commit Message Format](#commit-message-format)
- [Types](#types)
- [Example](#example)
- [Commit Authorship](#commit-authorship)
- [AI Co-Authorship](#ai-co-authorship)
- [Adding a New AI Service Account](#adding-a-new-ai-service-account)
- [Repository-Specific AI Identities](#repository-specific-ai-identities)

## Commit Message Format
Follow Conventional Commits:

```
<type>: <short description>

<optional detailed description>

<footer with co-authorship and generation info>
```

## Types
- feat
- fix
- docs
- style
- refactor
- test
- chore

## Example
```
fix: update API routers for renamed terminology

Updated API routers and schemas to use the new naming convention.
Fixed import order in fixtures to ensure metadata is registered.

Co-Authored-By: ai-tool <id+ai-tool@users.noreply.github.com>
```

## Commit Authorship
All commits must be authored by a human. The human owns responsibility and
accountability for the change.

Do not set AI tooling as the author or committer.

## AI Co-Authorship
If an AI tool materially contributed to the change, include a co-author trailer
for that tool.

If no AI tool contributed, omit AI co-authors.

## Adding a New AI Service Account
When onboarding a new AI tool, create a dedicated service account to preserve
clear attribution.

Setup steps:
1. Create a GitHub account named `ai-<tool>`.
2. Use an email alias for signup to avoid creating a new inbox.
3. Enable 2FA and keep the email address private.
4. Copy the account's GitHub noreply email from Settings -> Emails.

Then update the repository-specific AI co-author list below.

## Repository-Specific AI Identities
Maintain the approved AI co-author identities here. Use these exact identities
when adding co-author trailers.

```
Co-Authored-By: ai-tool <id+ai-tool@users.noreply.github.com>
```
