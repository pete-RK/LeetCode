class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        q_sum, min_length = 0, float('inf')

        for ind, num in enumerate(nums):
            q_sum += num
            if q_sum >= k:
                min_length = min(min_length, ind+1)
            
            while q and q_sum - q[0][0] >= k:
                _, end_ind = q.popleft()
                min_length = min(min_length, ind - end_ind)
            
            while q and q[-1][0] > q_sum:
                q.pop()
            q.append((q_sum , ind))
            
        return min_length if min_length != float('inf') else -1
            


