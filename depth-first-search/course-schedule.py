class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses < 0 or prerequisites is None:
            return False
        if numCourses == 0 or not prerequisites:
            return True
        graph = defaultdict(list)
        indegree = [0] * numCourses
        queue = []
        count = 1

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.pop(0)
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    del indegree[nei]
        
        return count == numCourses

        
