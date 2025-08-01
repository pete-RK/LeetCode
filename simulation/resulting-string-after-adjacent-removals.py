class Solution:
    def resultingString(self, s: str) -> str:
        stack = [s[0]]

        for char in s[1:]:
            if stack and (abs(ord(char) - ord(stack[-1])) == 1 or abs(ord(char) - ord(stack[-1])) == 25):
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)