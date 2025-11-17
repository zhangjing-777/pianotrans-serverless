import runpod
import base64
import tempfile
from predict import transcribe_piano

def handler(event):
    """
    RunPod Serverless Entry
    Expected input:
    {
        "input": {
            "audio_base64": "<base64 audio>"
        }
    }
    """
    try:
        audio_b64 = event["input"]["audio_base64"]
        audio_bytes = base64.b64decode(audio_b64)

        # Save uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio_bytes)
            audio_path = f.name

        midi_path = transcribe_piano(audio_path)

        # Convert MIDI to base64
        with open(midi_path, "rb") as f:
            midi_b64 = base64.b64encode(f.read()).decode()

        return {"midi_base64": midi_b64}
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
