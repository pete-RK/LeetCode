class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid2 or not grid1[0] or not grid2[0]:
            return 0
        
        rows, cols = len(grid1), len(grid1[0])
        self.count = 0  # Initialize count of sub-islands
        
        def dfs(x: int, y: int) -> bool:
            # Mark current cell as visited in grid2
            grid2[x][y] = 0
            is_sub_island = True  # Track if current island is a sub-island
            
            # Explore all four directions
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid2[nx][ny] == 1:
                    # If corresponding cell in grid1 is 0, this is not a sub-island
                    if grid1[nx][ny] == 0:
                        is_sub_island = False
                    # Continue DFS; if any recursive call returns False, mark as not a sub-island
                    if not dfs(nx, ny):
                        is_sub_island = False
            
            return is_sub_island
        
        # Iterate through each cell in grid2
        for i in range(rows):
            for j in range(cols):
                # Start DFS only if cell is land in both grids
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    if dfs(i, j):
                        self.count += 1
        
        return self.count