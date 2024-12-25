import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException

# Set up Spotify authentication
clientId = '1f6e1c1b2ec54efc9d8fb0e4df9e8d91'
clientSecret = '18331dc1fe41432b94a1af96eb76db1b' 
client_credentials_manager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


query = vibe + " music"  # Assuming you want to append ' music' to the vibe
print("I searched:", query)

    # Perform the search with 'playlist' type
results = sp.search(q=query, type='playlist', limit=5)  # Use Spotipy here

    # Debug: print the search results to see its structure
print("Search Results:", results)

    # Check if the 'playlists' key exists and contains items
if 'playlists' in results and 'items' in results['playlists']:
        playlists = results['playlists']['items']
        if playlists:
            # Print the first playlist's name and link
            playlist = playlists[0]
            print(f"Playlist Name: {playlist['name']}")
            print(f"Playlist URL: https://open.spotify.com/playlist/{playlist['id']}")
            
            # Fetch tracks from the playlist
            tracks = sp.playlist_tracks(playlist['id'])
            
            # Check and print the artist names for the first few tracks
            for track in tracks['items']:
                track_info = track.get('track')  # Safely get the track object
                if track_info and track_info.get('artists'):  # Ensure both track and artists exist
                    print(f"Artist Name: {track_info['artists'][0]['name']}")
                else:
                    print("Track or artist data missing")
        else:
            print("No playlists found.")
else:
        print("Invalid search results, no playlists key found.")