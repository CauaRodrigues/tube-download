from pytube import YouTube, Playlist
from src.utils import Clear, Welcome

import os
from moviepy.editor import *
import time

from pydub import AudioSegment
from pydub.playback import play


def Videos(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path='./downloads/videos')
    print(f'Download de "{yt.title}" completo!')


def Playlists(urls):
    while True:
        Welcome()
        option = str(
            input(
                'Baixar playlist em formato de vídeo ou apenas áudio?\n[y] - Vídeos\n[n] - Áudio\n-->> '
            )).lower().strip()

        print('\n')

        if (option in 'yn') and (len(option) == 1):
            playlist = Playlist(urls)

            optionNamePlaylist = str(
                input('Definir nome para a playlist? [y/n]\n-->> ')).lower(
                ).strip()
            if optionNamePlaylist == 'y':
                title = str(input('Nome da playlist: '))
            else:
                title = playlist.title

            if option == 'y':
                for url in playlist:
                    yt = YouTube(url)
                    video = yt.streams.get_highest_resolution()
                    video.download(output_path=f'./downloads/videos/{title}')
                print(
                    f'Playlist "{title}" salva em ./downloads/videos/{title}')
            elif option == 'n':
                for url in playlist:
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True)[0]
                    video.download(output_path=f'./downloads/music/{title}')
                print(f'Playlist "{title}" salva em ./downloads/music/{title}')

            break
        else:
            continue


def Songs(url):
    print('Buscando...')
    time.sleep(3.2)
    yt = YouTube(url)
    audio = yt.streams.get_highest_resolution()
    audio.download(output_path='./downloads/music')

    Welcome()
    print('Convertendo arquivo...\n')
    time.sleep(3.3)
    mp4_file = VideoFileClip(os.path.join(f'./downloads/music/{yt.title}.mp4'))
    mp4_file.audio.write_audiofile(
        os.path.join(f'./downloads/music/{yt.title}.mp3'))

    Welcome()
    print(f'Download de "{yt.title}" completo!\n')

    option = str(input('Deseja reproduzir a música? [y/n]')).lower().strip()

    if option == 'y':
        print(f'Reproduzindo {yt.title}...')
        song = AudioSegment.from_mp3(
            os.path.join(f'./downloads/music/{yt.title}.mp3'))
        play(song)
    else:
        pass