"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        queue = deque([id])

        total = 0
        for emp in employees:
            graph[emp.id] += [emp.importance, emp.subordinates]
        
        while queue:
            node = queue.popleft()
            total += graph[node][0]

            for nei in graph[node][1]:
                queue.append(nei)
        
        return total

