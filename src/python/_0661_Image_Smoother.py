class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i, row in enumerate(img):
            for j, cell in enumerate(row):
                d = 1
                s = cell

                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n:
                        d += 1
                        s += img[x][y]

                ans[i][j] = s // d

        return ans
