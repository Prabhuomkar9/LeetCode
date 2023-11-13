class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        candidates = defaultdict(int)
        ans = 0

        for num in nums:
            candidate = k - num

            if candidates[candidate]:
                ans += 1
                candidates[candidate] -= 1
            else:
                candidates[num] += 1

        return ans
