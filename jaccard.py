from pyjarowinkler.distance import get_jaro_distance

def default_scorer(a, b):
    return get_jaro_distance(a, b)

class Jaccard(object):
    """docstring for Jaccard."""
    def __init__(self, scorer=default_scorer):
        """
        state map is a dict were the keys are shingles
        and the value are sets of words
        """
        self.state_map = dict()
        self.scorer = scorer

    def add_text(self, phrase):
        """
        phrase is a string of many words
        """
        words = phrase.split()
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        shingles = shingle_word(word.strip())
        for shingle in shingles:
            self.add_shingle(shingle, word)


    def add_shingle(self, shingle, word):
        """
        word is a string, ex. "marcus"
        shingle is a three letter string, ex. "mar" from the name "marcus"
        state_map is a dict
        """
        word_set = self.state_map.get(shingle)
        if word_set is None:
            self.state_map[shingle] = set()
        self.state_map[shingle].add(word)

    def search(self, word):
        found_sets = []
        shingles = shingle_word(word)
        for shingle in shingles:
            found_set = self.state_map.get(shingle)
            print found_set
            if found_set is not None:
                found_sets.append(found_set)
        words = []
        for each_set in found_sets:
            for each_word in each_set:
                words.append(each_word)

        return { found: self.scorer(word, found) for found in words }


def shingle_word(word):
    """
    word is a string, ex: "marcus"
    this function shinglizes a string into shingles(strings)
    of size 3 that overlap

    such that shingle_word("marcus") returns ["mar", "arc", "rcu", "cus"]

    """
    shingle_count = len(word) - 2
    shingles = []
    for i in range(0, shingle_count):
        print i
        shingle = word[i: i + 3]
        print shingle
        shingles.append(shingle)
        print shingles


    return shingles
