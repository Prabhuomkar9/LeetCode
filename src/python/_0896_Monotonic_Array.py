class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False
        isDecreasing = False

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            elif nums[i - 1] < nums[i]:
                isIncreasing = True
            else:
                isDecreasing = True

            if isIncreasing and isDecreasing:
                return False

        return True
