class Solution:
    def countHousePlacements(self, n: int) -> int:
        curr = 1
        adder = 1

        for i in range(n):
            curr, adder = adder, (curr + adder) % (10**9 + 7)

        return (adder**2) % (10**9 + 7)
