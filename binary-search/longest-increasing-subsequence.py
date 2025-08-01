class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j]: LIS length starting at i with previous element at j (j=n means no prev)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Base case: when i = n, length is 0 for all j
        for j in range(n + 1):
            dp[n][j] = 0
        
        # Fill table from right to left (bottom-up)
        for i in range(n - 1, -1, -1):
            for j in range(n + 1):
                # Don't take nums[i]
                no_take = dp[i + 1][j]
                
                # Take nums[i] if possible
                take = 0
                if j == n or nums[i] > nums[j]:  # j=n means no prev (like -inf)
                    take = 1 + dp[i + 1][i]  # New prev becomes nums[i]
                
                dp[i][j] = max(take, no_take)
        
        # Result is at dp[0][n] (start at 0 with no previous element)
        return dp[0][n]


            


