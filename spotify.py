import spotipy
from spotipy.oauth2 import SpotifyOAuth
import subprocess



class SpotifyControl:

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='3e6e56512ed143ddac9a8155278104c2',
                                                        client_secret='723a92d37fce487e8c761a17fddab70d',
                                                        redirect_uri='http://localhost:3007/callback',
                                                        scope='user-modify-playback-state'))
        self.tries = 2
        

    def play_song(self,song_name):
        try:
            results = self.sp.search(q=song_name, type='track', limit=1)

            if results['tracks']['items']:
                song_uri = results['tracks']['items'][0]['uri']
                song_duration_ms = results['tracks']['items'][0]['duration_ms']
                self.sp.start_playback(uris=[song_uri])
                print(f"Now playing: {song_name}")

                return song_duration_ms
            else:
                print("Song not found.")
        except Exception as e:
            if self.tries > 0:
                print("Start activating the player device")
                self.run_terminal_command()
                self.play_song(song_name=song_name)
                print(f"An  error occurred , {str(e)}")
            



    def run_terminal_command(self):
        try:
            subprocess.Popen(['open', '-a', 'Terminal', 'utils/run_command.sh'])
        except Exception as e:
            print(f"An error occurred: {e}")

    def pause_song(self,song_name):
        try:
            print(f"Stopping the song : {song_name}")
            self.sp.pause_playback()

        except Exception as e:
            print(f"Some Error occured  : {str(e)}")


    def play_song_uri(self,song_uri):
        
        self.sp.start_playback(uris=[song_uri])
        print(f"playing the song {str(song_uri)}")

    def get_artist_top_tracks(self,artist_name):
        results = self.sp.search(q=artist_name, type='artist', limit=1)

        if results['artists']['items']:
            artist_id = results['artists']['items'][0]['id']
            top_tracks = self.sp.artist_top_tracks(artist_id)

            if top_tracks['tracks']:
                tracks_list = []
                for track in top_tracks['tracks']:
                    track_info = {
                        'name': track['name'],
                        'uri': track['uri']
                    }
                    tracks_list.append(track_info)
                return tracks_list
            else:
                print(f"No top tracks found for {artist_name}.")
                return []
        else:
            print(f"Artist '{artist_name}' not found.")
            return []

    # Replace the placeholders with your actual credentials and redirect URI.
    # Make sure to add 'YOUR_REDIRECT_URI' to the Redirect URIs list in your Spotify Developer Dashboard.

