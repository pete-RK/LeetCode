class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dest, time in times:
            graph[src-1].append([dest-1, time])
        visited = set()
        distances = [math.inf]*n
        distances[k-1] = 0 
        heap = [(0, k-1)]

        while heap:
            dist, node = heappop(heap)
            visited.add(node)

            if len(visited) == n:
                return dist
            
            if distances[node] < dist:
                continue
            
            for dest, time in graph[node]:
                new_time = time + dist
                if new_time < distances[dest]:
                    distances[dest] = new_time
                    heappush(heap, (new_time, dest))
        
        return -1





