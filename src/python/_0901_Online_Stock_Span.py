class StockSpanner:
    def __init__(self):
        self.minStack = deque()

    def next(self, price: int) -> int:
        days = 1
        while self.minStack and price >= self.minStack[-1][0]:
            _, day = self.minStack.pop()
            days += day
        self.minStack.append((price, days))
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
