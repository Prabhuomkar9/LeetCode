class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prevSpend = spend = 0

        for c in cost:
            prevSpend, spend = spend, c + min(prevSpend, spend)

        return min(prevSpend, spend)
