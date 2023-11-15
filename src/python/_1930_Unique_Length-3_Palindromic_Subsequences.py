class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for c in set(s):
            l, r = s.find(c), s.rfind(c)

            if l > -1:
                count += len(set(s[l + 1 : r]))

        return count
