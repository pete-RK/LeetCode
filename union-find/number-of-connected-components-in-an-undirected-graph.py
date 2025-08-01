class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj, count, visited = defaultdict(list), 0, set()

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count



