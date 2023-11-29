class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     ans = 0

    #     while n:
    #         ans += n & 1
    #         n >>= 1

    #     return ans

    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            n &= n - 1
            ans += 1

        return ans
