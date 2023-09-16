#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stdbool.h>

int **threeSum(int *nums, int numsSize, int *returnSize, int **returnColumnSizes)
{
    int **returnColumnSize = 3;
    for (int i = 0; i < numsSize; i++)
    {
        for (int j = i + 1; j < numsSize; j++)
        {
            for (int k = j + 1; k < numsSize; k++)
            {
                if (nums[i] + nums[j] + nums[k] == 0)
                {
                    int *temp = (int *)malloc(3 * sizeof(int));
                    temp[0] = i;
                    temp[1] = j;
                    temp[2] = k;
                }
            }
        }
    }
}

// Driver code
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
