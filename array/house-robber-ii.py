class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1 or len(nums) == 2: return max(nums)


        def rob2(nums):
            prev2, prev1 = nums[0], max(nums[1], nums[0])

            for i in range(2, len(nums)):
                temp = max(prev1, prev2+nums[i])
                prev2 = prev1
                prev1 = temp
            
            return prev1
        
        return max(rob2(nums[:-1]), rob2(nums[1:]))


