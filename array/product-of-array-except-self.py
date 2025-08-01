class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev, next = [1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            prev[i] = nums[i-1]*prev[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            next[j] = nums[j+1]*next[j+1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(next[i]*prev[i]) 
        
        return ans

        