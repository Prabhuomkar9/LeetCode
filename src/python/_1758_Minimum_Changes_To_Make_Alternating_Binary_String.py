class Solution:
    def minOperations(self, s: str) -> int:
        b = len(s) // 2
        a = len(s) - b

        zero = 0
        one = 0

        flag = True

        for c in s:
            if flag:
                zero += c == "0"
            else:
                one += c == "1"
            flag = not flag

        return min(a + b - zero - one, zero + one)
