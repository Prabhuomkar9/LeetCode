/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *countBits(int n, int *returnSize)
{
    *returnSize = n + 1;
    int *ans = (int *)malloc(*returnSize * sizeof(int));
    ans[0] = 0;

    for (int i = 0; i < n + 1; i++)
        ans[i] = ans[i / 2] + i % 2;

    return ans;
}
