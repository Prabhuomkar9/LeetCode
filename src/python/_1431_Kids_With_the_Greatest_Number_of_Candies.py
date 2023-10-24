class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)

        ans = [candy + extraCandies >= greatest for candy in candies]

        return ans
