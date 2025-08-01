class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1, s2 = set(), set()

        for num in nums:
            if num not in s1 and num not in s2:
                s1.add(num)
            else:
                s2.add(num)
        
        return (s1-s2).pop()