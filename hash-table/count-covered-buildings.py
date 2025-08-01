class Solution:
    def countCoveredBuildings(self, n: int, grid: List[List[int]]) -> int:
        x_to_y_bounds = defaultdict(lambda: [inf, -inf])  # [min_y, max_y]
        y_to_x_bounds = defaultdict(lambda: [inf, -inf])  # [min_x, max_x]
        
        # Populate maps with min/max bounds
        for x, y in grid:
            x_to_y_bounds[x][0] = min(x_to_y_bounds[x][0], y)  # Update min_y
            x_to_y_bounds[x][1] = max(x_to_y_bounds[x][1], y)  # Update max_y
            y_to_x_bounds[y][0] = min(y_to_x_bounds[y][0], x)  # Update min_x
            y_to_x_bounds[y][1] = max(y_to_x_bounds[y][1], x)  # Update max_x
        
        count = 0
        # Check each building for coverage
        for x, y in grid:
            # Get bounds
            min_y, max_y = x_to_y_bounds[x]
            min_x, max_x = y_to_x_bounds[y]
            
            # Check if surrounded: min_y < y < max_y, min_x < x < max_x
            if min_y < y < max_y and min_x < x < max_x:
                count += 1
        
        return count



