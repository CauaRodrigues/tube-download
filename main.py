from pytube import YouTube, Playlist

print('''
  ______      __            ____                      __                __
 /_  __/_  __/ /_  ___     / __ \____ _      ______  / /___  ____ _____/ /
  / / / / / / __ \/ _ \   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / 
 / / / /_/ / /_/ /  __/  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  
/_/  \__,_/_.___/\___/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/                           
      
      ''')

VIDEO_URL = input('Informe a url do video:\n--> ')
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLyORnIW1xT6waC0PNjAMj33FdK2ngL_ik'


def download_video(video_url):
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download()


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path='./downloads/playlist')


def download_audio(video_url):
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()


if __name__ == '__main__':
    download_playlist(PLAYLIST_URL)

# for stream in yt.streams:
#     print(stream)