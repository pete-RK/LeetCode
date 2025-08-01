class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = max(nums)

        for num in nums:
            curr_max, curr_min = max(curr_max * num, curr_min * num, num), min(curr_max * num, curr_min * num, num)
            
            res = max(res, curr_max)
        
        return res
