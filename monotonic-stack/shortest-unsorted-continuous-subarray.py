class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_seen = nums[0]
        right_boundary = -1
        for i in range(1, len(nums)):
            if nums[i] < max_seen:
                right_boundary = i
            else:
                max_seen = nums[i]
        min_seen = nums[-1]
        left_boundary = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > min_seen:
                left_boundary = i
            else:
                min_seen = nums[i]
        
        if right_boundary >= left_boundary:
            return right_boundary - left_boundary + 1
        else:
            return 0
