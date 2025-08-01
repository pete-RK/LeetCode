class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return -1
        heap = []

        for row in matrix:
            for num in row:
                if len(heap) < k:
                    heappush(heap, -num)
                elif -num > heap[0]:
                    heappushpop(heap, -num)
        
        return -heap[0]


