class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = -1
        prefix_sum = 0
        count = 0

        for ind, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum - k in prefix:
                count = max(count , ind - prefix[prefix_sum - k])
            
            if prefix_sum not in prefix:
                prefix[prefix_sum] = ind
        
        return count
            
