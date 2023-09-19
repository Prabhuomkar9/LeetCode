class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}

        for n in nums:
            seen[n] = 1 + seen.get(n, 0)

        ans = list(seen.keys())
        ans.sort(key=lambda k: -seen[k])

        return ans[:k]
