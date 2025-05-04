import sys
import json
from pathlib import Path
import subprocess
import pytest
import numpy as np

def test_import_transcribe():
    import scripts.transcribe  # should import without errors

def test_help_output():
    result = subprocess.run(
        [sys.executable, "scripts/transcribe.py", "--help"],
        capture_output=True, text=True
    )
    assert "Transcribe Hungarian speech" in result.stdout

class DummyModel:
    def transcribe(self, audio, language):
        return {"text": "dummy", "segments": [], "language": language}

@pytest.fixture(autouse=True)
def patch_deps(monkeypatch):
    import whisper
    import utils.audio_tools as atools
    monkeypatch.setattr(whisper, "load_model", lambda *args, **kwargs: DummyModel())
    # Stub load_audio to avoid actual file operations
    monkeypatch.setattr(atools, "load_audio", lambda input_path, sr=16000: np.zeros(sr, dtype=np.float32))

def test_transcribe_functionality(tmp_path):
    input_audio = tmp_path / "input.mp3"
    input_audio.write_bytes(b"")  # dummy content
    output_json = tmp_path / "output.json"
    from scripts.transcribe import transcribe
    transcribe(input_audio, output_json)
    assert output_json.is_file()
    data = json.loads(output_json.read_text(encoding="utf-8"))
    assert data["text"] == "dummy"
    assert data["language"] == "hu"
