class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((s, i) for i, (s, _) in enumerate(intervals))
        ans = []

        for _, end in intervals:
            idx = bisect_left(starts, (end,))
            ans.append(starts[idx][1] if idx < len(starts) else -1)

        return ans
