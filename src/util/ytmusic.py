import requests
import sys

from ytmusicapi import YTMusic

def get_song_link(track_name: str, artist_name: str) -> str:
    ytmusic = YTMusic()
    search_query = artist_name + " " + track_name
    
    results = ytmusic.search(search_query, filter="songs")
    try:
        v_id = results[0]["videoId"]
        print("TEST: V-ID SUCCESS")
        return v_id
    except:
        print("ERROR: could not find song.")
        print("Application closing...")
        sys.exit()
    