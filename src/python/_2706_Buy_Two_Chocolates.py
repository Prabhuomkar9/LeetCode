class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first, second = float("infinity"), float("infinity")

        for price in prices:
            if price < first:
                first, second = price, first
            elif price < second:
                second = price

        if money < first + second:
            return money

        return money - first - second
