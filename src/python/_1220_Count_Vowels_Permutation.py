class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(n - 1):
            A = e
            E = (a + i) % MOD
            I = (a + e + o + u) % MOD
            O = (i + u) % MOD
            U = a

            a, e, i, o, u = A, E, I, O, U

        return (a + e + i + o + u) % MOD
