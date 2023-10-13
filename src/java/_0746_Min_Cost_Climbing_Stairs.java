class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] dp = new int[cost.length];

        dp[cost.length - 1] = cost[cost.length - 1];
        dp[cost.length - 2] = cost[cost.length - 2];

        for (int i = cost.length - 3; i >= 0; i--)
            if (dp[i + 1] < dp[i + 2])
                dp[i] = cost[i] + dp[i + 1];
            else
                dp[i] = cost[i] + dp[i + 2];

        return dp[0] < dp[1] ? dp[0] : dp[1];
    }
}
