---
name: voice-echo
description: "Use when a family wants the plan spoken in their own voice."
version: 1.0.0
---

# Voice echo

The plan, read aloud in the person's own cloned voice, optionally with a talking portrait. Verified working, October 2026.

## The rails come first

1. **Consent recorded before anything else.** The person reads the consent line on the recording, or signs the paper version which gets photographed into `shared/plan/voice/consent.jpg`. Template: `shared/consent-template.md`. No consent file, no clone, no render. Ever.
2. **Scope is the plan, nothing wider.** Default: "my voice may read my plan back to my family." Any other use needs its own yes, in writing.
3. **Every file opens with the disclosure card.** Four seconds, silent, plain text: synthetic voice, made with permission, whose copy it is. No exceptions, including private demos.
4. **Their own voice only.** Never clone a spouse, a parent, or anyone deceased without documented pre-death permission.
5. **Plan-only.** The clone reads what the person wrote. New sentences in the voice of someone who has died is impersonation, not memory.
6. **Family folder, deletable.** One command removes sample, provider clone and every render. Document it in the manifest.

## The working pipeline (verified end to end)

1. **Portrait**: a clear front-facing photo, stored as `portrait.jpg` in `shared/plan/voice/`.
2. **Script**: the person's own words from the plan, split into parts of **15 seconds or less** (the avatar provider caps each clip at 15s). Write the parts at sentence boundaries.
3. **Voice**: TTS with the person's cloned voice.

   - This house: MiniMax clone, `voice_id` from the profile (Brendan's own: `moss_audio_23686446-66a2-11f0-b6f8-daebc56235b9`).
   - POST `https://api.minimax.io/v1/t2a_v2`, model `speech-2.8-hd`, `vol: 4` (5+ clips), speed 0.92.
   - Response audio is **hex**, decode with `bytes.fromhex()`.
   - Normalise: `ffmpeg -af loudnorm=I=-16:TP=-1.5:LRA=11`.
   - New families: Fish Audio S2 (about $15/M bytes, clone from 10s). Never ElevenLabs unless the family asks.

4. **Talking portrait**: Higgsfield Speak.

   - Header: `Authorization: Key <HIGGSFIELD_API_KEY>`.
   - Upload files: POST `https://api.higgsfield.ai/files/generate-upload-url` `{"content_type": "image/jpeg" | "audio/wav"}`, PUT the bytes to `upload_url` with the returned headers, keep `public_url`.
   - Submit: POST `https://api.higgsfield.ai/v1/speak/higgsfield` with `{"params": {"input_image": {"type": "image_url", "image_url": ...}, "input_audio": {"type": "audio_url", "audio_url": ...}, "prompt": "...", "quality": "mid", "duration": 15}}`.
   - **Audio must be WAV** (convert with ffmpeg, mono 44.1k) and **duration is 5, 10 or 15** (integer), not a string.
   - Poll `GET /requests/<id>/status` until `completed`; the video URL is under `jobs[].results.raw.url` (or `video.url`).

5. **Assemble**: ffmpeg concat, disclosure card first:

   ```bash
   ffmpeg -f lavfi -i "color=c=0x1f1a16:s=1280x720:d=4:r=25" -vf "drawtext=..." card.mp4
   ffmpeg -f concat -safe 0 -i concat.txt -c:v libx264 -pix_fmt yuv420p -c:a aac plan-avatar.mp4
   ```

6. **Manifest**: `shared/plan/voice/manifest.md` records consent, script, voice id, provider jobs, dates, file hashes, and the deletion steps.

## Costs (Oct 2026)

- Voice: about 2 cents per 2,000-word plan on Fish; MiniMax HD $100/M chars.
- Avatar: Higgsfield Speak per 15s clip (mid quality); Kling Avatar V2 ($0.035-0.056/s) and OmniHuman ($0.12-0.16/s) are alternatives for longer or more realistic renders.
- Runway: the public API has **no /lip_sync endpoint** (verified 404). Act-Two needs a performance video, so it is the wrong tool for photo + audio. Use Higgsfield, Kling or OmniHuman.

## When it goes wrong

- Speak rejects the audio: check WAV, under 15s, mono.
- Facial distortion: the portrait needs a clear front-facing face, no heavy angles or sunglasses.
- Robot look: slow the speech 0.9x in TTS before rendering; never speed it up.
