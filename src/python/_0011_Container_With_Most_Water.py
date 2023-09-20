class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        width = len(height) - 1
        l, r = 0, width

        while l < r:
            if height[l] < height[r]:
                vol = height[l] * width
                l += 1
            else:
                vol = height[r] * width
                r -= 1

            width -= 1

            if vol > ans:
                ans = vol

        return ans
