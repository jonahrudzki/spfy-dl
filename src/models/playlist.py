import requests

from models.track import Track

class Playlist:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.tracks = []
    
    def create_tracks(self, tracks_url: str, headers) -> None:
        tracks_response = requests.get(tracks_url, headers=headers)
        tracks_data = tracks_response.json()
        
        for track in tracks_data['items']: # TrackObject JSON
            track_name = track['track']['name']
            album_name = track['track']['album']['name']
            album_img_url = track['track']['album']['images'][0]['url'] 
            artist_name = track['track']['artists'][0]['name']
            
            self.tracks.append(Track(track_name, album_name, album_img_url, artist_name))
            
        