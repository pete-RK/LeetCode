class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0

        for sell in prices[1:]:
            if buy < sell:
                result = max(result, sell - buy)
            else:
                buy = sell
        
        return result
        



        