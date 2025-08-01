class Solution:
    def coloredCells(self, n: int) -> int:
        total = 0

        for i in range(n):
            total += (2 ** i + 1)* 2
        
        total -= (2**n +1)

        return total