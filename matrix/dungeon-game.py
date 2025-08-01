class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf')]*(cols+1) for _ in range(rows+1)]
        dp[rows-1][cols], dp[rows][cols-1] = 1, 1

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - grid[i][j], 1)
        
        return dp[0][0]

        