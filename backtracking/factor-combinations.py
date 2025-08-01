class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1: return []
        factors = list(filter(lambda x: n % x == 0, range(2, n//2 + 1)))
        res = []
        def dfs(ind, rem, curr):
            if rem == 1:
                res.append(curr.copy())
                return
            
            for i in range(ind, len(factors)):
                if rem % factors[i] == 0:
                    dfs(i, rem//factors[i], curr + [factors[i]])
            
        dfs(0, n, [])
        return res
