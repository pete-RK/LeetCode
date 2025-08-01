class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.rstrip().split(" ")

        return len(strings[-1])
