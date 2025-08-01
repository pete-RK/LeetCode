class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        total = 0

        for num in nums:
            if total < 0:
                total = 0
            
            total += num
            curr = max(curr, total)
        
        return curr