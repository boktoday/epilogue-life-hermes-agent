---
name: voice-echo
description: "Use when a family wants the plan spoken in their own voice."
version: 2.0.0
---

# Voice echo (voice only)

The plan rendered as spoken word in a synthetic copy of the writer's voice. No avatar. Rolled back 19 October 2026 after the talking-portrait demo was judged too uncanny and too much machinery.

## Non-negotiables

1. **Consent on record first.** Spoken or written, filed in `shared/plan/voice/consent.md`. Template in `shared/consent-template.md`. No consent, no clone, no render.
2. **Their own voice only.** Never clone someone else, and never anyone deceased without documented pre-death permission.
3. **Plan only.** The voice reads what the person wrote. It never generates new sentences.
4. **Disclosure first, spoken, in every render:** "This is a synthetic copy of <name>'s voice, made with permission."
5. **Family folder, deletable.** One command removes sample, provider clone and every render.

## Pipeline

1. Sample: 10 to 30 seconds of clean speech, `shared/plan/voice/sample.wav`.
2. TTS with their cloned voice:

   - New families: Fish Audio S2, about $15/M UTF-8 bytes (a full plan is about 2 cents), clone from 10 seconds.
   - This house: MiniMax clone, `moss_audio_23686446-66a2-11f0-b6f8-daebc56235b9` for Brendan.
   - POST `https://api.minimax.io/v1/t2a_v2`, `speech-2.8-hd`, `vol: 4`, speed 0.92. The response audio is **hex**: `bytes.fromhex()`.
   - Offline-only families: NeuTTS Air on laptop CPU, no account.

3. Split the plan at chapter headings: one MP3 per chapter plus one complete file. Prepend the disclosure line to the complete file and to each chapter.
4. Normalise with `ffmpeg -af loudnorm=I=-16:TP=-1.5:LRA=11`.
5. Write `shared/plan/voice/manifest.md`: consent, sample hash, provider, voice id, dates, file list, deletion steps.

## When it goes wrong

- Thin or robotic: speed 0.9 to 0.92, never faster. Re-record the sample somewhere quiet before blaming the provider.
- Clipped peaks: always loudnorm to -16 LUFS / -1.5 dBTP.
- Pronoun trouble on names: add phonetic spellings to the script for the render, never to the saved plan.

## Do not

- Do not build avatar or lip-sync versions. Parked deliberately (see `docs/voice-echo.md`).
- Do not store the sample or voice id in anything that syncs outside the family folder.
