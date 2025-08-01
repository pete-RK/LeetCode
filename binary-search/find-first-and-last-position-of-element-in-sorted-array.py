class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            return l
        
        def find_right():
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return r
        
        left = find_left()
        if left not in range(len(nums)) or nums[left] != target: return [-1, -1]
        right = find_right()
        return [left, right]