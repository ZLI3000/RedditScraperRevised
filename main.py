import torch
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
speakerPath = Path(
    "/home/egg/PycharmProjects/RedditScraperRevised/.venv/lib/python3.11/site-packages/tortoise/voices/geralt/3.wav")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

with open("nosleep.txt", "r") as ns:
    text = ns.read()

tts.tts_to_file(text=text,
                file_path="nosleepaudio.wav",
                speaker_wav=speakerPath,
                language='en')

