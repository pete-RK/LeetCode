class Solution:
    def minInsertions(self, s: str) -> int:
        t = s[::-1]
        if s == t: return 0
        memo = {}
        n = len(s)
        
        dp = [[-1]*(n+1) for _ in range(n+1)]
        for i in range(n+1): dp[i][0] = 0
        for j in range(n+1): dp[0][j] = 0

        for ind1 in range(1,n+1):
            for ind2 in range(1, n+1):
                take = 0
                if s[ind1-1] == t[ind2-1]:
                    take = 1 + dp[ind1-1][ind2-1]
                no_take = max(dp[ind1-1][ind2], dp[ind1][ind2-1])

                dp[ind1][ind2] = max(take, no_take)

        return n - dp[n][n]
