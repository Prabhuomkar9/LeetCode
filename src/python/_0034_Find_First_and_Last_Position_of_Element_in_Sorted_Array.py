class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = [-1, -1]

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                first, last = m, m

                while first >= 0 and nums[first] == target:
                    first -= 1

                while last < len(nums) and nums[last] == target:
                    last += 1

                ans[0] = first + 1
                ans[1] = last - 1

                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return ans
