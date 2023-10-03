class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hashMap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res += hashMap[columnNumber % 26]
            columnNumber //= 26

        return res[::-1]
