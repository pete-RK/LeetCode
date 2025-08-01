class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph) - 1

        def dfs(node, path):
            if node == n:
                res.append(list(path))
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()            
        
        dfs(0, [0])
        return res
