class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        horizontal = abs(fx - sx)
        vertical = abs(fy - sy)
        need = max(horizontal, vertical)

        if need > 0:
            return need <= t
        else:
            return t != 1
