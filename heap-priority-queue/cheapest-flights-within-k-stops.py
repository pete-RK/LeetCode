class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, dst: int, k: int) -> int:
        visited = {}
        graph = defaultdict(list)
        for src, dest, pr in flights:
            graph[src].append([dest, pr])
        heap = [(0, 0, source)]

        while heap:
            price, stops, node = heappop(heap)
            if stops > k+1 : continue
            if node == dst: return price
            if node in visited and visited[node] == stops:
                continue
            visited[node] = stops
            for dest, pr in graph[node]:
                new_price = pr + price
                if dest not in visited or visited[dest] > stops:
                    heappush(heap, (new_price, stops+1, dest))
        
        return -1




            


            