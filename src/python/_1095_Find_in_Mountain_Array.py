# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        length = mountain_arr.length()
        cache = {}

        def valAt(idx):
            if idx not in cache:
                cache[idx] = mountain_arr.get(idx)
            return cache[idx]

        l, r = 1, length - 2

        while l <= r:
            m = (l + r) // 2
            lastVal = valAt(m - 1)
            currVal = valAt(m)
            nextVal = valAt(m + 1)

            if lastVal < currVal > nextVal:
                if currVal == target:
                    return m
                peak = m
                break
            elif lastVal < currVal < nextVal:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            currVal = valAt(m)

            if currVal == target:
                return m
            elif currVal < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak + 1, length - 1

        while l <= r:
            m = (l + r) // 2
            currVal = valAt(m)

            if currVal == target:
                return m
            elif currVal < target:
                r = m - 1
            else:
                l = m + 1

        return -1
