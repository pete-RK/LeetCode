class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        nodes = defaultdict(list)

        def bfs(src):
            queue = deque()
            visited = set()
            queue.append(src)

            while queue:
                node = queue.popleft()
                visited.add(node)

                for des in nodes[node]:
                    if des not in visited:
                        queue.append(des)
            
            return len(visited) == n

        for t, src, dest in logs:
            nodes[src].append(dest)
            nodes[dest].append(src)

            if bfs(src):
                return t
        
        return -1

        