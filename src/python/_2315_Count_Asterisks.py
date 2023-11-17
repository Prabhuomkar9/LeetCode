class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = False
        ans = 0

        for c in s:
            if c == "|":
                pair = not pair
            elif not pair and c == "*":
                ans += 1

        return ans
