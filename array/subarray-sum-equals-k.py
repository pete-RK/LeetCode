class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, count = 0, 0
        prefix = defaultdict(int)
        prefix[0] += 1

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]
            
            prefix[prefix_sum] += 1
        
        return count


