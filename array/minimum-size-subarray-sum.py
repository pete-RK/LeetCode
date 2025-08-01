class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                min_len = min(min_len, r-l+1)
                curr -= nums[l]
                l += 1
        
        return min_len if min_len != float("inf") else 0

        
        

        
