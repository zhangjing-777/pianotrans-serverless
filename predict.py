from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import tempfile

def transcribe_piano(audio_path: str):
    """
    Load audio → run piano transcription → save MIDI
    """
    # Load audio
    audio, sr = load_audio(audio_path, sr=sample_rate, mono=True)

    # Load transcriptor
    transcriptor = PianoTranscription(device='cuda')

    # Output MIDI path
    temp_midi = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
    out_midi_path = temp_midi.name

    # Run inference
    transcriptor.transcribe(audio, out_midi_path)

    return out_midi_path
