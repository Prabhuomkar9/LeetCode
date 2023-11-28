class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
            elif zeroCount > 0:
                nums[i - zeroCount], nums[i] = num, 0
