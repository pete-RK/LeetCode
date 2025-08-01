class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        queue = deque()
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if nx in range(rows) and ny in range(cols) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            if not queue: break
            time += 1
        
        return time if fresh == 0 else -1
                
            



