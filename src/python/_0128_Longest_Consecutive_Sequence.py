class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        leftMost = {}
        seen = set(nums)

        for n in nums:
            if n - 1 not in seen:
                leftMost[n] = 1

        for left in leftMost:
            temp = left
            while temp + 1 in seen:
                leftMost[left] += 1
                temp += 1

        return max(leftMost.values())
