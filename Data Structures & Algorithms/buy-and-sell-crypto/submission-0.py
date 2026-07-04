class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for j in range(len(prices)):
            sell = prices[j]
            if sell <= buy:
                buy = sell
            else:
                profit = max(sell - buy, profit)
        return profit