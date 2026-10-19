# Voice echo: the plan read aloud, in their own voice

The feature: the person writes their plan, and Epilogue renders it as spoken word in a synthetic copy of their own voice, so their family can hear it in the voice they know. Voice only. No avatar.

## Why voice only

A talking portrait was built and tested on 19 October 2026 (Higgsfield Speak, five clips, disclosed). It worked, and it was wrong: uncanny, fiddly, expensive per minute, and it turned a human document into a novelty. The spoken word version is simpler, warmer and cheaper by two orders of magnitude. The portrait route is parked, documented at the end.

## Providers (checked October 2026)

| Route | Cost | Notes |
|---|---|---|
| **Fish Audio S2** | about $15 per million UTF-8 bytes; a 2,000-word plan is about 12KB, so about 2 cents | Default for new families. Clone from 10 seconds, 80+ languages, #1 TTS-Arena at launch, free tier includes cloning |
| **MiniMax Speech 2.8** | $60/M Turbo, $100/M HD; $1.50 per voice clone | The house default: Brendan's own clone is already on this account. China-hosted, so flag data residency to families |
| **NeuTTS Air** | free, laptop CPU, no account | The offline path for families who refuse any cloud. Small quality trade |
| **Chatterbox (MIT)** | free, wants a small GPU | Better quality than NeuTTS, needs hardware |
| **ElevenLabs** | about $165 per million characters | Only when the family asks, or needs 30+ minutes of training audio for a pro clone |

## The pipeline

1. **Consent, on record.** Spoken or written, filed in `shared/plan/voice/consent.md`. Template: `shared/consent-template.md`. No consent file, no clone, no render.
2. **Sample.** Ten to thirty seconds of clean speech, saved as `shared/plan/voice/sample.wav`. Their own voice only.
3. **Clone.** Fish (new families) or MiniMax (this house). Store the voice id in the manifest, never the sample, in the app config.
4. **Script.** The plan is split into chapters at heading boundaries. Plain text, their words, no rewriting.
5. **Render.** One file per chapter, plus one complete file. Every render opens with the disclosure line, spoken first:
   > "This is a synthetic copy of <name>'s voice, made with permission."
6. **Normalise.** `ffmpeg -af loudnorm=I=-16:TP=-1.5:LRA=11` to MP3 128k or AAC.
7. **Manifest.** `shared/plan/voice/manifest.md`: consent, sample hash, provider, voice id, dates, file list.

## Costs in practice

A 2,000-word plan is about 12 minutes of speech. Fish: about 2 cents. MiniMax HD: well under a dollar. Either way the family pays once and owns the files.

## Rails

- Recorded consent, every time, before anything.
- Their own voice only. Never a spouse, a parent, or anyone deceased without documented pre-death permission.
- The voice reads what they wrote. It never generates new sentences. A clone that invents words is impersonation, not memory.
- Every render opens with the disclosure line.
- Files live in the family's own folder. Deletion is one command: remove the sample, the provider clone and every rendered file, then note it in the manifest.

## Parked: talking portrait

Tested 19 Oct 2026: portrait photo plus cloned audio through Higgsfield Speak (15-second clips, hard cut past 15s, video-only output needing a per-clip audio mux), assembled with a disclosure card. Verdict: parked by the owner as too uncanny and too much machinery for a funeral-adjacent product. Runway's public API has no lip-sync endpoint (404, verified). Kling Avatar V2 and OmniHuman remain the routes if this ever returns. The demo video and skill remain in git history.
