class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        prev2, prev1 = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            temp = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = temp
        
        return prev1
