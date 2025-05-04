# Transcriber Prototype

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3130/)  
[![PyTorch 2.7.0](https://img.shields.io/badge/torch-2.7.0-orange)](https://pytorch.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Tartalomjegyzék

- [Leírás](#leírás)  
- [Főbb funkciók](#főbb-funkciók)  
- [Projekt struktúra](#projekt-struktúra)  
- [Telepítés](#telepítés)  
- [Használat](#használat)  
- [JSON kimenet](#json-kimenet)  
- [További tervek](#további-tervek)  
- [Hozzájárulás](#hozzájárulás)  
- [Licenc](#licenc)

---

## Leírás

Ez a prototípus egy egyszerű CLI (parancssori) alkalmazás, amely magyar nyelvű `.wav` hangfájlokból automatikusan szöveges átiratot készít az OpenAI Whisper modellen keresztül. A kimenetet `output/output.json` formátumban menti, hogy könnyen integrálható legyen további backend vagy frontend rendszerekbe.

---

## Főbb funkciók

- 🗣️ Magyar nyelvű beszédfelismerés Whisper (openai-whisper vagy whisper.cpp) segítségével  
- 🔄 Egyszerű bemenet (`audio/input.wav`) és kimenet (`output/output.json`)  
- ⚙️ Parancssorból futtatható, GUI nélkül  
- 📂 Előre elkészített mappa- és fájlstruktúra későbbi bővítésekhez  
- 🚀 Gyors indítás helyi környezetben, internetkapcsolat nélkül

---

## Projekt struktúra

```
transcriber-prototype/
├── audio/                 # Bemeneti WAV fájl(ok)
│   └── input.wav
├── output/                # Kimeneti JSON fájl(ok)
│   └── output.json
├── models/                # Letöltött Whisper-modellek cache
├── scripts/               # Futtatható script(ek)
│   └── transcribe.py
├── utils/                 # Segédfüggvények (pl. zajszűrés, normalizálás)
│   └── audio_tools.py
├── requirements.txt       # Python-csomagok listája
└── README.md              # Ez a fájl
```

---

## Telepítés

1. **Kód klónozása**

   ```bash
   git clone https://github.com/<felhasználó>/transcriber-prototype.git
   cd transcriber-prototype
   ```

2. **Virtuális környezet létrehozása és aktiválása**

   ```bash
   python -m venv venv
   ```

   - **Windows**  
     ```cmd
     venv\Scripts\activate
     ```
   - **macOS/Linux**  
     ```bash
     source venv/bin/activate
     ```

3. **Függőségek telepítése**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **FFmpeg telepítése**  
   Győződj meg róla, hogy a rendszereden elérhető a `ffmpeg` parancs (pl. `ffmpeg -version`).

---

## Használat

1. Másold vagy helyezd be a feldolgozandó `.wav` fájlt az `audio/input.wav` útvonalra.  
2. Futtasd a transzkripciós scriptet:

   ```bash
   python scripts/transcribe.py
   ```

3. A JSON kimenetet az `output/output.json` fájlban találod.

---

## JSON kimenet

```json
{
  "text": "Ez itt egy példa átirat magyar nyelven.",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 5.0,
      "text": "Ez itt egy példa átirat",
      "tokens": [50364, 1435, 417, ...],
      "temperature": 0.0,
      "avg_logprob": -0.12345,
      "compression_ratio": 1.0,
      "no_speech_prob": 0.01
    }
  ],
  "language": "hu"
}
```

- **text**: teljes átirat  
- **segments**: időbélyegzett részek, statisztikákkal  
- **language**: felismert nyelv (`hu` = magyar)

---

## További tervek

- 🔊 Zajszűrés integrálása (ffmpeg / noisereduce)  
- 🗣️ Speaker diarization (pyannote-audio vagy Whisper beépített)  
- 🌐 FastAPI backend és WebSocket valós idejű szolgáltatás  
- 🔄 Több hangforrás szinkronizálása és kezelése

---

## Hozzájárulás

1. Forkold ezt a repót  
2. Hozz létre feature branch-et (`git checkout -b feature/uj-funkcio`)  
3. Commit-old a változtatásaid (`git commit -am 'Új funkció hozzáadva'`)  
4. Push-olj (`git push origin feature/uj-funkcio`)  
5. Nyiss egy Pull Request-et

---

## Licenc

Ez a projekt **MIT Licence** alatt érhető el. Részletek a [LICENSE](LICENSE) fájlban.
