class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = 0
            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    dfs(nx, ny)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    dfs(i, j)
        
        return sum(sum(row) for row in grid)