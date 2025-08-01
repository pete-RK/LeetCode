class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        for i in range(len(nums)-1):
            if (flag and nums[i] > nums[i+1]) or (not flag and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            flag = not flag
