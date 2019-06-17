filler_words = ["a", "after", "all", "All", "am", "an",
                "and", "Any", "any", "are", "as", "As", "at", "be", "been", "but", "by", "can", "could",
                "did", "during", "for", "For", "from", "had", "has", "have", "he", "hence", "henceforth",
                "hereafter",
                "herein", "however", "in", "In", "indeed", "is", "it", "It", "of", "on", "On", "one", "or",
                "our",
                "out", "per", "shall", "she", "since", "so", "the", "The", "then", "There", "thereafter",
                "therefore", "they", "this", "through", "thus", "to", "until", "was", "were", "when",
                "whereby", "which", "while", "will", "with", "would", "you", "With", "While", "When", "What",
                "We", "get", "Very", "very", "much", "many", "Many", "too", "being", "should",
                "Upon", "upon", "Too", "there", "due", "Due"
                ]

class Clean:

    def __init__(self, str_input):
        self.to_clean = str_input
        self.new_str = ""
        toggle = False


    """
    TODO: Find a neat way to remove html formatting
    """


    def remove_punctuation(self):
        for c in self.to_clean:
            if (('a' <= c <= 'z') or '0' <= c <= '9' or 'A' <= c <= 'Z'):
                self.new_str += c

        return self.new_str


    def tokenize(self):
        #Remove html formatting
        sentence = self.remove_punctuation()
        words = sentence.split(' ')

        filtered = set()

        #manually filter
        for elem in words:
            if elem in filler_words:
                filtered.add(elem)

