class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                val = deque()
                while stack[-1] != '[':
                    val.appendleft(stack.pop())
                stack.pop()
                num = deque()
                while stack and stack[-1].isdigit():
                    num.appendleft(stack.pop())
                stack.append(int(''.join(num)) * ''.join(val))
        return ''.join(stack)
