class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for src, des in edges:
            adj[src].append(des)
            adj[des].append(src)

        visited = set()
        queue = deque([(0, -1)])
        while queue:
            node, src = queue.popleft()
            visited.add(node)
            
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, node))
                elif src != nei:
                    return False

        if len(visited) != n:
            return False
        return True
