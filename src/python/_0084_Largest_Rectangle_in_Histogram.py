class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        end = len(heights)
        stack = []

        for index, height in enumerate(heights):
            last = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                area = max(area, (index - i) * h)
                last = i
            stack.append((last, height))

        for s in stack:
            i, h = s
            area = max(area, (end - i) * h)

        return area
