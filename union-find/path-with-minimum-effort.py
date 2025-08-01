class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[math.inf] * cols for _ in range(rows)]
        dist[0][0] = 0
        DIR = [0, 1, 0, -1, 0]
        heap = [(0, 0, 0)]

        while heap:
            d, x, y = heappop(heap)
            if d > dist[x][y]: continue
            if x == rows-1 and y == cols-1:
                return d
            
            for i in range(4):
                nx, ny = x + DIR[i], y + DIR[i+1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    newDist = max(d, abs(heights[nx][ny] - heights[x][y]))
                    if dist[nx][ny] > newDist:
                        dist[nx][ny] = newDist
                        heappush(heap, (newDist, nx, ny))
        
        return -1

