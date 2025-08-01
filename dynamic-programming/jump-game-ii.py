class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        dp[0] = 0

        for i in range(len(nums)-1):
            for j in range(i, min(len(nums), i+nums[i]+1)):
                dp[j] = min(dp[j], 1+dp[i])
        
        return dp[-1]



        