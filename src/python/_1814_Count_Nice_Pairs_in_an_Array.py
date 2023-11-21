class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)

        for num in nums:
            hashValue = num - int(str(num)[::-1])
            ans += freq[hashValue]
            freq[hashValue] += 1

        return ans % (10**9 + 7)
