from tortoise import api
from tortoise import utils
clips_paths = '/home/egg/tortoise-tts/tortoise/voices/deniro/1.wav'

reference_clips = [utils.audio.load_audio('/home/egg/tortoise-tts/tortoise/voices/deniro/1.wav', 22050) for p in clips_paths]
tts = api.TextToSpeech(use_deepspeed=True, kv_cache=True, half=True)
pcm_audio = tts.tts_with_preset("your text here", voice_samples=reference_clips, preset='fast')
