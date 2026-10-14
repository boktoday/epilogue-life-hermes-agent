# Installing Epilogue Life

## 1. Install Hermes Agent

One command on any laptop, Windows / macOS / Linux. Follow the official guide at
https://hermes-agent.nousresearch.com/docs and connect the chat app you already use
(Telegram recommended; it is private and works on any phone).

## 2. Add the profile

Copy these folders into your Hermes profile directory:

- `skills/` -> your profile's `skills/`
- `shared/` -> a plan folder of your choosing (the setup script creates it)
- `schedules/` -> install the three schedules per `schedules/README.md`

The example `config.yaml` shows a working configuration; merge what you need.

## 3. Create your plan folder

```
python scripts/setup-plan-folder.py ~/epilogue-life
```

This creates the folder tree (profile, loved ones, answers, plan), copies the templates,
and drops the question bank inside. Nothing else is needed; the agent finds it from there.

## 4. First conversation

Open your chat with your assistant and say:

> Let's begin my Epilogue Life plan.

The Epilogue Navigator takes over: it introduces itself, explains what this is and is not,
and runs the onboarding at your pace. Onboarding writes `shared/profile.md` and
`shared/loved-ones.md`.

## 5. Gentle schedules (recommended)

Install the daily-questions schedule first. Two or three questions a morning is the
heartbeat of the whole thing. See `schedules/README.md` for the exact commands.

## 6. Optional: email sharing through Maton

To let the agent email your finished plan (or individual letters) to loved ones, add a free
Maton account and the Google Mail connection. See `docs/connections.md`. Nothing is ever
sent without you naming the recipient and confirming, in the moment.

## 7. Optional: run fully offline

Everything here works with local models via LM Studio or Ollama, for complete privacy and
zero ongoing cost. See `docs/local-models.md`.

## Troubleshooting

- The agent does not know my profile: check that `shared/profile.md` exists and has content.
- Questions are not coming daily: verify the schedule is installed and the answer time suits you.
- Email sending fails: check the Maton connection is live; sending is optional and the plan
  prints beautifully regardless.
