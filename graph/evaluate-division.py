class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))          
            graph[b].append((a, 1.0 / value))
        
        def dfs(start, end, visited, product):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return product
            visited.add(start)
            for neighbor, value in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited, product * value)
                    if result != -1.0:
                        return result
            return -1.0
        
        results = []
        for x, y in queries:
            result = dfs(x, y, set(), 1.0)
            results.append(result)
        
        return results

