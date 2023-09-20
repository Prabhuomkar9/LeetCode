class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        monoStack = []

        for i, temp in enumerate(temperatures):
            while monoStack and monoStack[-1][0] < temp:
                lastTemp, j = monoStack.pop()
                ans[j] = i - j

            monoStack.append((temp, i))

        return ans
