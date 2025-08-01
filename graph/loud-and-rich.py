class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_list = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n
        ans = list(range(n))
        queue = deque()

        for rich, poor in richer:
            adj_list[rich].append(poor)
            indegree[poor] += 1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()

            for nei in adj_list[node]:
                if quiet[ans[node]] < quiet[ans[nei]]:
                    ans[nei] = ans[node]

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return ans

        

        