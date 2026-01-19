# Commit Messages and Authorship

## Table of Contents
- [Commit Message Format](#commit-message-format)
- [Types](#types)
- [Example](#example)
- [Commit Authorship](#commit-authorship)
- [AI Co-Authorship](#ai-co-authorship)
- [AI identity strategy](#ai-identity-strategy)
- [Adding a New AI Service Account](#adding-a-new-ai-service-account)
  - [Step-by-step checklist](#step-by-step-checklist)
  - [Practical example: wphillipmoore-codex](#practical-example-wphillipmoore-codex)
- [Scaling to shared ownership](#scaling-to-shared-ownership)
- [Project-specific AI identities](#project-specific-ai-identities)

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

## AI identity strategy
AI service accounts represent tools, not humans.

Default naming:
- Personal scope: `<owner>-<tool>` (for example, `wphillipmoore-codex`)
- Project scope: `<project>-<tool>` (for example, `mnemosys-codex`)
- Shared or org scope: `<org>-<tool>` or `ai-<tool>` when multiple humans share
  responsibility

All repositories must list approved AI identities in
`docs/standards-and-conventions.md`. Only those identities may be used in
commit trailers.

## Adding a New AI Service Account
When onboarding a new AI tool, create a dedicated service account to preserve
clear attribution.

### Step-by-step checklist
1. Sign out of GitHub or use a private browsing session so the new account is
   created separately.
2. Create a GitHub account with the chosen name (per AI identity strategy).
3. Use a dedicated email alias for signup to avoid creating a new inbox.
4. Verify the email address.
5. Enable 2FA with an authenticator app and store recovery codes securely.
6. Set email visibility to private.
7. Copy the account's GitHub noreply email from Settings -> Emails.
8. Add the account to the approved AI identity list in
   `docs/standards-and-conventions.md`.

Then update the repository-specific AI co-author list in
`docs/standards-and-conventions.md`.

### Practical example: wphillipmoore-codex
Create the account:
1. Username: `wphillipmoore-codex`
2. Signup email: `w.phillip.moore+github-codex@gmail.com`
3. Verify the email after signup.
4. Enable 2FA and save recovery codes.
5. Set email visibility to private.
6. Copy the noreply email and record it in `docs/standards-and-conventions.md`:
   - `255923655+wphillipmoore-codex@users.noreply.github.com`

### Practical example: wphillipmoore-claude
Create the account:
1. Username: `wphillipmoore-claude`
2. Signup email: `w.phillip.moore+github-claude@gmail.com`
3. Verify the email after signup.
4. Enable 2FA and save recovery codes.
5. Set email visibility to private.
6. Copy the noreply email and record it in `docs/standards-and-conventions.md`:
   - `255925739+wphillipmoore-claude@users.noreply.github.com`

## Scaling to shared ownership
When multiple humans share responsibility:
- Prefer shared tool identities (`<org>-<tool>` or `ai-<tool>`) over
  person-scoped accounts.
- Keep the human as the commit author; add the AI tool as a co-author.
- Store credentials in a shared secret manager with owner rotation and
  documented recovery procedures.
- Re-evaluate identity naming when ownership changes or repositories move to
  an organization.

## Project-specific AI identities
Maintain approved AI co-author identities in
`docs/standards-and-conventions.md` for each repository. Use only the identities
listed there when adding co-author trailers.
