class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(curr_list, index, prev):
            if len(curr_list) > 1:
                res.append(curr_list.copy())

            seen=set()

            for i in range(index, len(nums)):
                if nums[i] in seen:
                    continue

                if prev <= nums[i]:
                    curr_list.append(nums[i])
                    backtracking(curr_list, i+1, nums[i])
                    curr_list.pop()
                
                seen.add(nums[i])
            
        backtracking([], 0, float('-inf'))

        return res
            

            

        