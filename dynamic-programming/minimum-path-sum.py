class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev = grid[0]
        m, n = len(grid), len(grid[0])

        for i in range(1, n):
            prev[i] += prev[i-1]
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    grid[i][j] += prev[j]
                else:
                    grid[i][j] = min(grid[i][j]+prev[j], grid[i][j]+grid[i][j-1])
            prev = grid[i]
        
        return prev[-1]



        