class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for price in prices:
            if price < buyPrice:
                buyPrice = price
            elif price - buyPrice > profit:
                profit = price - buyPrice

        return profit
