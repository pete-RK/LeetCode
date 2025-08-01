class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        ind = 0

        for color in range(3):
            freq = counter.get(color, 0)
            nums[ind:ind+freq] = [color]*freq
            ind += freq
        
        