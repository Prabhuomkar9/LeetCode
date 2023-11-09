class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        length = 0
        lastSeen = s[0]

        for c in s:
            if c == lastSeen:
                length += 1
            else:
                ans += length * (length + 1) // 2
                lastSeen = c
                length = 1

        ans += length * (length + 1) // 2

        return ans % (10**9 + 7)
