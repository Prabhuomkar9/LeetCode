class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = [0] * len(mat)
        col = [0] * len(mat[0])

        for i, r in enumerate(mat):
            for j, val in enumerate(r):
                if val == 1:
                    row[i] += 1
                    col[j] += 1

        ans = 0

        for i, r in enumerate(mat):
            for j, val in enumerate(r):
                if val == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1

        return ans
