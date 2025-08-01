class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [x for x in range(1, 11)]
        res = []

        def dfs(ind, curr):
            if ind >= len(nums):
                return

            if sum(curr) == n and len(curr) == k:
                res.append(curr.copy())
                return
            
            dfs(ind+1, curr + [nums[ind]])
            dfs(ind+1, curr)
        
        dfs(0, [])

        return res


        