class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        seats = 0

        l = None

        for r, val in enumerate(corridor):
            if val == "P":
                continue

            seats += 1

            if l and seats == 1:
                ans *= r - l
            elif seats == 2:
                l = r
                seats = 0

        if not l or seats == 1:
            return 0

        return ans % (10**9 + 7)
