class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands, visited = set(), set()
        rows, cols = len(grid), len(grid[0])

        def get_shape(shape):
            x, y = shape[0][0], shape[0][1]
            distances = [(0, 0)]

            for dx, dy in shape[1:]:
                nx, ny = dx - x, dy - y
                distances.append((nx, ny))

            islands.add(tuple(distances))

        def dfs(x, y, shape):
            shape.append((x,y))
            visited.add((x,y))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]  

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 1:
                    dfs(nx, ny, shape)

            return shape
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    shape = dfs(i, j, [])
                    get_shape(shape)

        return len(islands)
        



            