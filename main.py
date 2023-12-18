from bs4 import BeautifulSoup
import requests
import spotify
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to go back(YYYY-MM-DD):")

response = requests.get("https://www.billboard.com/charts/india-songs-hotw/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]