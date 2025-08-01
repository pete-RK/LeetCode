class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(ind, curr):
            res.append(curr.copy())      
                      
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                    
                backtracking(i+1, curr +[nums[i]])
                
        
        backtracking(0, [])
        return res