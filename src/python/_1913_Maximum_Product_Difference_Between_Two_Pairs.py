class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        firstMax = 0
        secondMax = 0
        firstMin = float("infinity")
        secondMin = float("infinity")

        for num in nums:
            if num > firstMax:
                firstMax, secondMax = num, firstMax
            elif num > secondMax:
                secondMax = num

            if num < firstMin:
                firstMin, secondMin = num, firstMin
            elif num < secondMin:
                secondMin = num

        return (firstMax * secondMax) - (firstMin * secondMin)
