class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(n):
            if n >= len(nums):
                ans.append([x for x in subset])
                return

            subset.append(nums[n])
            backtrack(n + 1)

            subset.pop()
            backtrack(n + 1)

        backtrack(0)

        return ans
