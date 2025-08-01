class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        nums.append(math.inf)
        stack = []

        for ind, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                res[j] = ind - stack[-1] -1 if stack else ind

            stack.append(ind)

        return res



