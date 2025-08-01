class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        kill_list = set()
        nodes = defaultdict(list)

        for i in range(len(pid)):
            nodes[ppid[i]].append(pid[i])
        queue = deque([kill])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                kill_list.add(node)

                for nei in nodes[node]:
                    queue.append(nei)
        
        return list(kill_list)

