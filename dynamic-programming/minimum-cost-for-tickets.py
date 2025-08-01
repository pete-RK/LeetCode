class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * n
        l7, l30 = 0, 0

        for i in range(n):
            while days[i] - days[l7] >= 7:
                l7 += 1
            while days[i] - days[l30] >= 30:
                l30 += 1
            
            c1 = (dp[i-1] if i > 0 else 0) + costs[0]
            c2 = (dp[l7-1] if l7 > 0 else 0) + costs[1]
            c3 = (dp[l30-1] if l30 > 0 else 0) + costs[2]

            dp[i] = min(c1, c2, c3)
        
        return dp[n-1]
            


            