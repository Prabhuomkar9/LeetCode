int majorityElement(int *nums, int numsSize)
{
    int ans = nums[0], count = 1;

    for (int i = 1; i < numsSize; i++)
    {
        if (count == 0)
            ans = nums[i];

        if (ans == nums[i])
            count++;
        else
            count--;
    }

    return ans;
}
