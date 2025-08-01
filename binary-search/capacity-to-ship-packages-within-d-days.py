class Solution:
    def shipWithinDays(self, nums: List[int], d: int) -> int:
        l, r = max(nums), sum(nums)

        def check(we):
            curr = 0
            days = 1
            for c in nums:
                curr += c
                
                if curr > we:
                    days += 1
                    curr = c

            return days <= d
        
        while l < r:
            mid = l + (r-l)//2

            if check(mid): 
                r = mid
            else:
                l = mid + 1
        
        return l