class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = 0, sum(nums)
        ans = []

        for i, num in enumerate(nums):
            ans.append(num * i - prefix + suffix - num * (n - i))
            prefix += num
            suffix -= num

        return ans
