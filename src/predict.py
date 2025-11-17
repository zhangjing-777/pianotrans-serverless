from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import tempfile
import os

# 全局变量，只加载一次模型
_transcriptor = None

def get_transcriptor():
    """获取或创建转录器实例（单例模式）"""
    global _transcriptor
    if _transcriptor is None:
        print("Loading piano transcription model...")
        _transcriptor = PianoTranscription(device='cuda', checkpoint_path=None)
        print("Model loaded successfully!")
    return _transcriptor

def transcribe_piano(audio_path: str):
    """
    Load audio → run piano transcription → save MIDI
    """
    print(f"Loading audio from {audio_path}")
    
    # Load audio
    audio, sr = load_audio(audio_path, sr=sample_rate, mono=True)
    
    print(f"Audio loaded: {len(audio)} samples at {sr}Hz")
    
    # Get transcriptor (reuse if already loaded)
    transcriptor = get_transcriptor()

    # Output MIDI path
    temp_midi = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
    out_midi_path = temp_midi.name
    temp_midi.close()  # 关闭文件句柄，让 transcribe 可以写入

    # Run inference
    print("Running transcription...")
    transcriptor.transcribe(audio, out_midi_path)
    print(f"Transcription complete, saved to {out_midi_path}")

    return out_midi_path
