class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = deque()
        total = 0
        ans = 0

        for ele in arr:
            i = 1
            while stk and stk[-1][0] >= ele:
                e, c = stk.pop()
                total -= e * c
                i += c
            stk.append((ele, i))
            total += ele * i
            ans += total

        return ans % (10**9 + 7)
