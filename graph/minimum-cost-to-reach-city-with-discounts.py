class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)

        for src, dest, toll in highways:
            graph[src].append([dest, toll])
            graph[dest].append([src, toll])
        
        visited = {}
        heap = [(0, 0, discounts)]

        while heap:
            cost, node, dis = heappop(heap)
            if node in visited and dis <= visited[node]: continue
            if node == n-1: return cost
            
            visited[node] = dis 
            for dest, toll in graph[node]:
                if dis > 0:
                    heappush(heap, (toll // 2 + cost, dest, dis-1))
                heappush(heap, (toll + cost, dest, dis))
        return -1



            