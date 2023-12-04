class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                ans = max(ans, ord(num[i]) - ord("0"))

        return "" if ans == -1 else f"{ans}" * 3
