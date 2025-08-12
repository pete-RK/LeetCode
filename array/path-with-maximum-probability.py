class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], src: int, dest: int) -> float:
        graph = defaultdict(list)

        for ind, curr in enumerate(edges):
            u, v = curr[0], curr[-1]
            graph[u].append([v, succProb[ind]])
            graph[v].append([u, succProb[ind]])
        
        heap = [(-1, src)]
        probs = [-math.inf] * n
        probs[src] = 1

        while heap:
            prob, node = heappop(heap)

            if probs[node] < -prob:
                continue
            
            if node == dest:
                return -prob
            
            for nei, p in graph[node]:
                new_prob = -prob * p
                if new_prob > probs[nei]:
                    probs[nei] = new_prob
                    heappush(heap, (-new_prob, nei))
        
        return 0.00
            



