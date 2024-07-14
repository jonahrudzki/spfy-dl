import requests
import json

import base64

import sys
import os
from dotenv import load_dotenv

def get_token():
    # get client id and secret from .env
    load_dotenv()
    
    cli_id = os.getenv('SPOTIFY_CLIENT_ID')
    cli_scrt = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    # auth header for POST request
    raw_str = cli_id + ":" + cli_scrt
    auth_key = base64.b64encode(raw_str.encode("ascii")).decode("ascii")
    auth_header = {'Authorization': 'Basic ' + auth_key}
    
    # data form & url
    data_payload = {'grant_type': 'client_credentials'}
    post_url = "https://accounts.spotify.com/api/token"
    
    # handle request response
    response = requests.post(post_url, headers=auth_header, data=data_payload, json=True)
    
    if response.status_code == 200:
        print("Access token received successfully!")
        access_data = response.json()
        return access_data["access_token"]
    else:
        print("Invalid request received! Status code: " + str(response.status_code))
        print("Please try again, ensuring that CLIENT_ID and CLIENT_SECRET are both correct!")
        print("Application closing...")
        sys.exit()