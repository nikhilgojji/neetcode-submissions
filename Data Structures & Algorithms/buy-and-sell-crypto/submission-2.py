class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for stock in prices:
            minPrice = min(minPrice, stock)
            profit = max(profit, stock - minPrice)
        return profit
        