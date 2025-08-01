class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])
        while n > 2:
            leaves_count = len(leaves)
            n -= leaves_count

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for nei in adjacency_list[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)
        
        return list(leaves)
