class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_1, index_2 = float('inf'), float('inf')
        min_val = float('inf')

        for i in range(len(wordsDict)):
            if word1 == word2 == wordsDict[i]:
                index_1 = index_2
                index_2 = i
            elif wordsDict[i] == word1:
                index_1 = i
            elif wordsDict[i] == word2:
                index_2 = i

            min_val = min(min_val, abs(index_1 - index_2))
        return min_val



        

            
