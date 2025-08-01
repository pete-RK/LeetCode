class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        graph = defaultdict(set)

        for src, dest in edges:
            graph[src].add(dest)
            graph[dest].add(src)
        
        visited, res = set(), 0.
        def dfs(node, p, time):
            nonlocal res
            if time >= t:
                if node == target: res = p
                return
            visited.add(node)
            neighbors = graph[node] - visited
            for n in neighbors or [node]:
                dfs(n, p / (len(neighbors) or 1), time + 1)
        dfs(1, 1, 0)
        return res

