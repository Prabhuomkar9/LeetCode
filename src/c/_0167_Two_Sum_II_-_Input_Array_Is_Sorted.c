/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *numbers, int numbersSize, int target, int *returnSize)
{
    *returnSize = 2;
    int *ans = (int *)malloc(2 * sizeof(int));
    int l = 0, r = numbersSize - 1;
    while (l < r)
    {
        int value = numbers[l] + numbers[r];
        if (value > target)
            r--;
        if (value < target)
            l++;
        if (value == target)
        {
            ans[0] = l + 1;
            ans[1] = r + 1;
            return ans;
        }
    }
    return ans;
}
