class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        ans = 0

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 0
            ans += seen[num]

        return ans
