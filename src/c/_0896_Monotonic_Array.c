bool isMonotonic(int *nums, int numsSize)
{
    if (nums[0] < nums[numsSize - 1])
    {
        for (int i = 1; i < numsSize; i++)
            if (nums[i - 1] > nums[i])
                return false;
    }
    else
    {
        for (int i = 1; i < numsSize; i++)
            if (nums[i - 1] < nums[i])
                return false;
    }

    return true;
}
