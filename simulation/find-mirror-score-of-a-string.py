class Solution:
    def calculateScore(self, s: str) -> int:
        ords = defaultdict(list)
        res = 0

        for i, c in enumerate(s):
            check = ord(c) - ord('a')
            if (25 - check) in ords:
                j = ords[25-check].pop()
                if not ords[25-check]:
                    del ords[25-check]
                res += i - j
            else:
                ords[check].append(i)
        
        return res
            






