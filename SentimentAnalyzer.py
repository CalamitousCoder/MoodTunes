from textblob import TextBlob

class SpecialFeelings:
    outlierList = []  # Initialize the outlier list

    def __init__(self, name, mood):
        self.name = name
        self.mood = mood
        SpecialFeelings.outlierList.append(self)  # Add instance to the outlier list

    @classmethod 
    def getOutliers(cls):
        return cls.outlierList  # Return the list of outliers

def vibeChecker(userVibe):
    print("entered Vibe checker")
    userBlob = TextBlob(userVibe)
    calcVibe = userBlob.polarity
    calcCertainty = userBlob.subjectivity
    
    if calcCertainty < .5:
        print("Can you expand more on your vibes?")
        print("Just a few words or a sentence will suffice.")
        
        clarifier = input()
        clariBlob = TextBlob(clarifier + ' ' + userVibe)
        
        newCertainty = clariBlob.subjectivity
        calcVibe = clariBlob.polarity

        if newCertainty < .5:
            print("hmm, ok. I think I got it.")
    print("vibe number was " + calcVibe)
    print("got converted to " + convertVibeToString(calcVibe))
    return convertVibeToString(calcVibe)

def convertVibeToString(num: float) -> str:
    if num <= -0.7:  # Despair: [-1, -0.7]
        return 'depressing'
    elif -0.7 < num <= -0.2:  # Sad: [-0.6, -0.2]
        return 'sad'
    elif -0.2 < num <= 0.2:  # Mellow: [-0.2, 0.2]
        return 'mellow'
    elif 0.2 < num <= 0.7:  # Happy: [0.2, 0.7]
        return 'happy'
    elif num > 0.7:  # Ecstatic: [0.7, 1]
        return 'cheerful'

def getWords(phrase):
    phraseBlob = TextBlob(phrase)
    return phraseBlob.words

def findOutlierFeelings(wordsList):
    outlierList = SpecialFeelings.getOutliers()
    for x in wordsList:
        for y in outlierList:
            if x == y.name:
                return True, y.name  
    return False, -1


# Define the outlier feelings
depressed = SpecialFeelings("depressed", "despair")
hype = SpecialFeelings("hype", "elated")
whimsical = SpecialFeelings("whimsical", "whimsy")
whimsy = SpecialFeelings("whimsy", "whimsy")

anger = SpecialFeelings("anger", "mad")
angry = SpecialFeelings("angry", "mad")
mad = SpecialFeelings("mad", "mad")
furious = SpecialFeelings("furious", "rage")
fuming = SpecialFeelings("fuming", "rage")
rage = SpecialFeelings("rage", "rage")

hater = SpecialFeelings("hater", "hater")
hateful = SpecialFeelings("hateful", "rage")

lovesick = SpecialFeelings("lovesick", "romantic")
romantic = SpecialFeelings("romantic", "romantic")
heartbroken = SpecialFeelings("heartbroken", "heartbroken")

smug = SpecialFeelings("smug", "smug")

nostalgic = SpecialFeelings("nostalgic", "nostalgic")