FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user PATH=/home/user/.local/bin:$PATH DEEPFACE_HOME=/home/user PORT=7860
WORKDIR /home/user/app

COPY --chown=user requirements-deploy.txt .
RUN pip install --no-cache-dir --user -r requirements-deploy.txt

COPY --chown=user . .
# Download the emotion model at build time so the first request is fast
RUN python -c "from deepface import DeepFace; DeepFace.build_model(task='facial_attribute', model_name='Emotion')" || true

EXPOSE 7860
CMD ["python", "main.py"]
