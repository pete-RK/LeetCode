class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                if nums[mid] >= target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
