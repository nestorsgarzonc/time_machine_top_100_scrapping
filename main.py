from scrapping.billboard import get_name_songs
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
date = input('Enter date to scratch YYYY-MM-DD: ')
song_names = get_name_songs(date)

spotipy_sesion = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri='http://localhost',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotipy_sesion.me()['id']

spotipy.prompt_for_user_token(
    user_id, scope='playlist-modify-public', redirect_uri='http://localhost'
)


def get_user_token():
    return spotipy_sesion.current_user()


def get_spotify_id_songs():
    spotipy_songs = []
    for song in song_names:
        try:
            print(f'Searching: {song}')
            ns = spotipy_sesion.search(song, limit=1)
            spotipy_songs.append(ns['tracks']['items'][0]['uri'])
        except Exception as e:
            print(f'Dont found {e}')
    return spotipy_songs


spotipy_songs = get_spotify_id_songs()

print(spotipy_songs)

playlist = spotipy_sesion.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
spoplaylist = spotipy_sesion.playlist_add_items(
    playlist_id=playlist["id"], items=spotipy_songs
)
