class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        count, curr = 0, 0

        for num in nums[:-1]:
            curr += num
            if curr >= total - curr:
                count += 1
        
        return count
