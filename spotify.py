import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='',
                                                   client_secret='',
                                                   redirect_uri='http://localhost:3007/callback',
                                                   scope='user-modify-playback-state'))
def play_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)

    if results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        song_duration_ms = results['tracks']['items'][0]['duration_ms']
        sp.start_playback(uris=[song_uri])
        print(f"Now playing: {song_name}")

        return song_duration_ms
    else:
        print("Song not found.")

def pause_song():
    try:
        print("Stoping the current song")
        sp.pause_playback()

    except Exception as e:
        print(f"Some Error occured  : {str(e)}")


def get_artist_top_tracks(artist_name):
    results = sp.search(q=artist_name, type='artist', limit=1)

    if results['artists']['items']:
        artist_id = results['artists']['items'][0]['id']
        top_tracks = sp.artist_top_tracks(artist_id)

        if top_tracks['tracks']:
            return [track['name'] for track in top_tracks['tracks']]
        else:
            print(f"No top tracks found for {artist_name}.")
            return []
    else:
        print(f"Artist '{artist_name}' not found.")
        return []

# Replace the placeholders with your actual credentials and redirect URI.
# Make sure to add 'YOUR_REDIRECT_URI' to the Redirect URIs list in your Spotify Developer Dashboard.

