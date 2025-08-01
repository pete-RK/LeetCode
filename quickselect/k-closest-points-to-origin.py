class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for point in points:
            var = (point[0] - 0)**2 + (point[1] - 0)**2
            dis = math.sqrt(var)

            heappush(heap, (dis, tuple(point)))
        
        for _ in range(k):
            dis, point = heappop(heap)
            res.append(list(point))
        
        return res