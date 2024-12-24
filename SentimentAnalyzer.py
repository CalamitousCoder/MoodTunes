from textblob import TextBlob
blob = TextBlob("TextBlob is a great tool for text analysis!")

def vibeChecker(userVibe):

    userBlob = TextBlob(userVibe)
    calcVibe = userBlob.polarity
    calcCertainty = userBlob.subjectivity
    
    if(calcCertainty < .5):
        print("Can you expand more on your vibes.")
        print("Just a few words or a sentence will suffice")
        
        clarifier = input()
        clariBlob = TextBlob(clarifier + ' ' + userVibe)
        
        newCertainty = clariBlob.subjectivity
        calcVibe = clariBlob.polarity

        if(newCertainty < .5 ):
            print("hmm, ok. I think I got it.")
    return convertVibeToString(calcVibe)

        
    
def convertVibeToString(num:float)-> str:
   if num <= -0.7:  # Despair: [-1, -0.7]
        return 'despair'
   elif -0.7 < num <= -0.2:  # Sad: [-0.6, -0.2]
        return 'sad'
   elif -0.2 < num <= 0.2:  # Mellow: [-0.2, 0.2]
        return 'mellow'
   elif 0.2 < num <= 0.7:  # Happy: [0.2, 0.7]
        return 'happy'
   elif num > 0.7:  # Ecstatic: [0.7, 1]
        return 'ecstatic'
        
def findOutlierFeelings():
    thisDict = {
        
    }