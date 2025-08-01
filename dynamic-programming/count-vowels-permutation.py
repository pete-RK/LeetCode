class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1,1,1,1,1

        for _ in range(1, n):
            a1 = e
            e1 = (a+i)%MOD
            i1 = (a+e+o+u)%MOD
            o1 = (i+u)%MOD
            u1 = a

            a, e, i, o, u = a1, e1, i1, o1, u1
        
        return (a+e+i+o+u)%MOD


        

        