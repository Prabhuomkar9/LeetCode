class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dps(open, close):
            if open > n or close > open:
                return

            if open == close == n:
                res.append("".join(stack))
                return

            stack.append("(")
            dps(open + 1, close)
            stack.pop()

            stack.append(")")
            dps(open, close + 1)
            stack.pop()

        dps(0, 0)
        return res
