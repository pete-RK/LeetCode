class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub, min_sub = float('-inf'), float('inf')
        total_sum = 0
        min_curr, max_curr = 0 , 0

        for num in nums:
            max_curr = max(num, max_curr+num)
            min_curr = min(num, min_curr+num)

            max_sub = max(max_curr, max_sub)
            min_sub = min(min_curr, min_sub)

            total_sum += num
        
        return max_sub if max_sub < 0 else max(max_sub, total_sum - min_sub)

