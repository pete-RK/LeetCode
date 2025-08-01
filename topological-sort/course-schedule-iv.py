class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if numCourses < 0 or prerequisites is None or queries is None:
            return []
        
        # Initialize adjacency list for directed graph
        graph = defaultdict(list)
        for prerequisite, course in prerequisites:
            if 0 <= prerequisite < numCourses and 0 <= course < numCourses:
                graph[prerequisite].append(course)
        
        # Shared memoization cache for DFS results
        memo = {}  # (node, dest) -> bool
        
        def checkPrereqs(source: int, destination: int) -> bool:
            # Memoized result
            if (source, destination) in memo:
                return memo[(source, destination)]
            
            # Base case: direct match
            if source == destination:
                memo[(source, destination)] = True
                return True
            
            # DFS to find path to destination
            for neighbor in graph[source]:
                if checkPrereqs(neighbor, destination):
                    memo[(source, destination)] = True
                    return True
            
            # No path found
            memo[(source, destination)] = False
            return False
        
        # Process each query
        results = []
        for src, dest in queries:
            if 0 <= src < numCourses and 0 <= dest < numCourses:
                results.append(checkPrereqs(src, dest))
            else:
                results.append(False)  # Invalid query
        
        return results
            

            


            
        
