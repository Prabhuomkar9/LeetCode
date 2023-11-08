class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rotten = deque()
        fresh = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    rotten.append((i, j))
                elif cell == 1:
                    fresh += 1

        t = 0

        while rotten and fresh > 0:
            t += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += x
                    dy += y

                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                        fresh -= 1
                        grid[dx][dy] = 2
                        rotten.append((dx, dy))

        return t if fresh == 0 else -1
