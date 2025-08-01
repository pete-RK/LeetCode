class Solution:
    def tribonacci(self, n: int) -> int:
        t1, t2, t3 = 0, 1, 1
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        for _ in range(n - 2):
            curr = t1 + t2 + t3
            t1, t2, t3 = t2, t3, curr
        
        return t3