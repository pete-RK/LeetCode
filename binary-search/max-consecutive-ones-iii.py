class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, max_len = 0, 0
        check = 0

        for right in range(len(nums)):
            if nums[right] == 0: check += 1
            while left <= right and check > k:
                if nums[left] == 0:
                    check -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
