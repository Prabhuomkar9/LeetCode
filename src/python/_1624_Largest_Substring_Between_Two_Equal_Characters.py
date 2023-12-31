class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        position = {}

        for i, c in enumerate(s):
            if c in position:
                ans = max(ans, i - position[c])
            else:
                position[c] = i + 1

        return ans
