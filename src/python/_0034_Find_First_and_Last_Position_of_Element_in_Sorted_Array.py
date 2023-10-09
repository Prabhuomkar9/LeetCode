class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target and (m == 0 or nums[m - 1] != nums[m]):
                start = m
                break
            elif nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target and (m == len(nums) - 1 or nums[m] != nums[m + 1]):
                end = m
                break
            elif nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        return [start, end]
