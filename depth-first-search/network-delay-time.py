class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append([v, w])
        
        heap = [(0, k)]
        min_times = [math.inf]*n
        min_times[k-1] = 0
        count = set()

        while heap:
            time, node = heappop(heap)
            count.add(node)

            if time > min_times[node-1]:
                continue

            if len(count) == n:
                return time

            for v, w in graph[node]:
                new_time = w + time
                if new_time < min_times[v-1]:
                    min_times[v-1] = new_time
                    heappush(heap, (new_time, v))


        return -1
        






