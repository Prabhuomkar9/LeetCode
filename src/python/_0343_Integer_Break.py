class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        if n == 3:
            return 2

        totalPow = (n + 2) // 3
        twoPow = (3 - (n % 3)) % 3
        threePow = totalPow - twoPow

        return (3**threePow) * (2**twoPow)
