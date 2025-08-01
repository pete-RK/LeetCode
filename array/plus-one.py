class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''

        for x in digits:
            res += str(x)
        res = str(int(res) + 1)

        return [int(i) for i in res]