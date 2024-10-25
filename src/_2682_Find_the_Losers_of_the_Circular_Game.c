/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *circularGameLosers(int n, int k, int *returnSize)
{
    bool *seen = (int *)malloc(n * sizeof(int));

    memset(seen, false, n * sizeof(int));

    int i = 1, num = 0;

    while (!seen[num])
    {
        seen[num] = true;
        num += i * k;
        num %= n;
        i++;
    }

    *returnSize = n - i + 1;
    int *ans = (int *)malloc(*returnSize * sizeof(int));
    i = 0;

    for (int j = 0; j < n; j++)
        if (!seen[j])
            ans[i++] = j + 1;

    free(seen);

    return ans;
}
