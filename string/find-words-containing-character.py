class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i in range(len(words)):
            if x in Counter(words[i]):
                res.append(i)
        
        return res