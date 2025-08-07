class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = []

        def dfs(x, y, max_x, max_y):
            grid[x][y] = 0
            max_x, max_y = max(max_x, x), max(max_y, y)
            directions = [[1,0],[0,1],[-1,0],[-1,0]]

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                    rx, ry = dfs(nx, ny, max_x, max_y)
                    max_x, max_y = max(max_x, rx), max(max_y, ry)
            
            return max_x, max_y
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    a, b = i, j
                    c, d = dfs(i, j, 0, 0)
                    res.append([a,b,c,d])
        
        return res

        



