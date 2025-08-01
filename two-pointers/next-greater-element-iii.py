class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        pivot = -1

        for i in range(len(digits)-2, -1, -1):
            if digits[i] < digits[i+1]:
                pivot = i
                break

        if pivot == -1: return -1

        for j in range(len(digits) - 1, pivot, - 1):
            if digits[j] > digits[pivot]:
                digits[j], digits[pivot] = digits[pivot], digits[j]
                break
        
        digits[pivot + 1:] = digits[pivot + 1:][::-1]
        res = int("".join(digits))

        return res if res <= 2**31 -1 else -1



