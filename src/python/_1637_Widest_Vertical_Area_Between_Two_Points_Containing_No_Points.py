class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted({x for x, _ in points})

        return max([0] + [b - a for a, b in zip(x, x[1:])])
