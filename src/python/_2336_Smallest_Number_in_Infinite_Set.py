class SmallestInfiniteSet:
    def __init__(self):
        self.small = 1
        self.added = []
        self.seen = set()

    def popSmallest(self) -> int:
        if self.added:
            smallest = heapq.heappop(self.added)
            self.seen.remove(smallest)
            return smallest

        self.small += 1
        return self.small - 1

    def addBack(self, num: int) -> None:
        if num < self.small and num not in self.seen:
            self.seen.add(num)
            heapq.heappush(self.added, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
