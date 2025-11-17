# Piano Transcription RunPod Serverless

Convert piano audio → MIDI using the `piano_transcription_inference` package.

## Input Format

POST to RunPod Endpoint:
{
"input": {
"audio_base64": "<base64_wav/mp3>"
}
}

shell
Copy code

## Output Format
{
"midi_base64": "<base64_midi>"
}

markdown
Copy code

## Notes
- Runs on GPU (`cuda`) inside RunPod Serverless.
- Charged per second per inference.
