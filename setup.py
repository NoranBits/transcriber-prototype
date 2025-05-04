# setup.py
from setuptools import setup, find_packages

setup(
    name="transcriber_prototype",
    version="0.1.2",
    packages=find_packages(where="."),
    install_requires=[
        "ffmpeg-python==0.2.0",                                             # :contentReference[oaicite:0]{index=0}
        "numpy==2.2.5",                                                      # :contentReference[oaicite:1]{index=1}
        "torch==2.7.0",                                                      # :contentReference[oaicite:2]{index=2}
        "torchaudio==2.7.0",                                                 # :contentReference[oaicite:3]{index=3}
        "openai-whisper @ git+https://github.com/openai/whisper.git@main",    # :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}
        "noisereduce==3.0.3",                                                # :contentReference[oaicite:6]{index=6}
        "soundfile==0.13.1"                                                  # :contentReference[oaicite:7]{index=7}
    ],
    python_requires=">=3.13",
)
# This setup script is designed to package the transcriber prototype as a Python module.