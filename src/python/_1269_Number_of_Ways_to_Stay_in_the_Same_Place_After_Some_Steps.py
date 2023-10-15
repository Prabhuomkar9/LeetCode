class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        seen = {}

        def fn(currIdx, remain):
            if (currIdx, remain) in seen:
                return seen[(currIdx, remain)]

            if not 0 <= currIdx < arrLen:
                return 0

            if remain == 0:
                if currIdx == 0:
                    seen[(currIdx, remain)] = 1
                else:
                    seen[(currIdx, remain)] = 0
            else:
                left = fn(currIdx - 1, remain - 1)
                stay = fn(currIdx, remain - 1)
                right = fn(currIdx + 1, remain - 1)

                seen[(currIdx, remain)] = (left + stay + right) % (10**9 + 7)

            return seen[(currIdx, remain)]

        return fn(0, steps)
