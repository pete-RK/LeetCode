class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen, path = set(), set()
        safe_nodes, safe_check = [], [-1]*len(graph)

        def dfs(node):
            seen.add(node)
            path.add(node)

            for nei in graph[node]:
                if nei not in seen:
                    if dfs(nei): return True
                elif nei in path:
                    return True

            safe_check[node] = 1
            path.remove(node)
            return False
        
        for i in range(len(graph)):
            if i not in seen:
                dfs(i)
        
        for i in range(len(graph)):
            if safe_check[i] == 1:
                safe_nodes.append(i)
        
        return safe_nodes



