class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def check(speed):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + speed - 1) // speed  
                if total_hours > h: 
                    return False
            return total_hours <= h

        while l < r:
            mid = l + (r-l)//2

            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
