class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sum1, sum2, chunks = 0 ,0 ,0

        for ind, num in enumerate(arr):
            sum1 += ind
            sum2 += num
            if sum1 == sum2 :
                chunks += 1
        
        return chunks