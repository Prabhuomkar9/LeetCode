class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m - 1

        return l + k
