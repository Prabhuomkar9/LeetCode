class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for j in range(1, numRows):
            res.append([1] + [res[-1][i - 1] + res[-1][i] for i in range(1, j)] + [1])

        return res
