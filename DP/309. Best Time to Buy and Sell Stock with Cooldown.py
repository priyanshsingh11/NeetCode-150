class Solution:
    def maxProfit(self, prices):
        buy, sell, prev_sell = float('-inf'), 0, 0
        
        for price in prices:
            buy = max(buy, prev_sell - price)
            prev_sell = sell
            sell = max(sell, buy + price)
        
        return sell
