class Solution:
    # def minimumOneBitOperations(self, n: int) -> int:
    #     ans = 0
    #     i = 1

    #     while n:
    #         bit = n & 1
    #         n >>= 1
    #         ans = (2**i - 1) - ans if bit else ans
    #         i += 1

    #     return ans

    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0

        while n:
            ans = (n ^ (n - 1)) - ans
            n &= n - 1

        return ans
