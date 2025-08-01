class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)

        while len(sticks) >= 2:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            cost += first + second
            heapq.heappush(sticks, first+second)
        
        return cost