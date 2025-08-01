class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(x, y):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx in range(len(grid)) and ny in range(len(grid[0])) and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        
        return count


