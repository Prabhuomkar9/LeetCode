int searchInsert(int *nums, int numsSize, int target)
{
    int l = 0, mid;
    numsSize--;

    while (l < numsSize)
    {
        mid = (l + numsSize) / 2;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target)
            l = mid + 1;
        else
            numsSize = mid - 1;
    }

    return nums[l] < target ? l + 1 : l;
}
