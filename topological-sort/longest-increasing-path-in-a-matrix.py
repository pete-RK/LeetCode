class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix[0]), len(matrix)
        memory = [[-1]*n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if memory[x][y] != -1:
                return memory[x][y]

            max_path = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(matrix)
                    and 0 <= ny < len(matrix[0])
                    and matrix[nx][ny] > matrix[x][y]
                ):
                    max_path = max(max_path, 1 + dfs(nx, ny))

            memory[x][y] = max_path
            return max_path
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        
        return res

