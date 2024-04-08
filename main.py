import torch
import torchaudio
# from TTS.tts.configs.tortoise_config import TortoiseConfig
# from TTS.tts.models.tortoise import Tortoise
from TTS.api import TTS
from pathlib import Path
import praw

reddit = praw.Reddit(
    client_id='fXy-16VprltamlV0kpEuDQ',
    client_secret='_tXlzrPE-34k5AvsxWXX42wasLVS0g',
    user_agent='linux:com.nosleepscraper:0.1 (by /u/Middle_Reputation310)',
)

subreddit = reddit.subreddit("nosleep")  # grabs subreddit ID and attaches var
hot_submissions = subreddit.hot(limit=5)  # creates variable for hot submissions
for submission in hot_submissions:  # grabbing hot submissions
    with open("nosleep.txt", "w") as ns:  # opens nosleep.txt in write mode ns is the nosleep file path
        print(submission.selftext,
              file=ns)  # self text grabs the submissions text and the print is forwarded to a txt file

device = "cuda" if torch.cuda.is_available() else "cpu"  # specifies to use CUDA cores
# config = TortoiseConfig()  # uses tortoise config
# model = Tortoise.init_from_config(config)  # initializes model from tortoise config
# modelPath = Path('/home/egg/PycharmProjects/RedditScraperRevised/.venv/lib/python3.11/site-packages/tortoise/models/')
# voicePath = Path(
#     "/home/egg/PycharmProjects/RedditScraperRevised/.venv/lib/python3.11/site-packages/tortoise/voices/")
speakerPath = Path(
    "/home/egg/PycharmProjects/RedditScraperRevised/.venv/lib/python3.11/site-packages/tortoise/voices/geralt/3.wav")
# model.load_checkpoint(config,
#                       checkpoint_dir=modelPath,
#                       eval=True)
# finds path to use models
# tts = TTS("tts_models/en/multi-dataset/tortoise-v2")  # sets variable tts to use tortoise models specified in
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

with open("nosleep.txt", "r") as ns:
    text = ns.read()

tts.tts_to_file(text=text,
                file_path="output.wav",
                speaker_wav=speakerPath,
                language='en')
