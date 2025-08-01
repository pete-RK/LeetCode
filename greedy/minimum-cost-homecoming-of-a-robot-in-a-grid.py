class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res, [i,j], [x,y] = 0, startPos, homePos

        while i != x:
            i += (x-i)//abs(x-i)
            res += rowCosts[i]
        
        while j != y:
            j += (y-j)//abs(y-j)
            res += colCosts[j]
        
        return res




        

