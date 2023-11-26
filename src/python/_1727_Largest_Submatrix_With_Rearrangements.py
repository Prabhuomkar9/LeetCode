class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        ans = 0
        height = [0 for _ in range(n)]

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                height[j] = (height[j] * val) + val

            for j, val in enumerate(sorted(height)):
                ans = max(ans, val * (n - j))

        return ans
