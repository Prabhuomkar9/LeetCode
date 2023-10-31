class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        maxSum = float("-inf")

        for i, num in enumerate(nums):
            currSum += nums[i]
            if i >= k:
                currSum -= nums[i - k]
            if i >= k - 1:
                maxSum = max(maxSum, currSum)

        return maxSum / k
