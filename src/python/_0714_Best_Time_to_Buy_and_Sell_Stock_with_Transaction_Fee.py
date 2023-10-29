class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        investment = float("-inf")
        profit = 0

        for price in prices:
            investment = max(investment, profit - price)
            profit = max(profit, investment + price - fee)

        return profit
