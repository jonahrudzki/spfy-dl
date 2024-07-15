import requests
from pathlib import Path
import os

from models.track import Track
from models.playlist import Playlist

from util import ytmusic
from yt_dlp import YoutubeDL

# define the base output path
BASE_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'output')


def get_urls(playlist: Playlist):
    
    # ytmusicapi call to get top song search request yt video id
    for track in playlist.get_tracks():
        v_id = ytmusic.get_song_link(track.get_track_name(), track.get_artist_name())
        url = f'https://www.youtube.com/watch?v={v_id}'
        
        track.set_url(url)
        
def download_tracks(playlist: Playlist):
    # create the download directory for the playlist
    playlist_name = playlist.get_name()
    download_path = os.path.join(BASE_OUTPUT_PATH, playlist_name) # path in individual playlist folder
    os.makedirs(download_path, exist_ok=True)
    
    # save all video urls
    get_urls(playlist)
    failed = []
    for track in playlist.get_tracks():
        try:
            # download the image cover art
            title = track.get_track_name()
            
            invalid_chars = '\\/:*?"<>|' # replace incorrect chars
            for char in invalid_chars:
                title = title.replace(char, '_')
            
            image_filename = os.path.join(download_path, f"{title}_cover.jpg")
            download_image(track.get_album_img(), image_filename)
            
            # ddd yt-dlp download options/embed metadata
            ydl_opts = {
                'format': 'bestaudio/best',
                    'postprocessors': [{
                    'key': 'FFmpegMetadata',
                    'add_metadata': True
                }, {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'postprocessor_args': [
                    '-metadata', f'title={track.get_track_name()}',
                    '-metadata', f'artist={track.get_artist_name()}',
                    '-metadata', f'album={track.get_album_name()}',
                    '-strict', '-2'
                ],
                'outtmpl': os.path.join(download_path, f"{track.get_track_name()}.%(ext)s"),
                'logger': MyLogger(),
                'progress_hooks': [my_hook]
            }
            
            # send download request for file from yt-dlp API
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([track.get_url()])
            
            # clean up the downloaded image
            Path(image_filename).unlink()
        except:
            failed.append(track)
         
    # repeat failed tracks until completion
    while len(failed) > 0:
        track = failed.pop(0)
        try:
            # download the image cover art
            image_filename = os.path.join(download_path, f"{track.get_track_name()}_cover.jpg")
            download_image(track.get_album_img(), image_filename)
            
            # ddd yt-dlp download options/embed metadata
            ydl_opts = {
                'format': 'bestaudio/best',
                
                'outtmpl': os.path.join(download_path, f"{track.get_track_name()}.%(ext)s"),
                'logger': MyLogger(),
                'progress_hooks': [my_hook]
            }
            
            # send download request for file from yt-dlp API
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([track.get_url()])
            
            # clean up the downloaded image
            Path(image_filename).unlink()
        except:
            failed.append(track)

# function to download image from URL
def download_image(image_url, output_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image: {image_url}")

# see "progress_hooks" in help(yt_dlp.YoutubeDL)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

# from yt-dlp github
class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

        # Print the FFmpeg command
        if msg.startswith('[ffmpeg] '):
            print(msg[len('[ffmpeg] '):])  # Print the command without the prefix

    #def error(self, msg):
        #print(msg)
        
    