class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = [0] * len(grid)
        col = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row[i] += grid[i][j]
                col[j] += grid[i][j]

        return [
            [
                2 * row[i] + 2 * col[j] - len(grid) - len(grid[0])
                for j in range(len(grid[0]))
            ]
            for i in range(len(grid))
        ]
