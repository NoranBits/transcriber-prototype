# utils/audio_tools.py

"""Utility functions for audio preprocessing using FFmpeg + torchaudio."""

import sys
import numpy as np
import torchaudio
import ffmpeg
from pathlib import Path
from tempfile import NamedTemporaryFile

def _find_ffmpeg_executable() -> str:
    """
    Először megpróbálja használni a venv/Scripts/ffmpeg.exe-t,
    ha ott van, különben a PATH-beli 'ffmpeg'-et.
    """
    # sys.executable → .../venv/Scripts/python.exe
    exe_path = Path(sys.executable).parent
    ffmpeg_venv = exe_path / "ffmpeg.exe"
    if ffmpeg_venv.is_file():
        return str(ffmpeg_venv)
    return "ffmpeg"

def convert_to_wav(input_path: Path, output_path: Path, sr: int = 16000):
    """
    Convert any audio file (mp3, wav, etc.) to a mono WAV with target sample rate.
    Magába foglalja azt az ffmpeg.exe-t, ami a venv/Scripts alatt lehet.
    """
    ffmpeg_cmd = _find_ffmpeg_executable()
    (
        ffmpeg
        .input(str(input_path))
        .output(str(output_path),
                format="wav",
                acodec="pcm_s16le",
                ac=1,
                ar=str(sr))
        .overwrite_output()
        .run(cmd=ffmpeg_cmd, quiet=True)
    )

def load_audio(input_path: Path, sr: int = 16000) -> np.ndarray:
    """
    Load audio file into numpy array, converting first to WAV if needed.
    """
    # Ha nem .wav, akkor konvertálunk
    if input_path.suffix.lower() != ".wav":
        tmp = NamedTemporaryFile(suffix=".wav", delete=False)
        tmp_path = Path(tmp.name)
        tmp.close()
        convert_to_wav(input_path, tmp_path, sr=sr)
        wav_path = tmp_path
    else:
        wav_path = input_path

    # Betöltés torchaudio-val
    waveform, sample_rate = torchaudio.load(str(wav_path))

    # Mono
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    # Resample
    if sample_rate != sr:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=sr)
        waveform = resampler(waveform)

    # Tisztítás: ha ideiglenes volt, töröljük
    if wav_path != input_path:
        try:
            wav_path.unlink()
        except OSError:
            pass

    return waveform.squeeze(0).numpy().astype(np.float32)
