import requests
from ytmusicapi import YTMusic

def get_song_link(track_name: str, artist_name: str) -> str:
    ytmusic = YTMusic()
    search_query = artist_name + " " + track_name
    
    results = ytmusic.search(search_query, filter="songs")
    print(results[0]["videoId"])
    