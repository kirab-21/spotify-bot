import spotipy
from bs4 import BeautifulSoup
import requests
import spotify
from spotipy.oauth2 import SpotifyOAuth
# from dotenv import load_dotenv
# import os
#
#
# def configure():
#     load_dotenv()


date = input("Which year do you want to go back(YYYY-MM-DD):")

response = requests.get("https://www.billboard.com/charts/india-songs-hotw/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="a1976213bd974e48af8ca396c046cd72",
        client_secret="be3afac433c342048634ea019cc95003",
        show_dialog=True,
        cache_path="token.txt",
        username="Prabhu",
    )
)
user_id = sp.current_user()["id"]
