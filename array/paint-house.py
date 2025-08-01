class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev = costs[0]

        for curr in costs[1:]:
            dp = curr
            dp[0] = min(dp[0] + prev[1], dp[0] + prev[2])
            dp[2] = min(dp[2] + prev[1], dp[2] + prev[0])
            dp[1] = min(dp[1] + prev[0], dp[1] + prev[2])
            prev = dp
        
        return min(prev)