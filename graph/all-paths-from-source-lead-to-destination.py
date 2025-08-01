class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node,path):
            if not graph[node]:
                if node==destination:
                    return True
                else:
                    return False
                    
            if node in memo: 
                return memo[node]

            path.add(node)

            for nei in graph[node]:
                if nei in path:
                    return False
                else:
                    if not dfs(nei,path):
                        memo[node] = False
                        return False

            path.remove(node)
            memo[node] = True
            return True
        
        graph=defaultdict(list)
        for src,dst in edges:
            graph[src].append(dst)
        memo=defaultdict(bool)   

        return dfs(source,set())





