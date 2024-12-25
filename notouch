import time as builtin_time
import Utils
import SentimentAnalyzer
import SpotifyMethods
import streamlit as st
from textblob import TextBlob

st.write("Hello, World!")



def main():
    print("What's you're vibe right now?")
    currVibe = input()
    wordsList = SentimentAnalyzer.getWords(currVibe)
    areOutliers, particFeeling = SentimentAnalyzer.findOutlierFeelings(wordsList)
    
    if(not areOutliers):
      currVibe = SentimentAnalyzer.vibeChecker(currVibe)
      print("not an outlier the feeling")
    else:
       currVibe = particFeeling
    
    print(" I got your vibe was " +  currVibe)

    print("List a genre of music you'd like to hear")
    Utils.printAndSleep("If you have no preference type any", 2)
    userGenre = input()
    hasPreference = userGenre.lower() != "any" 

    Utils.printAndSleep("Would you like to:",2)
   
    Utils.printAndSleep("\t Intensify Vibe",1)
    desiredMood = 'IV'
    Utils.printAndSleep("\t Keep Vibe Going", 1)
    desiredMood = 'const'
    Utils.printAndSleep("\t Balance Mood", 1)
    desiredMood = 'bal'
    Utils.printAndSleep("\t Gradually Shift Mood",1)
    desiredMood = 'shift'
    Utils.printAndSleep("\t Feel Whiplash",1)
    desiredMood = 'whip'
    answer = input()

    match answer:
      case 'IV':
        print("Handle case IV here.")
      case 'const':
        if hasPreference:
            SpotifyMethods.genreSearch(currVibe, userGenre)
        else:
            SpotifyMethods.genericSearch(currVibe)
      case 'bal':
        print("Handle case 'bal' here.")
      case 'shift':
        print("Handle case 'shift' here.")
      case 'whip':
        print("Handle case 'whip' here.")
if __name__ == "__main__": main()