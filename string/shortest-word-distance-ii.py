class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_dict = defaultdict(list)
        self.generate_dict(wordsDict)

    def generate_dict(self, wordsDict: List[str]):
        for index, word in enumerate(wordsDict):
            self.word_dict[word].append(index)

    def min_distance(self, wl1: List[int], wl2: List[int]) -> int:
        i = 0
        j = 0
        min_diff = float('inf')
        while i < len(wl1) and j < len(wl2):
            diff = abs(wl1[i] - wl2[j])
            min_diff = min(min_diff, diff)
            if wl1[i] < wl2[j]:
                i += 1
            else:
                j += 1
        return min_diff

    def shortest(self, word1: str, word2: str) -> int:
        return self.min_distance(self.word_dict[word1], self.word_dict[word2])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)