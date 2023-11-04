class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n // 2 + 1

        while l <= r:
            k = l + (r - l) // 2
            total = k * (k + 1) // 2

            if total == n:
                return k
            elif total < n:
                l = k + 1
            else:
                r = k - 1

        return r
