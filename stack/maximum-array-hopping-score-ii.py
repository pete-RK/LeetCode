class Solution:
    def maxScore(self, nums: List[int]) -> int:
        stack = [(nums[-1], len(nums) - 1)]

        for i in range(len(nums)-2, -2, -1):
            if nums[i] > stack[-1][0]:
                stack.append((nums[i], i))
        
        res, j = 0, 0
        for num, ind in stack[::-1]:
            res += (ind - j) * num
            j = ind
        
        return res



