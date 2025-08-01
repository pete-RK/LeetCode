class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        times = [math.inf]*n
        ways = [0]*n
        MOD = 10**9+7

        times[0] = 0
        ways[0] = 1
        for src, dest, time in roads:
            graph[src].append([dest, time])
            graph[dest].append([src, time])
        heap = [(0, 0)]
        min_val, min_count = math.inf, 0

        while heap:
            time, node = heappop(heap)
            if time > times[node]: continue
            
            for dest, ti in graph[node]:
                new_time = time + ti
                if new_time < times[dest]:
                    times[dest] = new_time
                    ways[dest] = ways[node]
                    heappush(heap, (new_time, dest))
                elif new_time == times[dest]:
                    ways[dest] = (ways[dest] + ways[node]) % MOD

        return ways[-1]

                
