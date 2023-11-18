class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        monoStack = []

        for i, temperature in enumerate(temperatures):
            while monoStack and temperature > monoStack[-1][0]:
                _, idx = monoStack.pop()
                ans[idx] = i - idx

            monoStack.append((temperature, i))

        return ans
