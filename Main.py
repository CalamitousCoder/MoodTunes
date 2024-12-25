import Utils
import SentimentAnalyzer
import SpotifyMethods


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

   # need textBlob stuff

    Utils.printAndSleep("List a genre of music you'd like to hear")
    Utils.printAndSleep("If you have no preference type any")
    unsortedGenres = input()
    wordsList = SentimentAnalyzer.getWords(unsortedGenres)
    preferredGenre = Sp

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

    match desiredMood:
       case 'IV':
          print
       case 'const':
          fdfd
       case 'bal':
          fdgd
       case 'shift':
          fdgd
       case 'whip':
          fgdg
if __name__ == "__main__": main()