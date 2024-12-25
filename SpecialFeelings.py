class SpecialFeelings:
      outlierList = []  # Initialize the outlier list
    
      def __init__(self, name, mood):
        self.name = name
        self.mood = mood
        SpecialFeelings.outlierList.append(self)  # Add instance to the outlier list

      @classmethod 
      def getOutliers(cls):
        return cls.outlierList  # Return the list of outliers

        ## Write down our outliers
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
            
      