import requests
import sys

from util import auth, songdl
from models.track import Track
from models.playlist import Playlist

if __name__ == "__main__":
    # get auth access token
    access_token = auth.get_token()
    
    print("""\n+===============================+
Spotify to MP3 Playlist Converter          
+===============================+\n""")
    
    # get playlist id and send get request for playlist data
    playlist_id = input("Please enter a playlist code: ")
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    
    response = requests.get(url, headers=headers)
    
    # parse JSON playlist data
    if response.status_code != 200:
        print("Invalid request receive! Status code: " + str(response.status_code))
        print("Please try again, ensuring that you have entered a valid publicplaylist code")
        print("Application closing...")
        sys.exit()
    
    # continue if valid public playlist detected
    print("Retrieving playlist data...")
    pl_data = response.json()
    
    playlist = Playlist(pl_data["name"], playlist_id)
    playlist.create_tracks(pl_data["tracks"]["href"], headers)
    
    # ytmusicapi call to get top song search request yt video id
    songdl.download_tracks(playlist)