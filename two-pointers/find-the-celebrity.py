# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0

        for i in range(n):
            if knows(celeb, i):
                celeb = i
        
        for mem in range(n):
            if mem != celeb and (knows(celeb, mem) or not knows(mem, celeb)):
                return -1
        
        return celeb
