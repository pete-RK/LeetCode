class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)
        if total % 2 != 0: return False
        k = total // 2

        dp = [[False]*(k+1) for _ in range(n)]
        for i in range(n): dp[i][0] = True
        if nums[0] <= k: dp[0][nums[0]] = True

        for ind in range(1, n):
            for target in range(1, k+1):
                take = False
                if nums[ind] <= target:
                    take = dp[ind-1][target - nums[ind]]
                no_take = dp[ind-1][target]

                dp[ind][target] = take or no_take

        return dp[n-1][k]




