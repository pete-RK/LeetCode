class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        
        def find_boundaries(arr):
            max_seen = arr[0]
            right_boundary = -1
            for i in range(1, len(arr)):
                if arr[i] < max_seen:
                    right_boundary = i
                max_seen = max(max_seen, arr[i])
            
            min_seen = arr[-1]
            left_boundary = len(arr)
            for i in range(len(arr) - 2, -1, -1):
                if arr[i] > min_seen:
                    left_boundary = i
                min_seen = min(min_seen, arr[i])
            
            if right_boundary >= left_boundary:
                return right_boundary - left_boundary + 1
            return 0

        res = []
        for i in range(len(nums) - k + 1):
            curr = nums[i:i+k]
            res.append(find_boundaries(curr))
        
        return res
