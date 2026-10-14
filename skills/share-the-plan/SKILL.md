---
name: share-the-plan
description: "Use when the person wants to share the plan or a letter by email or print."
version: 1.0.0
author: Brendan O'Keefe (boktoday), Hermes Agent
license: PolyForm Noncommercial 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [sharing, email, epilogue-life, third-age]
---

# Share The Plan

Moves the plan (or single letters) to the people they are for: by print, or by email through Maton (Google Mail). Consent is the whole game.

## When to use

- "Send my plan to my daughter."
- "Print this for the family meeting."
- A letter is finished and its "read when" is "now".

## The sharing protocol, always in this order

1. **Name it**: exactly what is being shared (the whole plan? one letter? a copy without specific letters?).
2. **Name them**: the exact recipient(s), with their email address read aloud for confirmation.
3. **Preview**: show the subject line and opening lines of what will go.
4. **Confirm**: an explicit yes, in the moment: "Send it as shown?"
5. **Send** via the Maton Google Mail connection (see `docs/connections.md` and the api-gateway skill).
6. **Log**: append to `shared/plan/shared-log.md`: date, what, to whom, and that consent was given.

## Print-first default

Printing is always offered first: the plan is designed for paper, families read it together, and it needs no accounts. Email is for people far away.

## For letters

- Letters share individually, to their named person, within their "read when" rules.
- Milestone letters ("open when 21") are sent to a trusted holder, clearly marked, or held in the folder for the person to give by hand.
- Never bundle all letters into one email; a letter is personal or it is nothing.

## Rails

- No consent, no send. No exceptions, no "probably fine".
- Never send to a recipient not in `loved-ones.md` without adding them first, with the person present.
- If sending fails, say so plainly and offer print as the fallback.

## Collaboration

| Need | Goes to |
|---|---|
| Build or rebuild first | Plan Builder |
| A new person to add | Navigator (profile update) |
