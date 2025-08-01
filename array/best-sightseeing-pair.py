class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2: return sum(values)-1
        max_val, start = 0, values[0]

        for i in range(1, len(values)):
            max_val = max(max_val, start + values[i] - i)
            start = max(start, values[i] + i)
        
        return max_val



