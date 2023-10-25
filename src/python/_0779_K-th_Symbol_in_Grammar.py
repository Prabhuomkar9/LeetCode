class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(i, j):
            if i == 0:
                return 0

            if i == 1:
                return j

            divisor = 2 ** (i - 1)

            if divisor > j:
                return dfs(i - 1, j)
            elif dfs(i - 1, j % divisor) == 0:
                return 1
            else:
                return 0

        return dfs(n - 1, k - 1)
