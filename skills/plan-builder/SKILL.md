---
name: plan-builder
description: "Use when assembling the Epilogue Life Plan document."
version: 1.0.0
author: Brendan O'Keefe (boktoday), Hermes Agent
license: PolyForm Noncommercial 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [plan, output, epilogue-life, third-age]
---

# Plan Builder

Assembles everything into **the Epilogue Life Plan**: the finished document, in markdown and as a beautiful printable page. This is the product; everything else feeds it.

## When to use

- The person says "build my plan" or "I want to see it all together".
- Monthly review suggests a rebuild; letters or last-days pages have grown.

## Structure of the plan

1. **Cover**: name, date, one line from their reflection.
2. **About me**: from profile; their words.
3. **My people**: loved ones, and who is closest to decisions.
4. **What matters most**: values and beliefs.
5. **My answers, area by area**: all answered questions, their words.
6. **My reflection**: the woven piece.
7. **Letters**: listed per person with "read when" notes. (Letters can be excluded from a given copy; families do not accidentally read everything.)
8. **My final chapter**: last-days preferences.
9. **My arrangements**: funeral or celebration wishes, donation decisions, digital legacy.
10. **The soundtrack**: playlists.
11. **Where the official documents live**: pointers only (will, directive, DNR); never their contents.

## What you do

1. Read everything; check `progress.json` for skipped areas and leave a respectful "Not covered" line rather than inventing content.
2. Write `shared/plan/EPILOGUE-LIFE-PLAN.md` first; show it; corrections welcome, then rebuild.
3. Generate `shared/plan/epilogue-life-plan.html`: single file, warm design, print-first (A4 margins, page breaks before major sections, readable at 70). No external dependencies except fonts; it must open offline.
4. Add the honesty line at the foot: "This plan records wishes. It is not a will, not legal or medical advice; official documents are held separately."
5. Offer the next step: print it, or share it via Share The Plan.

## Rails

- Never auto-send anywhere. The plan moves only through explicit sharing.
- Big rebuilds wait until the person asks; small updates happen silently and are mentioned.

## Collaboration

| Need | Goes to |
|---|---|
| Missing content | The relevant skill, gently offered |
| Sharing | Share The Plan |
