from bs4 import BeautifulSoup
import requests
import spotipy
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
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
month = date.split("-")[1]
for song in song_names:
    res = sp.search(q=f"track:{song} year:{year}", type="track")
    print(res)
    try:
        uri = res["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{song} added to playlist")
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")


# Creating private playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{month}-{year} Hindi Billboard", public=False)
print(playlist)

# Adding songs into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
