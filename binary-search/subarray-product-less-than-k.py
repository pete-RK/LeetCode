class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, left = 0, 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]

            while left <= right and prod >= k:
                prod = prod // nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
