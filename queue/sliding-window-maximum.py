class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_values = []
        q = deque()

        for ind, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if ind >= k and nums[ind - k] == q[0]:
                q.popleft()
            
            if ind >= k - 1:
                max_values.append(q[0])
        
        return max_values

