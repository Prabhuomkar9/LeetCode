class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ans = []
        potions.sort()

        for spell in spells:
            left = bisect_left(potions, ceil(success / spell))
            ans.append(len(potions) - left)

        return ans
