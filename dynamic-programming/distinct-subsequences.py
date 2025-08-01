class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def recursion(ind1, ind2):
            if ind2 >= len(t):
                return 1
            if ind1 >= len(s): 
                return 0

            if (ind1, ind2) in memo:
                return memo[(ind1,ind2)]
            
            take, no_take = 0, 0
            if s[ind1] == t[ind2]:
                take = recursion(ind1+1, ind2+1)
            no_take = recursion(ind1+1, ind2)

            memo[(ind1,ind2)] = take + no_take
            return memo[(ind1,ind2)]

        return recursion(0, 0)



