class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        # 1D array for current row, size n+1
        dp = [0] * (n + 1)
        
        # Iterate over rows (i1)
        for i1 in range(1, n + 1):
            prev = 0  # Tracks dp[i1-1][i2-1] (diagonal from previous row)
            for i2 in range(1, n + 1):
                # Store current dp[i2] before overwriting (acts as dp[i1-1][i2])
                curr = dp[i2]
                # If characters match, use diagonal value
                if s[i1 - 1] == t[i2 - 1]:
                    dp[i2] = 1 + prev
                else:
                    # No match, max of left (dp[i1][i2-1]) and up (dp[i1-1][i2])
                    dp[i2] = max(dp[i2 - 1], curr)
                # Update prev for next iteration (prev becomes dp[i1-1][i2])
                prev = curr
        
        return dp[n]
            
            

        