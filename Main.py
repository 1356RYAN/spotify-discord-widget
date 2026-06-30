import sys
import os
import time
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path
from dotenv import load_dotenv
import requests

if getattr(sys, 'frozen', False):
    base_dir = Path(sys.executable).parent
else:
    base_dir = Path(__file__).parent

# Load environment variables from Client Info.env
load_dotenv(base_dir / "Client Info.env")

client_id = os.getenv("SPOTIFY_CLIENT_ID")  # Spotify client ID
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")  # Spotify client secret
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Bot token
APP_ID = os.getenv("DISCORD_APPLICATION_ID")  # Your Discord application ID
USER_ID = os.getenv("DISCORD_USER_ID")  # The user whose widget identity you own

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="https://127.0.0.1:1234", scope="user-top-read"))


while True:
    # Get the user's top tracks
    results = sp.current_user_top_tracks(limit=5, time_range="short_term")

    # Put the results into a widget payload
    widget_payload = {
        "data": {
            "dynamic": [
                {"type": 3, "name": "songimg_1", "value": {"url": results["items"][0]["album"]["images"][0]["url"]}},
                {"type": 1, "name": "songname_1", "value": f' 1) {results["items"][0]["name"]}'},
                {"type": 1, "name": "songartist_1", "value": f'{", ".join(artist["name"] for artist in results["items"][0]["artists"]) or "Unknown artist"}'},

                {"type": 3, "name": "songimg_2", "value": {"url": results["items"][1]["album"]["images"][0]["url"]}},
                {"type": 1, "name": "songname_2", "value": f' 2) {results["items"][1]["name"]}'},
                {"type": 1, "name": "songartist_2", "value": f'{", ".join(artist["name"] for artist in results["items"][1]["artists"]) or "Unknown artist"}'},

                {"type": 3, "name": "songimg_3", "value": {"url": results["items"][2]["album"]["images"][0]["url"]}},
                {"type": 1, "name": "songname_3", "value": f' 3) {results["items"][2]["name"]}'},
                {"type": 1, "name": "songartist_3", "value": f'{", ".join(artist["name"] for artist in results["items"][2]["artists"]) or "Unknown artist"}'},

                {"type": 3, "name": "songimg_4", "value": {"url": results["items"][3]["album"]["images"][0]["url"]}},
                {"type": 1, "name": "songname_4", "value": f' 4) {results["items"][3]["name"]}'},
                {"type": 1, "name": "songartist_4", "value": f'{", ".join(artist["name"] for artist in results["items"][3]["artists"]) or "Unknown artist"}'},
                
                {"type": 3, "name": "songimg_5", "value": {"url": results["items"][4]["album"]["images"][0]["url"]}},
                {"type": 1, "name": "songname_5", "value": f' 5) {results["items"][4]["name"]}'},
                {"type": 1, "name": "songartist_5", "value": f'{", ".join(artist["name"] for artist in results["items"][4]["artists"]) or "Unknown artist"}'}
            ]
        }
    }

    #stringify
    payload_json = json.dumps(widget_payload)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {BOT_TOKEN}",
        "User-Agent": "DiscordBot (https://github.com/discord/discord-api-docs, 1.0.0)"
    }

    url = f"https://discord.com/api/v9/applications/{APP_ID}/users/{USER_ID}/identities/0/profile"
    response = requests.patch(url, headers=headers, data=payload_json)

    os.system('cls')
    print(response.status_code)
    print(response.text)
    time.sleep(43200) # wait 12 hours before updating the widget again
input("Press Enter to exit...")
