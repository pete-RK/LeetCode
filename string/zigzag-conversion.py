class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        ind, d = 0, 1
        strings = ["" for _ in range(numRows)]

        for char in s:
            strings[ind] += char
            if ind == 0: d = 1
            elif ind == numRows -1: d = -1
            ind += d
        
        
        return ''.join(strings)

