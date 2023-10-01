class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, r = 0, 46340

        while l <= r:
            m = (l + r) // 2
            val = m * m

            if val == x:
                return m

            if val < x:
                l = m + 1
            else:
                r = m - 1

        return r
