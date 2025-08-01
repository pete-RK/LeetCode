class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        stack = []

        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                stack.append('*')
            elif stack:
                stack.pop()
            else:
                res += s[i]
        
        return res[::-1]

            

            