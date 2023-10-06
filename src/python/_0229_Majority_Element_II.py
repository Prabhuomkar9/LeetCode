class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lmt = len(nums) // 3
        ans = []

        for num in set(nums):
            if nums.count(num) > lmt:
                ans.append(num)

        return ans
