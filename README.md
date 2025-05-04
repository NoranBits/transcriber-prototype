# Transcriber Prototype with FFmpeg Support

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)]  
[![PyTorch 2.7.0](https://img.shields.io/badge/torch-2.7.0-orange)]  
[![FFmpeg Python 0.2.0](https://img.shields.io/badge/ffmpeg--python-0.2.0-lightgrey)]  

---

## Overview

This CLI application transcribes Hungarian speech from any audio format (WAV, MP3, etc.) into JSON, using FFmpeg for conversion and Whisper for transcription.

## Features

- 🔊 Converts input to WAV (16 kHz, mono) via FFmpeg  
- 🗣️ Transcribes with OpenAI Whisper  
- 🎧 Supports MP3, WAV, and more  
- 📂 Outputs JSON with timestamps  

## Structure

```
transcriber-prototype/
├── scripts/
│   ├── __init__.py
│   └── transcribe.py
├── utils/
│   ├── __init__.py
│   └── audio_tools.py
├── tests/
│   └── test_transcribe.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

```bash
git clone https://github.com/<user>/transcriber-prototype.git
cd transcriber-prototype
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

```bash
python scripts/transcribe.py -i audio/input.mp3 -o output/output.json
```

## License

MIT
