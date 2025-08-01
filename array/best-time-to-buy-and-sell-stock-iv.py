class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[0]* (k+1) for _ in range(2)] for _ in range(n+1)]
        
        for ind in range(n-1, -1, -1):
            for can_buy in range(2):
                for limit in range(1, k+1):
                    take = 0
                    if can_buy == 1:
                        take = max(-prices[ind] + dp[ind+1][1-can_buy][limit], dp[ind+1][can_buy][limit])
                    else:
                        take = max(prices[ind] + dp[ind+1][1-can_buy][limit-1], dp[ind+1][can_buy][limit])

                    dp[ind][can_buy][limit] = take
        return dp[0][1][k]