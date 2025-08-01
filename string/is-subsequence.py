class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        if len(s) > len(t): return False
        i = 0

        for char in t:
            if char == s[i]:
                if i == len(s)-1:
                    return True
                i += 1
        
        return False
        