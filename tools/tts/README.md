# TTS tools

## Kokoro smoke test

This optional utility generates **audition clips only**. It does not select a voice, clear a license, create subtitles, or authorize production audio.

```bash
python3 tools/tts/kokoro_smoke_test.py \
  --text-file content/long/GENESIS-001/TTS_LONG_SAMPLE_v01.txt \
  --output-dir audio/GENESIS-001/voice-test/kokoro \
  --voices pm_alex pm_santa \
  --speed 0.95
```

Run it in an isolated runtime containing `kokoro` and `soundfile`; the repository deliberately has no heavyweight ML dependency lockfile. The official model source, model/voice hash, package versions, attribution and license evidence must be logged in the content package before any output may be used in the final video.

If the model cannot be downloaded, record the failure and retry only on a network-enabled production machine or with a verified offline artifact. Do not substitute a random mirror or untracked model file.
