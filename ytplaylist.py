from pytube import Playlist

# AK8

playlist_url = input()
playlist = Playlist(playlist_url)


print(len(playlist.video_urls))


for video in playlist.videos:
    
    video.streams.get_audio_only().download()


print('--------All downloads have finished--------')
