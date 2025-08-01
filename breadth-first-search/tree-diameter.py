class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(edges) + 1
        seen = set()
        self.ans = 0

        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node):
            seen.add(node)
            max1, max2, res = 0, 0, 0

            for nei in graph[node]:
                if nei not in seen:
                    res = dfs(nei)
                
                if res > max1:
                    max1, max2 = res, max1
                elif res > max2:
                    max2 = res
                
                self.ans = max(self.ans, max1 + max2)
            return 1 + max1
        
        dfs(0)
        return self.ans
        


            


            

