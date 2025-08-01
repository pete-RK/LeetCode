class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        
        for num in nums:
            if len(res) % 2 == 0 or num != res[-1]:
                res.append(num)
        
        return len(nums) - (len(res) - len(res) % 2)