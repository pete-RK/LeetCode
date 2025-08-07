class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        seen = set()

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        

        def dfs(node):
            seen.add(node)
            count = 1

            for nei in graph[node]:
                if nei not in seen:
                    count += dfs(nei)
            
            return count
        
        ans = total = 0
        for i in range(n):
            if i not in seen:
                size = dfs(i)
                ans += size * total
                total += size
        
        return ans