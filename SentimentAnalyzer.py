from textblob import TextBlob
blob = TextBlob("TextBlob is a great tool for text analysis!")

def vibeChecker(userVibe):

    userBlob = TextBlob(userVibe)
    calcVibe = userBlob.polarity
    calcCertainty = userBlob.subjectivity
    
    if(calcCertainty < .5):
        print("Can you expand more on your vibes.")
        print("Just a few words or a sentence will suffice")
        clarfier = input()
        clariBlob = TextBlob(clarifier + ' ' + userVibe)
        calcVibe = clariBlob.polarity
        
        if(calcVibe < .5 ):
            print("hmm, ok")
        calcC = clariBlob.subjectivity
        return classifyVibe(calcVibe)
    
def classifyVibe(num):
    if(num == -1 or num <= -7.):
        return despair
    elif(num > .8):

        return
        
