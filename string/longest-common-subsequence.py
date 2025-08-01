class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(n+1): dp[0][i] = 0
        for j in range(m+1): dp[j][0] = 0

        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                take = 0
                if t1[ind1-1] == t2[ind2-1]:
                    take = 1 + dp[ind1-1][ind2-1]
                no_take = max(dp[ind1][ind2-1], dp[ind1-1][ind2])

                dp[ind1][ind2]= max(take, no_take)
        return dp[m][n]





        

            

            