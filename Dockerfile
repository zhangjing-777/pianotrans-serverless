FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# System deps
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip3 install --upgrade pip
RUN pip3 install \
    torch==2.1.0+cu121 \
    torchvision==0.16.0+cu121 \
    torchaudio==2.1.0+cu121 \
    --index-url https://download.pytorch.org/whl/cu121

RUN pip3 install piano_transcription_inference librosa soundfile numpy

# Copy code
WORKDIR /app
COPY handler.py .
COPY predict.py .

# RunPod Serverless expects uvicorn-compatible handler
CMD ["python3", "handler.py"]
