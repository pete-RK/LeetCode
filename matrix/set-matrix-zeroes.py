class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i in rows or j in cols:
                    nums[i][j] = 0
     

        