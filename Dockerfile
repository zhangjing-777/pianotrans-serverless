FROM runpod/serverless:gpu-cuda12.1-ffmpeg

RUN pip install piano_transcription_inference librosa soundfile numpy

WORKDIR /app
COPY handler.py .
COPY predict.py .

CMD ["python3", "handler.py"]
