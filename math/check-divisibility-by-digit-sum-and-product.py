class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_str = str(n)
        pdt, add = 1, 0

        for x in n_str:
            pdt *= int(x)
            add += int(x)

        return n % (pdt + add) == 0