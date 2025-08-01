class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])
        
        max_prob = [-math.inf]*n
        max_prob[start_node] = 1.00

        heap = [(-1.00, start_node)]

        while heap:
            prob, node = heappop(heap)
            if -prob < max_prob[node]: continue
            if node == end_node:
                return -prob
            
            for dest, p in graph[node]:
                new_prob = -prob * p
                if new_prob > max_prob[dest]:
                    max_prob[dest] = new_prob
                    heappush(heap, (-new_prob, dest))
        
        return 0.00
            



