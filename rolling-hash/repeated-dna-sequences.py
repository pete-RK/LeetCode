class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []

        char_set = set()
        res = set()

        for itr in range(len(s)-9):
            word = s[itr:itr+10]
            if word in char_set:
                res.add(word)
            else:
                char_set.add(word)
        
        return list(res)



