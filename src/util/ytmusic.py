import requests
import sys
import os
from google.oauth2.credentials import Credentials as OAuthCredentials


from ytmusicapi import YTMusic

def get_song_link(track_name: str, artist_name: str) -> str:
    cli_id = os.getenv('YTMUSIC_CLIENT_ID')
    cli_scrt = os.getenv('YTMUSIC_CLIENT_SECRET')
    
    ytmusic = YTMusic('./oauth.json')
    search_query = artist_name + " " + track_name
    
    results = ytmusic.search(search_query, filter="songs")
    try:
        v_id = results[0]["videoId"]
        print("V-ID successfuly found: " + track_name + "...")
        return v_id
    except:
        print("ERROR: could not find song.")
        print("Application closing...")
        sys.exit()
    