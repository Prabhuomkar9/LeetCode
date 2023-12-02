class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0

        for c1, c2 in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            carry += int(c1) + int(c2)
            ans = f"{carry % 2}" + ans
            carry //= 2

        if carry:
            ans = "1" + ans

        return ans
