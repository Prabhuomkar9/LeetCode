class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for v in freq.values():
            if v == 1:
                return -1

            ans += v // 3 + (v % 3 != 0)

        return ans
