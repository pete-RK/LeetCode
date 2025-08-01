class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def check(max_sum):
            count = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > max_sum:
                    curr_sum = num
                    count += 1
                if count > k: return False
            
            return True
        

        while l < r:
            mid = l + (r-l)//2

            if check(mid): 
                r = mid
            else:
                l = mid + 1
        
        return l
