class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        prev = ''
        currSum = 0
        maxTime = 0

        for color, time in zip(colors, neededTime):
            if color == prev:
                currSum += time
                maxTime = max(maxTime, time)
            else:
                ans += currSum - maxTime
                currSum = time
                maxTime = time
                prev = color

        return ans + currSum - maxTime
