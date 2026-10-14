# Design notes

## The idea

A will distributes assets. Almost nothing distributes the rest: the wishes, the reasons, the
words, the where-I-want-to-be, the what-I-want-said. Epilogue Life exists so the most
important conversations do not happen too late, or never at all.

## The web app, and why this edition exists

The original app (epilogue-life-pro, 2025) proved the demand: guided questions worked, the
plan meant something. But it required accounts, a subscription, a cloud database and API
keys, and it held sensitive end-of-life data in the cloud. Good fences make bad end-of-life
infrastructure.

This edition keeps the heart and changes the body: an agent in the person's own Hermes, a
folder on their own machine, no accounts, no billing, no cloud.

## Architecture

- Skills (nine) carry all behaviour; the Navigator is the front door.
- The plan folder is the state: profile, loved ones, answers, plan. Plain files, readable
  by humans and agents alike.
- question-bank.json drives the daily schedule; progress.json remembers what is answered,
  skipped or deferred.
- Schedules are ordinary Hermes cron jobs, so the questions come to the person at their
  chosen time without any app at all.
- Sharing is explicit and logged; printing is the first-class path.

## Ethics that shaped the build

- Dignity over engagement: no streaks, no notifications that chase, no gamified guilt.
- Truth over comfort: not a will, not advice; professionals make documents official.
- Hands to humans: grief and crisis always route to real people (hard-moments skill).
- Privacy as architecture, not policy: nothing leaves the folder without consent.
