class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0
        m, n = len(grid), len(grid[0])

        prev = [0]*n
        prev[0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    prev[j] = 0
                else:
                    if j > 0:
                        prev[j] += prev[j-1]
        
        return prev[-1]
                



        