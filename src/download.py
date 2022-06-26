from pytube import YouTube, Playlist
from src.utils import Welcome


def Videos(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path='./downloads/videos')


def Playlists(urls):
    while True:
        Welcome()
        option = str(
            input(
                'Baixar playlist em formato de vídeo ou apenas áudio?\n[y] - Vídeos\n[n] - Áudio\n-->> '
            )).lower().strip()

        if (option in 'yn') and (len(option) == 1):
            playlist = Playlist(urls)
            title = playlist.title

            if option == 'y':
                for url in playlist:
                    yt = YouTube(url)
                    video = yt.streams.get_highest_resolution()
                    video.download(output_path=f'./downloads/{title}')

            elif option == 'n':
                for url in playlist:
                    yt = YouTube(url)
                    video = yt.streams.filter(only_audio=True)[0]
                    video.download(output_path=f'./downloads/{title}')

            break
        else:
            continue


def Songs(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download(output_path='./downloads/music')