# need run two commands
# $ sudo apt-get install ffmpeg libavcodec-extra
# $ pip3 install pydub
# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_mp3('./downloads/music/GHOSTEMANE.mp3')
# play(song)
import os
from moviepy.editor import *

video = VideoFileClip(
    os.path.join(
        "./downloads/music/Fitz And The Tantrums - The Walker [LegendadoTradução].mp4"
    ))
video.audio.write_audiofile(
    os.path.join(
        "./downloads/music/Fitz And The Tantrums - The Walker [LegendadoTradução].mp3"
    ))
