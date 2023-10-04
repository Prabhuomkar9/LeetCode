class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for c in columnTitle:
            digit = ord(c) - ord("A") + 1
            ans = (ans * 26) + digit

        return ans
