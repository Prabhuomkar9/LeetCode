class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while a or b or c:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1
            if (bitA | bitB) != bitC:
                if bitC == 0:
                    count += bitA + bitB
                else:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1

        return count
