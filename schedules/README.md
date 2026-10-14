# Schedules: the gentle check-ins

Three ready-to-install rhythms. The daily questions one is the heartbeat; the other two are
optional kindnesses. Ask your assistant to install them, or use the cron commands directly.

## Daily questions (recommended)

Ask your assistant:

> Install my daily questions schedule for [TIME]. Two or three questions from the bank, in
> this chat, saved as I answer. If I do not answer, do not chase; try again tomorrow.

Cron equivalent: `0 9 * * *` (9am daily, Australia/Melbourne timezone, deliver to this chat).
The run reads `shared/answers/progress.json` via `scripts/next_questions.py` and asks the next
two or three questions.

## Weekly reflection (Sunday evening)

> Every Sunday at 5pm, look back at the week's answers, reflect one true thing, and offer one
> gentle prompt. No pressure to write more.

Cron: `0 17 * * 0`.

## Monthly plan review

> On the first of each month, review my progress, celebrate quietly, suggest one focus area,
> and offer to rebuild my plan.

Cron: `0 10 1 * *`.

## House rules for all schedules

- Two or three questions is a full helping. Never more.
- If the person does not respond, the schedule waits politely. No follow-ups, no guilt.
- In a hard moment, the schedule yields to Hard Moments and nothing else is asked that day.
