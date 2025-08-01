class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0]

        for nums in intervals[1:]:
            if curr[-1] >= nums[0]:
                curr[-1]= max(curr[-1], nums[1])
            else:
                res.append(curr)
                curr = nums
        
        res.append(curr)
        return res