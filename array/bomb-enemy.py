class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # Initialize the maximum number of enemies killed
        maxkilled = 0
        # Dictionary to store the number of enemies that can be killed from each empty cell
        hashmap = collections.defaultdict(int)
        
        def helper(row: int, col: int):
            
            # Check upward direction
            for i in range(row - 1, -1, -1):  # Traverse upwards
                if grid[i][col] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(i, col)] += 1
                if grid[i][col] == "W":  # Stop at a wall
                    break

            # Check downward direction
            for i in range(row + 1, len(grid)):  # Traverse downwards
                if grid[i][col] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(i, col)] += 1
                if grid[i][col] == "W":  # Stop at a wall
                    break

            # Check left direction
            for j in range(col - 1, -1, -1):  # Traverse left
                if grid[row][j] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(row, j)] += 1
                if grid[row][j] == "W":  # Stop at a wall
                    break

            # Check right direction
            for j in range(col + 1, len(grid[0])):  # Traverse right
                if grid[row][j] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(row, j)] += 1
                if grid[row][j] == "W":  # Stop at a wall
                    break

        # Traverse the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "E":  # If the current cell contains an enemy
                    helper(i, j)  # Calculate potential kills from all surrounding empty cells

        # If there are no valid empty cells, return 0
        if not hashmap.values():
            return 0

        # Return the maximum number of enemies that can be killed from a single empty cell
        return max(hashmap.values())
                