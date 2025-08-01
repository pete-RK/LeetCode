class Solution:
    def findMissingAndRepeatedValues(self, nums: List[List[int]]) -> List[int]:
        n = len(nums) ** 2
        total = (n * (n+1))/2
        nums_set = set()

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j] in nums_set:
                    a = nums[i][j]
                nums_set.add(nums[i][j])
        
        b = int(total - sum(list(nums_set)))

        return [a, b]