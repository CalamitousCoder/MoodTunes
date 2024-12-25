import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify authentication
clientId = '1f6e1c1b2ec54efc9d8fb0e4df9e8d91'
clientSecret = '18331dc1fe41432b94a1af96eb76db1b' 
client_credentials_manager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def is_valid_genre(genre):
    valid_genres = sp.recommendation_genre_seeds()
    return genre in valid_genres
def any_genres_in_list(list):
    for words in list:
        if(is_valid_genre(words)):
            return words
        else:
            return any

         