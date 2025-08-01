class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letter = {2:"abc", 3:"def", 4:"ghi",
                  5:"jkl", 6:"mno", 7:"pqrs",
                  8:"tuv", 9:"wxyz"}
        

        def backtrack(ind, comb):
            if ind == len(digits):
                res.append(comb[:])
                return
            
            for l in letter[int(digits[ind])]:
                backtrack(ind+1, comb+l)
        
        res = []
        backtrack(0, "")

        return res
        

        
        

