class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Handle empty grid or same color
        if not image or not image[0] or image[sr][sc] == color:
            return image
        
        original = image[sr][sc]
        rows, cols = len(image), len(image[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x: int, y: int) -> None:
            # Base case: Check if pixel is valid and matches original
            if x < 0 or x >= rows or y < 0 or y >= cols or image[x][y] != original:
                return
            
            # Replace color
            image[x][y] = color
            
            # Recurse in four directions
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        
        # Start DFS at (sr, sc)
        dfs(sr, sc)
        return image

