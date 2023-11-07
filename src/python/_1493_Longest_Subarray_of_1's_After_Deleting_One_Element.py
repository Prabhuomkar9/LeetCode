class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        zeroIndex = -1
        ans = 0

        while r < len(nums):
            if nums[r] == 0:
                ans = max(ans, r - l - 1)
                if zeroIndex >= 0:
                    l = zeroIndex + 1
                zeroIndex = r
            r += 1

        ans = max(ans, r - l - 1)

        if zeroIndex < 0:
            return len(nums) - 1
        else:
            return ans
