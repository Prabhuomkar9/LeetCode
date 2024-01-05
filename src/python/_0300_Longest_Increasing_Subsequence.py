class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # TLE - Memoization DP
        # @lru_cache
        # def dfs(idx, last):
        #     if idx >= len(nums):
        #         return 0

        #     included = 0
        #     if last < nums[idx]:
        #         included = 1 + dfs(idx + 1, nums[idx])

        #     notIncluded = dfs(idx + 1, last)

        #     return max(included, notIncluded)

        # return dfs(0, float("-infinity"))

        # Bottom-Up DP
        dp = [1 for _ in nums]
        ans = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])

        return ans
