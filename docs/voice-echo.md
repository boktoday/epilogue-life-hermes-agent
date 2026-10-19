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


## Avatar: their face, their voice, reading their plan (researched Oct 2026)

The simplest avatar is not a stack of open-source models. It is a still portrait plus the cloned voice audio, run through a hosted lipsync API. Providers that accept exactly that input (one photo + one audio file, no driving video):

| Route | Input | Price | Notes |
|---|---|---|---|
| **Runway Lip Sync** | image/video + audio or text | 5 credits/sec = **/usr/bin/bash.05/s**; up to 40s per dialogue, 10 dialogues, 2K | Key already in this house (rw-generate-video skill). 3-minute plan ~=  |
| **Kling Avatar V2** | photo + audio, follows audio length (up to 5 min) | **/usr/bin/bash.056/s** on fal, **/usr/bin/bash.035/s** on PoYo (standard) | Cheapest quality route; 30s ~ .05-1.68 |
| **OmniHuman 1.5** (BytePlus/fal) | image + audio, 5-35s steps | **/usr/bin/bash.12-0.16/s** | Whole-body motion, best realism; 3 min ~= 2-29. Final-render tool, not iteration |
| **Higgsfield Speak / Lipsync Studio** | photo + audio, several models (Kling Speak, Wan Speak, Speak 2.0) | per-generation, roughly /usr/bin/bash.86-4.22 per 5s clip by model | Key already in this house (Higgsfield). Good for a first test |
| **Seedance (BytePlus/fal)** | text/image to video | video only | No confirmed photo+audio lipsync path. Use for b-roll, not talking heads |
| **Runway Act-Two** | needs a driving PERFORMANCE VIDEO | /usr/bin/bash.05/s | Wrong tool here: we have a photo and audio, not footage of the person acting |
| **Open source (MuseTalk/LatentSync/SadTalker)** | photo then audio pipeline | free except hardware | Needs GPU (8-18GB VRAM); CPU demo is 3-5s per frame. Only for strict offline families |

### Recommendation

- **Default: Runway Lip Sync** with the existing key. Photo plus the Fish-cloned audio, chapter by chapter (Runway allows up to 40s per dialogue, ten dialogues in one generation, so a 3-4 minute plan fits in one job at 2K). About  per plan at /usr/bin/bash.05/s.
- **Budget: Kling Avatar V2 on fal or PoYo** (/usr/bin/bash.035-0.056/s). Same inputs, slightly more stiffness, roughly half the price.
- **Premium: OmniHuman 1.5** when the family wants shoulders and hands moving, not just a face. Quote it as a premium option, not a default.
- **First test: Higgsfield Speak** on the existing account, to see whether a talking photo lands emotionally before wiring a pipeline.
- **Offline-only families: MuseTalk** on a GPU machine, or voice-only playback (no avatar). Never pretend the local route is cheap.

### Assembly

voice (.mp3) + portrait (.jpg) -> lipsync API per chapter -> ffmpeg concat -> plan-avatar.mp4 in the family folder, with a 5-second synthetic-disclosure card as the first frame and the consent file beside it. Same ethics section above applies unchanged, and the avatar never speaks anything the person did not write.
