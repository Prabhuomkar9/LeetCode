double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    if (nums1Size == 0)
        return nums2Size % 2 ? nums2[nums2Size / 2] : (nums2[nums2Size / 2 - 1] + nums2[nums2Size / 2]) / 2.0;
    if (nums2Size == 0)
        return nums1Size % 2 ? nums1[nums1Size / 2] : (nums1[nums1Size / 2 - 1] + nums1[nums1Size / 2]) / 2.0;
    if (nums1Size > nums2Size)
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);

    int total = nums1Size + nums2Size,
        partitionSize = (total + 1) / 2;

    int smallConsideredStart = 0, smallConsideredEnd = nums1Size;

    int smallPartitionEndIndex, largePartitionEndIndex;
    int smallLeftValue, smallRightValue, largeLeftValue, largeRightValue;

    while (smallConsideredStart <= smallConsideredEnd)
    {
        smallPartitionEndIndex = (smallConsideredStart + smallConsideredEnd) / 2;
        largePartitionEndIndex = partitionSize - smallPartitionEndIndex;

        smallLeftValue = smallPartitionEndIndex == 0 ? INT_MIN : nums1[smallPartitionEndIndex - 1];
        smallRightValue = smallPartitionEndIndex >= nums1Size ? INT_MAX : nums1[smallPartitionEndIndex];
        largeLeftValue = largePartitionEndIndex == 0 ? INT_MIN : nums2[largePartitionEndIndex - 1];
        largeRightValue = largePartitionEndIndex >= nums2Size ? INT_MAX : nums2[largePartitionEndIndex];

        if (smallLeftValue <= largeRightValue && largeLeftValue <= smallRightValue)
            return total % 2 ? (smallLeftValue >= largeLeftValue ? smallLeftValue : largeLeftValue) : ((smallLeftValue >= largeLeftValue ? smallLeftValue : largeLeftValue) + (smallRightValue <= largeRightValue ? smallRightValue : largeRightValue)) / 2.0;
        else if (smallLeftValue > largeRightValue)
            smallConsideredEnd = smallPartitionEndIndex - 1;
        else
            smallConsideredStart = smallPartitionEndIndex + 1;
    }
    return 0.0;
}
