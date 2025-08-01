class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0]* n
        queue = deque()

        for prev, next in relations:
            graph[prev-1].append(next-1)
            indegree[next-1] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append((i, 1))

        max_level, toposort = 0, []
        while queue:
            node, level = queue.popleft()
            max_level = max(max_level, level)
            toposort.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append((nei, level+1))
        
        return max_level if len(toposort) == n else -1
        

            




        
