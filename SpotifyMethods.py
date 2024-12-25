import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

# Load credentials from secrets.toml
client_id = st.secrets["spotify"]["client_id"]
client_secret = st.secrets["spotify"]["client_secret"]

# Set up Spotify Client Credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def basicSearch(vibe):
    query = vibe + " music"
    results = sp.search(query, limit= 15, type='playlist')  # Increase limit to allow skipping
    
    # Ensure the 'items' list is not empty
    if results['playlists']['items']:
        for playlist in results['playlists']['items']:
            # Ensure the playlist object is valid
            if playlist:
                owner_name = playlist['owner'].get('display_name', '').lower()
                
                # Skip if the playlist is owned by Spotify
                if owner_name == "spotify":
                    continue
                
                playlist_name = playlist.get('name', 'Unknown Playlist')
                playlist_id = playlist.get('id', None)
                
                if playlist_id:
                    
                    return playlist_name, f"Playlist URL: https://open.spotify.com/playlist/{playlist_id}"
                else:
                    print("Playlist found, but missing an ID.")
            else:
                  print(f"No suitable playlists found for '{query}'.")
    else:
        print(f"Sorry, I couldn't find any playlists for '{query}'.")
def genreSearch(vibe, genre):
    # Perform the search with 'playlist' type
    search_query = f"{vibe} {genre} music"
    results = sp.search(q=search_query, type='playlist', limit=15)

    # Check if the 'playlists' key exists and contains items
    if 'playlists' in results and 'items' in results['playlists']:
        playlists = results['playlists']['items']
        if playlists:
            # Iterate through the playlists and filter out those owned by Spotify
            for playlist in playlists:
                # Skip if playlist is None
                if playlist is None:
                    continue
                
                # Ensure the 'owner' key exists and is not None
                owner = playlist.get('owner', None)
                if owner and owner.get('display_name', '').lower() == 'spotify':
                    continue  # Skip this playlist if the owner is Spotify

                playlist_name = playlist.get('name', 'Unknown Playlist')
                playlist_id = playlist.get('id', None)

                if playlist_id:
                     # Exit after printing the first valid playlist
                    return playlist_name, f"Playlist URL: https://open.spotify.com/playlist/{playlist_id}"
                else:
                    print("Playlist found, but missing an ID.")
        else:
            print("No playlists found.")
    else:
        print("Invalid search results, no playlists key found.")
