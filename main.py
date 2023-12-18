import spotipy
from bs4 import BeautifulSoup
import requests
import spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


# Scraping BillBoard Hindi
date = input("Which year do you want to go back(YYYY-MM-DD):")
response = requests.get("https://www.billboard.com/charts/india-songs-hotw/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]

# Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id={os.getenv('CLIENT_ID')},
        client_secret={os.getenv('CLIENT_SECRET')},
        show_dialog=True,
        cache_path="token.txt",
        username="Prabhu",
    )
)
user_id = sp.current_user()["id"]
