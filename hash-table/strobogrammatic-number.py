class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map = {
            "1" : "1",
            "6" : "9",
            "9" : "6",
            "8" : "8",
            "0" : "0"
        }
        l, r = 0, len(num)-1

        while l <= r:
            if num[l] not in map or map[num[l]] != num[r]: return False
            l += 1
            r -= 1
        return True