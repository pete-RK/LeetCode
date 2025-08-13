class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        ans = [n+1, n+1]


        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        def get_mindistance(node):
            heap = [(0, node)]
            seen = set()
            min_distances = [math.inf]*n
            min_distances[node] = 0

            while heap:
                dist, node = heappop(heap)
                seen.add(node)

                if dist > min_distances[node]:
                    continue
                
                for v, w in graph[node]:
                    new_dist = dist + w
                    if new_dist < min_distances[v]: 
                        min_distances[v] = new_dist
                        if new_dist <= distanceThreshold:
                            heappush(heap, (new_dist, v))
            return len(seen) - 1
        
        for i in range(n):
            check = get_mindistance(i)
            if check < ans[1]:
                ans[1] = check
                ans[0] = i
            elif check == ans[1]:
                ans[0] = max(ans[0], i)
            
        return ans[0]



                
