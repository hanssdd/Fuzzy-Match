class Compare:


    """
    REQUIRES: Two (2) sets of sets of words and threshold value;
				  word1(check) and word2(against)
	MODIFIES: words_1, words_2, threshold
	EFFECTS	: Creates a Compare object to with members words_1, words_2, threshold
	          Initializes an empty dictionary scores[set<string>] = float

    """
    def __init__(self, words_1, words_2, threshold, num_in):
        self.words_1 = words_1
        self.words_2 = words_2
        self.threshold = threshold
        self.scores = {}
        self.flags = []
        self.num_parameters = num_in


    """

    REQUIRES: Two (2) sets of words; source and check
	MODIFIES: Nothing
	EFFECTS	: Finds similarity index between 2 sets of words

    """
    def compare(self, source, check):
        count = 0
        size = len(check)

        if size <= 5:
            return 0

        for it in source:
            if it in check or it + 's' in check:
                count += 1

        """

        casting required to avoid rounding
        e.g. if count = 4, float = 10
        then count/size without casting is 0

        """
        s = float(count)/float(size)*100

        return s

    """
    REQUIRES: A list of set<string> with length num_parameters
    MODIFIES: Nothing
    EFFECTS : Returns the score of an array, given by the arithmetic mean of scores of each column
    
    """


    """
    REQUIRES: Set of words
	MODIFIES: Nothing
	EFFECTS	: Returns max{min score > threshold, highest similarity index}
	"""
    def score(self, words):

        for pll in self.words_2 :
            s = self.compare(words, pll)
            if s > self.threshold:
                return s

        return 0

    def all_scores(self):
        count = 0
        for pll in self.words_1:
            s = self.score(pll)
            self.scores[ pll ] = s

    # no need for this function?
    def getScores(self):
        self.all_scores()
        return self.scores

    def similar(self):

        self.all_scores()
        for it in self.scores:
            if self.scores[it] > self.threshold:
                self.flags.append(it)

        return self.flags

