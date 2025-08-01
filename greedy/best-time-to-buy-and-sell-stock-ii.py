class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_pr = 0

        for sell in prices[1:]:
            if sell > buy:
                max_pr += sell - buy
            buy = sell
        
        return max_pr