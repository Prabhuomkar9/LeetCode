class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0

        for cookie in s:
            if i >= len(g):
                break

            if g[i] <= cookie:
                i += 1

        return i
