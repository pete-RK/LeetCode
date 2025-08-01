class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    if dist <= r1:
                        graph[i].append(j)
        
        def dfs(ind, visited):
            visited.add(ind)
            count = 1 
            for neighbor in graph[ind]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count
        
        max_detonations = 0
        for i in range(n):
            detonations = dfs(i, set())
            max_detonations = max(max_detonations, detonations)
        
        return max_detonations







            
