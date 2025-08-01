class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}
        m, n = len(grid), len(grid[0])

        def recursion(row, c1, c2):
            if not 0<=c1<n or not 0<=c2<n or not 0<=row<m: return -math.inf

            if row == m-1:
                if c1 == c2: return grid[row][c1]
                else: return grid[row][c1] + grid[row][c2]
            
            if (row, c1, c2) in memo: return memo[(row, c1, c2)]
            
            maxi = -math.inf
            for i1 in range(-1, 2):
                for i2 in range(-1, 2):
                    val = 0
                    if c1 == c2: val = grid[row][c1]
                    else: val = grid[row][c1] + grid[row][c2]
                    val += recursion(row+1, c1+i1, c2+i2)

                    maxi = max(maxi, val)
                    memo[(row, c1, c2)] = maxi
            
            return memo[(row, c1, c2)]
        
        return recursion(0, 0, n-1)



