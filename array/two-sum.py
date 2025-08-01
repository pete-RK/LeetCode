class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = defaultdict(int)

        for ind, num in enumerate(nums):
            if num in cache:
                return [ind, cache[num]]
            cache[target - num] = ind
        
        
        

        