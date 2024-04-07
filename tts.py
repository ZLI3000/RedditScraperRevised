import torch
from main import ns
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

with open("nosleep.txt", "r") as ns:  # Run TTS
    text = ns.read()
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech to a file
tts.tts_to_file(text=text, speaker_wav="/home/egg/PycharmProjects/RedditScraperRevised/.venv/lib/python3.11/site-packages/TTS/voices/emma/1.wav", language="en", file_path="output.wav")

