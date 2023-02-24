# Best time to buy and sell stock 
class Solution:
    def maxProfit(self, prices):
        minPrice = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > max_profit:
                max_profit = prices[i] - minPrice

        return max_profit
