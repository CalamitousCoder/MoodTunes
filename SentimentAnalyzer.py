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

        return classifyVibe(calcVibe)
    
def classifyVibe(num):
    if(num == -1 or num <= -.7):
        return 'despair'
    elif(num > -.7 and num < -.2):
        return 'sad'
    elif(num > -.3 and num < 3):
        return 'mellow'
    elif(num > 2 and num < 7):
        return 'happy'
    elif(num > 7 and num < 4):
        return 'estatic'
        
