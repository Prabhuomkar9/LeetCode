class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dxdy = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        Queue<int[]> rotten = new ArrayDeque<>();
        int fresh = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)
                    rotten.offer(new int[] { i, j });
                else if (grid[i][j] == 1)
                    fresh += 1;
            }
        }

        int t = 0;

        while (!rotten.isEmpty() && fresh > 0) {
            t += 1;

            int size = rotten.size();
            for (int i = 0; i < size; i++) {
                int[] xy = rotten.poll();
                int x = xy[0];
                int y = xy[1];

                for (int j = 0; j < 4; j++) {
                    int dx = x + dxdy[j][0];
                    int dy = y + dxdy[j][1];

                    if (dx < 0 || dx >= m || dy < 0 || dy >= n)
                        continue;

                    if (grid[dx][dy] == 1) {
                        fresh -= 1;
                        grid[dx][dy] = 2;
                        rotten.offer(new int[] { dx, dy });
                    }
                }
            }
        }

        if (fresh > 0)
            return -1;
        else
            return t;
    }
}
