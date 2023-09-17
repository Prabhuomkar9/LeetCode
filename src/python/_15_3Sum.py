class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        size = len(nums)
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = size - 1
            while l < r:
                value = nums[l] + nums[r]
                if value < -n:
                    l += 1
                elif value > -n:
                    r -= 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans
