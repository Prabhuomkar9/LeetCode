void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    m--;
    n--;

    while (n >= 0)
        if (m < 0 || nums1[m] < nums2[n])
        {
            nums1[m + n + 1] = nums2[n];
            n--;
        }
        else
        {
            nums1[m + n + 1] = nums1[m];
            m--;
        }
}
