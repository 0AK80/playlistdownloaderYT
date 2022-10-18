from pytube import Playlist

# AK8

playlist_url = 'https://www.youtube.com/playlist?list='
playlist = Playlist(playlist_url)


print(len(playlist.video_urls))

# Muestra la  url de los primeros 4 videos de la playlist
for video in playlist.video_urls[:4]:
    print(video)


for video in playlist.videos:
    video.streams.get_audio_only().download()


print('Download Finished')
