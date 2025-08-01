class Solution:
    def findCircleNum(self, adj: List[List[int]]) -> int:
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            neighbours = adj[node-1]

            for i, nei in enumerate(neighbours):
                if nei == 1 and i+1 not in visited:
                    dfs(i+1)
            
        for ind in range(len(adj)):
            if ind+1 not in visited:
                count += 1
                dfs(ind+1)
        
        return count


