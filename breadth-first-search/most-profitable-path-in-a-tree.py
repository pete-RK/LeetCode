class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        bob_dist = [-1] * len(amount)
        path = []

        def fill_bob(node, parent):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fill_bob(neighbor, node):
                        return True
                    path.pop()

        fill_bob(bob, -1)

        for i, node in enumerate(path):
            bob_dist[node] = i
        
        def alice_dfs(node, parent, curr, dist):
            if bob_dist[node] == -1 or bob_dist[node] > dist:
                curr += amount[node]
            elif bob_dist[node] == dist:
                curr += amount[node] // 2
            return curr if len(graph[node]) == 1 and node != 0 else max(alice_dfs(neighbor, node, curr, dist + 1) for neighbor in graph[node] if neighbor != parent)

        return alice_dfs(0, -1, 0, 0)


        
