class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        limit = 1

        for i in range(len(arr)):
            if arr[i] >= limit:
                limit += 1

        return limit - 1
