/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
    *returnSize = 2;
    int *ans = (int *)malloc(2 * sizeof(int));
    ans[0] = -1;
    ans[1] = -1;

    int l = 0, r = numsSize - 1;

    while (l <= r)
    {
        int m = (l + r) / 2;

        if (nums[m] == target && (m == 0 || nums[m - 1] != nums[m]))
        {
            ans[0] = m;
            break;
        }
        else if (nums[m] >= target)
            r = m - 1;
        else
            l = m + 1;
    }

    l = 0, r = numsSize - 1;

    while (l <= r)
    {
        int m = (l + r) / 2;

        if (nums[m] == target && (m == numsSize - 1 || nums[m] != nums[m + 1]))
        {
            ans[1] = m;
            break;
        }
        else if (nums[m] <= target)
            l = m + 1;
        else
            r = m - 1;
    }

    return ans;
}
