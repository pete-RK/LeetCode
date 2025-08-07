class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        print(count)
        return count == numCourses

        
