class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        lowest_price = prices[0]
        for price in prices:
            profits = max(profits,price - lowest_price)
            lowest_price = min(price,lowest_price)
        return profits