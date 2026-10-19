# Voice echo: cloning the plan in your own voice

The original Epilogue idea: the person's final plan, written in their own words and spoken in their own voice. This note records where that feature stands and what the options cost in October 2026.

**Status in this repo:** no voice or cloning code exists yet. Neither `epilogue-life-hermes-agent` nor `epilogue-life-website` carries an ElevenLabs integration (searched for voice, audio, tts, eleven, clone: nothing). Whatever existed earlier lived outside these repos.

## What changed since the ElevenLabs build

ElevenLabs is no longer the default. Three shifts:

1. **Fish Audio S2** launched March 2026, ranks #1 on TTS-Arena, posts the best speaker-identity score (4.03) in an independent comparison, clones from about 10 seconds, and costs roughly **$15 per million UTF-8 bytes** against ElevenLabs' ~$165 per million characters. Retail plans from $11-15/month, free tier includes cloning.
2. **MiniMax Speech 2.8** is a strong budget API ($60/M chars Turbo, $100/M HD, $1.50 per clone), but it is China-based, which matters for data residency on something as personal as a voice.
3. **Open weights caught up.** Chatterbox (MIT, Resemble) gives the best small-GPU clone for free; Fish's S2 weights are public for research only; CPU-only machines can use NeuTTS Air (GGUF, BYO voice) at modest quality.

## Recommendation for Epilogue

**Hosted default: Fish Audio S2.** Ten seconds of sample, speech that carries the speaker's character, and a cost so small it is irrelevant at our scale. A final plan of 2,000 words is about 12,000 bytes, so roughly **2 cents per rendered plan**.

**Local option: NeuTTS Air** for families who refuse to upload a voice sample. It runs on a laptop CPU, no GPU, no account. Quality is below hosted, and it is still recognisably the speaker. Document the trade honestly and let the family choose.

**Keep ElevenLabs only if** a family asks for its pro voice cloning (30+ minutes of training audio) or a specific voice library voice. Otherwise it is six to eleven times the price for a marginal gain.

## The ethics, which matter more than the model

Epilogue deals with people planning the end of their lives, and with families who may later want to hear a voice that is gone. That raises the bar:

1. **Consent is recorded, not assumed.** Before cloning: the person reads a consent line on the sample recording (or signs one on paper, photographed and stored). No consent, no clone. Ever.
2. **The consent covers the use.** "My voice may be used to read my plan back to my family" is the default scope. Anything broader needs its own yes.
3. **Synthetic, and said so.** Every rendered audio starts with one spoken line: "This is a synthetic copy of {name}'s voice, made with their permission." File metadata carries the same. No deception of listeners, ever.
4. **One voice, the person's own.** Never clone a third party (a spouse, a parent, someone deceased without documented pre-death permission).
5. **Family-only by default.** The audio lives in the family's folder, not on a public page. Sharing is a deliberate act by the executor.
6. **Deletion means deletion.** One command removes the sample, the clone on the provider, and every rendered file. Record how.
7. **No posthumous generation beyond the plan.** The feature reads the plan the person wrote. It is not a chatbot in their voice, not a comfort simulation. Listening to a parent read their own plan is memory; generating new sentences in a dead person's voice is impersonation. We do the first, never the second.

## Architecture (if we build this)

- `skills/voice-echo/`: consent capture, sample recording (30-60 seconds read of a supplied passage), clone creation, render, deletion.
- Provider abstraction with two backends: `fish` (hosted, default) and `local-neutts` (offline). Config keys: provider, api key name, consent file path.
- Output convention: `shared/plan/voice/consent.mp3`, `sample.wav`, `plan-voice.mp3`, plus a manifest with the consent text, dates and hashes.
- The website gains one section: "Your voice, your words" with the consent and synthetic-disclosure rules stated plainly, above any sample.

## Sources (Oct 2026)

- TTS comparison incl. Fish S2, MiniMax 2.8, ElevenLabs, Chatterbox, Inworld: ocdevel.com TTS roundup (Jul 2025, updated 2026)
- Pricing and identity scores: clonemyvoice.ai comparison, reveo.news API comparison (Q1 2026)
- Consumer tools and plan pricing: renderreport.com, fast.io roundups
