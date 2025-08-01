class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recursion(ind):
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if ind in memo: return memo[ind]

            if ind + 1 < len(s) and 10 <= int(s[ind:ind+2]) <= 26:
                memo[ind] = recursion(ind+1) + recursion(ind+2)
            else:
                memo[ind] = recursion(ind+1)
            
            return memo[ind]
        
        return recursion(0)

            
        
        
        


            

        