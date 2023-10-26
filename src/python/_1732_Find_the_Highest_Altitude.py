class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = max(0, gain[0])

        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            ans = max(ans, gain[i])

        return ans
