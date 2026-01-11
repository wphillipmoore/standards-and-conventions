# Hotfix Policy

## Table of Contents
- [Status](#status)
- [1. Purpose](#1-purpose)
- [2. Definition](#2-definition)
- [3. Branching Rules](#3-branching-rules)
- [4. Merge Requirements](#4-merge-requirements)
- [5. Cultural Invariant](#5-cultural-invariant)
- [6. Postmortem Requirement](#6-postmortem-requirement)
- [7. Forbidden Practices](#7-forbidden-practices)
- [8. Guiding Principle](#8-guiding-principle)

## Status
Frozen v0.1 snapshot

---

## 1. Purpose
Define the hotfix process as a controlled failure mode.

Hotfixes exist to correct production-blocking issues when normal promotion flow
is insufficient. They are expected to be rare.

---

## 2. Definition
A hotfix is a change that:
- addresses a production outage or critical defect
- cannot wait for standard develop to release to main promotion
- requires immediate correction in production

---

## 3. Branching Rules
Hotfixes use the following branch namespace:

```
hotfix/<concise-description>
```

Rules:
- branch from main
- fix only the production issue
- no unrelated refactors or enhancements

---

## 4. Merge Requirements
A hotfix branch must:
1. be merged into main
2. be forward-merged into release
3. be forward-merged into develop
4. produce a new release version
5. be deleted immediately

Skipping any step is forbidden.

---

## 5. Cultural Invariant
Creating a hotfix is an explicit signal of process failure upstream.

The system is intentionally designed to make hotfixes:
- visible
- slightly painful
- operationally expensive

This discourages normalization.

---

## 6. Postmortem Requirement
Every hotfix requires a brief written postmortem addressing:
- root cause
- why the issue escaped test
- what process change prevents recurrence

No blame. Only system correction.

---

## 7. Forbidden Practices
- using hotfixes for convenience
- long-lived hotfix branches
- bypassing release validation post-hotfix
- treating hotfixes as normal workflow

---

## 8. Guiding Principle
Hotfixes are allowed, not accepted.
