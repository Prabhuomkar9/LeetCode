class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        i = 0
        j = 1
        k = 1

        for _ in range(n - 2):
            i, j, k = j, k, i + j + k

        return k
