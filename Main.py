import time
import spotipy
import Utils
from spotipy.oauth2 import SpotifyClientCredentials


# Set up Spotify authentication
clientId = '1f6e1c1b2ec54efc9d8fb0e4df9e8d91'
clientSecret = '18331dc1fe41432b94a1af96eb76db1b' 
client_credentials_manager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def main():
    # Your code goes here

    print("What's you're vibe right now?")
    currVibe = input()

    ## need textBlob stuff

    Utils.printAndSleep("What genres of music are in the mood to hear")
    unsortedResponse = input()
    # need to add tokenizer

    Utils.printAndSleep("Would you like to:",2)
   
    Utils.printAndSleep("\t Intensify Vibe",1)
    desiredMood = 'IV'
    Utils.printAndSleep("\t Keep Vibe Going", 1)
    desiredMood = 'const'
    Utils.printAndSleepprint("\t Balance Mood", 1)
    desiredMood = 'bal'
    Utils.printAndSleep("\t Gradually Shift Mood",1)
    desiredMood = 'shift'
    Utils.printAndSleep("\t Feel Whiplash",1)
    desiredMood = 'whip'

