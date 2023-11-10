class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = l + (r - l) // 2
            hour = sum(ceil(pile / k) for pile in piles)

            if hour <= h:
                r = k - 1
            else:
                l = k + 1

        return l
