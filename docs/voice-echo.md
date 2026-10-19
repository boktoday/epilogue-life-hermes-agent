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


## Getting a family set up

The agent walks them through this in order, in plain words, no jargon:

1. **Offer the best route first: they read it themselves.** If the person is well enough to record, a phone recording of them reading their own plan beats any clone: no cloud, no cost, perfect fidelity. The clone exists for when reading the whole plan is too much, or for after their voice is gone.
2. **Then the hosted clone**, if they still want it: 10 to 30 seconds of speech, recorded in the app, consent line first.
3. **Or the offline clone** for families who refuse the cloud: NeuTTS Air on their own laptop, free, nothing leaves the house.

### What the cloud really means

Say it plainly, because families deserve the truth and not a euphemism:

> **The cloud is someone else's computer.** A machine in a company's data centre, in a specific country, reached over the internet. When we clone a voice through a provider, four things travel there: the sample recording, the words being read, the voice model they build from it, and the audio they send back.

What happens to the sample until it is deleted:

- **Upload.** The recording leaves the device and lands on the provider's storage. From that moment, it is their copy, held under their terms.
- **The clone.** Their systems build a voice profile from it. Many providers keep the original sample for identity checks and abuse monitoring, some keep it indefinitely unless asked to delete it.
- **Who can reach it.** Provider staff and contractors under their policies; automated abuse scanning; law enforcement with the right paperwork; a security breach, which is rare and has happened to every large provider at some point. If the provider is overseas, foreign law applies, not Australian law.
- **Rendering.** Every render also sends the plan's text to the provider to be spoken. The plan contains medical wishes, family names, private instructions. That text is processed on their servers too.
- **Deleting.** An API delete removes the active voice model and the stored files. Backups expire on the provider's schedule, not instantly. Deletion is a request, not a shredder. What we can give the family is our own written record: what was deleted, when, and the provider's response, kept in their manifest.
- **What cannot be undone.** Once a voice model has existed, no one can promise every copy is gone. That is exactly why consent, disclosure and the family's folder matter more than any technical measure.

If any of that is unacceptable to the family, the answer is simple and we should say it without hesitation: use the local route, or record themselves. Never talk them into the cloud because it is cheaper and easier.
