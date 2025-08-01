class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        distance = [math.inf]*(n+1)

        for src, dest, dist in roads:
            graph[src].append([dest, dist])
            graph[dest].append([src, dist])
        
        heap = [(1, math.inf)]
        distance[1] = math.inf
        visited = defaultdict(int)

        while heap:
            node, dist = heappop(heap)

            if distance[node] < dist:
                continue

            for nei, d in graph[node]:
                new_dist = min(dist, d)
                if new_dist < distance[nei]:
                    distance[nei] = new_dist
                    heappush(heap, (nei, new_dist))
        
        return distance[n]
            
