int minCostClimbingStairs(int *cost, int costSize)
{
    int *dp = (int *)malloc(costSize * sizeof(int));

    dp[costSize - 1] = cost[costSize - 1];
    dp[costSize - 2] = cost[costSize - 2];

    for (int i = costSize - 3; i >= 0; i--)
        if (dp[i + 1] < dp[i + 2])
            dp[i] = cost[i] + dp[i + 1];
        else
            dp[i] = cost[i] + dp[i + 2];

    return dp[0] < dp[1] ? dp[0] : dp[1];
}
