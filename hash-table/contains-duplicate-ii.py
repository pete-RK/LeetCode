class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ddict = {}

        for i, num in enumerate(nums):
            if num in ddict:
                if abs(ddict[num]-i) <= k:
                    return True
            ddict[num] = i
        print(ddict)
        return False

            