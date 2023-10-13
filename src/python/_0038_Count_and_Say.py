class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        ans = ""
        lastAns = self.countAndSay(n - 1)
        seenCh = lastAns[0]
        freq = 0

        for ch in lastAns:
            if seenCh == ch:
                freq += 1
            else:
                ans += f"{freq}{seenCh}"
                freq = 1
                seenCh = ch

        ans += f"{freq}{seenCh}"

        return ans
