class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        are_values_same = True
        n = 2**(n - 1)

        while n != 1:
            n //= 2
            if k > n:
                k -= n
                are_values_same = not are_values_same

        return 0 if are_values_same else 1

