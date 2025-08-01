class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], end: List[int]) -> int:
        start, end = tuple(start), tuple(end)
        m, n = len(maze), len(maze[0])
        distances = defaultdict(lambda : float('inf'))
        distances[start] = 0

        def traverse(pos, dx, dy):
            i, j = pos
            l = 0
            while 0 <= i + dx < m and 0 <= j + dy < n and maze[i + dx][j + dy] != 1:
                i += dx
                j += dy
                l += 1
            return l, (i, j)
            
        heap = [(0, start)]
        while heap:
            current_distance, node = heapq.heappop(heap)
            if current_distance > distances[node]:
                continue
            if node == end:
                return current_distance
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                length, new_node = traverse(node, dx, dy)
                new_distance = current_distance + length
                if new_distance < distances[new_node]:
                    distances[new_node] = new_distance
                    heapq.heappush(heap, (new_distance, new_node))
        
        return -1


                
                
