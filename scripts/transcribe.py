#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

import whisper
from utils.audio_tools import load_audio

def transcribe(input_path: Path, output_path: Path):
    # Load audio array (supports WAV, MP3, etc., with FFmpeg conversion)
    audio = load_audio(input_path)
    # Load Whisper model
    model = whisper.load_model("base", download_root="models")
    # Perform transcription (Hungarian)
    result = model.transcribe(audio, language="hu")
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write JSON output
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"✅ Transcription saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Transcribe Hungarian speech to JSON, with FFmpeg conversion")
    parser.add_argument("-i", "--input", required=True, help="Input audio file (wav, mp3, etc.)")
    parser.add_argument("-o", "--output", required=True, help="Output JSON file path")
    args = parser.parse_args()

    inp = Path(args.input)
    outp = Path(args.output)
    if not inp.is_file():
        parser.error(f"Input file does not exist: {inp}")

    transcribe(inp, outp)

if __name__ == "__main__":
    main()
