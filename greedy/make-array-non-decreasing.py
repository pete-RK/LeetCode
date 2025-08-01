class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = [nums[-1]]

        for i in range(len(nums)-2, -1, -1):
            while stack and nums[i] > stack[-1]:
                stack.pop()
            
            stack.append(nums[i])
        
        return len(stack)