class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        n //= 2

        for i in range(n-1, -1, -1):
            l, r = sorted((cost[2*i+1], cost[2*i+2]))
            res += r - l
            cost[i] += r
        
        return res

            



