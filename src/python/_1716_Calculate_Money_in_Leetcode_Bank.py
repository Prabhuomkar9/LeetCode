class Solution:
    def totalMoney(self, n: int) -> int:
        w, d = divmod(n, 7)
        return 28 * w + 7 * w * (w - 1) // 2 + d * (d + 1) // 2 + w * d
