class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(ind, curr):
            if ind == len(nums) and curr == target:
                return 1
            
            if ind == len(nums):
                return 0
            
            if (ind, curr) in memo:
                return memo[(ind, curr)]
            
            add = dfs(ind+1, curr+nums[ind])
            sub = dfs(ind+1, curr-nums[ind])

            memo[(ind, curr)] = add + sub

            return memo[(ind, curr)] 

        return dfs(0, 0)


            

        