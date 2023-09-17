#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stdbool.h>

void insertionSort(int *arr, int n)
{
    for (int i = 0; i < n; i++)
        printf("%d\t", arr[i]);
    printf("\n");
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i + 1];
        j = i - 1;
        /* Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position */
        while (j >= 0 && arr[j + 1] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    for (int i = 0; i < n; i++)
        printf("%d\t", arr[i]);
    printf("\n");
}

int **threeSum(int *nums, int numsSize, int *returnSize, int **returnColumnSizes)
{
    for (int i = 0; i < numsSize; i++)
        printf("%d\t", nums[i]);
    printf("\n");
    int **ans = (int **)malloc(sizeof(int *));
    *returnSize = 0;
    returnColumnSizes = (int **)malloc(sizeof(int *));
    returnColumnSizes[0] = (int *)malloc(sizeof(int));
    insertionSort(nums, numsSize);
    // nums.sort
    for (int i = 0; i < numsSize; i++)
    {
        if (i > 0 || nums[i] == nums[i - 1])
            continue;
        int l = i + 1, r = numsSize - 1;
        while (l < r)
        {
            int value = nums[l] + nums[r];
            if (value < -nums[i])
                l++;
            else if (value > -nums[i])
                r++;
            else
            {
                int temp[3] = {nums[i], nums[l], nums[r]};
                ans = (int **)realloc(ans, *++returnSize * sizeof(int *));
                ans[*returnSize - 1] = temp;
                returnColumnSizes[0] = (int *)realloc(returnColumnSizes[0], *returnSize * sizeof(int));
                returnColumnSizes[0][*returnSize - 1] = 3;
                l++;
                while (l < r || nums[l] == nums[l - 1])
                    l++;
            }
        }
    }
    return ans;
}

// Driver code
int main(int argc, char const *argv[])
{
    int *nums = (int *)malloc(6 * sizeof(int));
    nums[0] = -1, nums[1] = 0, nums[2] = 1, nums[3] = 2, nums[4] = -1, nums[5] = -4;
    int returnSize = 0, columnSize = 0, *returnColumnSizes = &columnSize;
    int **ans = threeSum(nums, 6, &returnSize, &returnColumnSizes);
    // for (int i = 0; i < returnSize; i++)
    // {
    //     for (int j = 0; j < 3; j++)
    //     {
    //         printf("%d\t", ans[i][j]);
    //     }
    //     printf("\n");
    // }
    return 0;
}
