class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 0

        ans = 0

        for val in seen.values():
            ans += (val * (val + 1)) // 2

        return ans
