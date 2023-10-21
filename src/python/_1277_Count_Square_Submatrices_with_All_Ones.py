class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0

        for i in range(min(m, n)):
            for j in range(m - 1, i - 1, -1):
                for k in range(n - 1, i - 1, -1):
                    count += matrix[j][k]
                    if j == i - 1 or k == i - 1:
                        continue
                    matrix[j][k] = (
                        matrix[j][k]
                        + matrix[j - 1][k]
                        + matrix[j][k - 1]
                        + matrix[j - 1][k - 1]
                    ) // 4

        return count
