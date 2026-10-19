# Epilogue Life (Hermes edition)

A free, open planning companion for your third age, built on **[Hermes Agent](https://hermes-agent.nousresearch.com/docs)**. It walks beside you, one gentle question at a time, and helps you turn a lifetime of wisdom, wishes and practical details into a plan your loved ones can actually hold.

No accounts. No subscriptions. Everything lives in your own folder, on your own machine.

---

## What this is

Epilogue Life was born as a web app. This is the Hermes edition: the same care, the same question bank, and the same purpose, rebuilt so it runs as a personal agent you actually own.

- **Onboarding** builds your profile: who you are, who you love, what matters.
- **The question bank** (35 questions across seven areas) is worked through at your pace, or a few per day by a gentle cron schedule.
- **Reflections, letters, playlists and last-days wishes** grow out of your answers.
- **The Epilogue Life Plan** is the final output: a complete, printable document you can share with the people you love, by hand or by email.
- **Human hand-off rails** throughout: in a hard moment, the agent stops, cares, and points to real people.

---

## The team

| Skill | What it does |
|---|---|
| Epilogue Navigator | Front door: onboarding, your profile, routing, the big picture |
| Life Questions | Works through the 35-question bank at your pace and records every answer |
| Reflection Writer | Weaves your answers into a gentle, truthful reflection of your life |
| Wish I Had Said | Guided messages and letters for the people you love |
| Last Days Planner | Comfort, dignity and preference planning for the final chapter |
| Memory Playlist | The soundtrack of your life, gathered moment by moment |
| Plan Builder | Assembles everything into your Epilogue Life Plan (document + printable page) |
| Share The Plan | Shares by print or email (Maton/Gmail), always with your explicit yes |
| Hard Moments | Crisis, grief and hard family moments: care first, humans always |

Every skill is written to be dignified, honest and unhurried. See `SOUL.md` for the principles and `AGENTS.md` for how the team works together.

---

## How it works

1. **One shared folder.** Every skill reads and writes the same plan folder: `shared/profile.md`, `shared/answers/`, `shared/plan/`. You own it; you can open it, edit it, back it up, or delete it.
2. **One front door.** The Navigator runs your onboarding and introduces every other skill when its moment comes.
3. **Your pace.** Answer questions in one long sitting or two minutes a day. The daily-questions schedule can ask a couple of questions each morning and nothing more; the plan fills in over weeks, not hours.
4. **The plan is the product.** Everything points at the Epilogue Life Plan: a document your family will thank you for.
5. **Sharing is a choice, in the moment.** Nothing is ever sent to anyone without you naming the person and saying yes, then and there.
6. **Honesty about what this is.** Not legal advice, not medical advice, not a will: a planner that helps you get clear, and points you to the professionals for the documents only they can make.

---

## Install

See `INSTALL.md`. Short version:

1. Install Hermes Agent (one command, any laptop).
2. Copy the `skills/`, `shared/` and `schedules/` folders into your Hermes profile.
3. Run `scripts/setup-plan-folder.py` to create your plan folder.
4. Have your first conversation with the Epilogue Navigator.
5. Optionally install the schedules so the questions come to you gently.

---

## Schedules

| Schedule | Rhythm | What it does |
|---|---|---|
| Daily questions | Every morning (time is yours) | Two or three questions from the bank, saved as you answer |
| Weekly reflection | Sunday evening | A gentle look back at the week's answers, one reflection prompt |
| Monthly plan review | Monthly | Progress, wins, and one suggested focus area |

Setup commands are in `schedules/README.md`.

The daily rhythm is the ideal place for a **local model**: small, frequent and private, with nothing to pay per message and nothing leaving the machine. `docs/local-models.md` helps you pick one that fits.

---

## What it is not

- Not a will, not legal or medical advice. It helps you prepare; lawyers, doctors and official forms do the rest.
- Not a replacement for your family, your faith leader, your doctor or your grief counsellor.
- Not a crisis service, and it never pretends to be one. In a hard moment it stops, responds with care, points to the verified lines in `skills/hard-moments/helplines.md`, and hands the matter to a real person.
- Not a companion. It is a support tool that works for you, and says so.

---

## Repository layout

```
skills/            nine skills (each SKILL.md), incl. hard-moments and helplines
shared/            your plan folder templates: profile, loved ones, question bank,
                   answers/ and plan/ (created by the setup script)
schedules/         ready-to-install check-ins (daily questions, weekly, monthly)
SOUL.md            the principles every skill lives by
AGENTS.md          how the team works together
INSTALL.md         full setup guide (including fully-offline local models)
PROFILE_BUILDER.md the guided onboarding
config.yaml        example Hermes configuration
scripts/           setup-plan-folder.py, next_questions.py
docs/              design document + connections + local models
```

---

## License

PolyForm Noncommercial License 1.0.0. Free to use, change and share for any noncommercial purpose, with credit. See `LICENSE`.

Required Notice: Copyright 2026 Brendan O'Keefe (https://onetoeight.org)



## Voice echo: the plan in their own voice

A working feature. With recorded consent, Epilogue clones the person's voice and reads their written plan back to their family, as spoken word. No avatar: voice only, by design.

- Every render opens with a spoken disclosure that the voice is synthetic and made with permission.
- The voice reads what they wrote, never new sentences. Their own voice only. Deletion is one command.
- Details: `docs/voice-echo.md`. Skill: `skills/voice-echo/`. Consent template: `shared/consent-template.md`.
- Demo: [docs/demo/epilogue-voice-demo.mp3](docs/demo/epilogue-voice-demo.mp3) (49 seconds, disclosure line first).
