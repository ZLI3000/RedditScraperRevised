
from moviepy.editor import *
clip = VideoFileClip("darkvideo.mp4")
audio = AudioFileClip("output.wav")
'''Set the audio for the clip'''
clip = clip.set_audio(audio)
'''Loop the clip until the end of the video'''
loopedClip = clip.loop(duration=audio.duration)

loopedClip.write_videofile(
    "output.mp4",
    preset='ultrafast',
    audio=True)

