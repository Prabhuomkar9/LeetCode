class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0] + list(accumulate(travel))

        ans = len("".join(garbage))
        xIdx = {"M": 0, "G": 0, "P": 0}
        i = len(garbage) - 1

        while i >= 0 and xIdx["M"] * xIdx["G"] * xIdx["P"] == 0:
            for c in "MGP":
                if c in garbage[i]:
                    xIdx[c] = max(xIdx[c], i)

            i -= 1

        for idx in xIdx.values():
            ans += prefix[idx]

        return ans
