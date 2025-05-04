#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

import whisper
from utils.audio_tools import load_audio


def transcribe(input_path: Path, output_path: Path):
    """
    Simple transcribe function using default model 'base' on CPU.
    """
    model = whisper.load_model("base", device="cpu", download_root="models")
    transcribe_with_model(model, "cpu", input_path, output_path)


def transcribe_with_model(model, device, input_path: Path, output_path: Path):
    """
    Transcribes a single audio file using a pre-loaded Whisper model.
    """
    # Load and preprocess audio
    audio = load_audio(input_path)
    print(f"🔄 Transcribing {input_path.name} on {device}…")
    # Perform transcription
    result = model.transcribe(audio, language="hu")
    # Save JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved: {output_path}\n")


def generate_runs(inputs, models, output_args):
    runs = []
    total = len(inputs) * len(models)
    if len(output_args) == total:
        outs = [Path(p) for p in output_args]
        i = 0
        for inp in inputs:
            for m in models:
                runs.append((inp, m, outs[i]))
                i += 1
    elif len(output_args) == 1:
        base = Path(output_args[0])
        stem = base.stem
        suffix = base.suffix or ".json"
        directory = base.parent
        for inp in inputs:
            for m in models:
                name = f"{stem}_{m}{suffix}"
                runs.append((inp, m, directory / name))
    else:
        raise ValueError(
            f"Provide either {total} outputs (one per input/model) or a single base output path"
        )
    return runs


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe Hungarian speech to JSON outputs (supports multiple models)"
    )
    parser.add_argument(
        "-i", "--input", nargs='+', required=True,
        help="Input audio file(s)"
    )
    parser.add_argument(
        "-m", "--model", nargs='+', required=False,
        choices=["tiny","base","small","medium","large"],
        default=["base"],
        help="Whisper model(s) to use (default: 'base')"
    )
    parser.add_argument(
        "-o", "--output", nargs='+', required=True,
        help="Output JSON file path(s), either one base or one per run"
    )
    parser.add_argument(
        "-d", "--device", choices=["cpu","cuda"], default="cpu",
        help="Device to run on (default: cpu)"
    )
    args = parser.parse_args()

    inputs = [Path(p) for p in args.input]
    models = args.model if isinstance(args.model, list) else [args.model]
    device = args.device

    try:
        runs_conf = generate_runs(inputs, models, args.output)
    except ValueError as e:
        parser.error(str(e))

    # Load each model once
    loaded = {m: whisper.load_model(m, device=device, download_root="models") for m in models}

    # Process each combination
    for inp_path, m_name, out_path in runs_conf:
        if not inp_path.is_file():
            parser.error(f"Input file does not exist: {inp_path}")
        transcribe_with_model(loaded[m_name], device, inp_path, out_path)


if __name__ == "__main__":
    main()
# This script is designed to transcribe Hungarian speech using the Whisper model.
# It includes command-line arguments for input/output file paths, model selection, and device choice.

