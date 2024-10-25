/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool *kidsWithCandies(int *candies, int candiesSize, int extraCandies, int *returnSize)
{
    *returnSize = candiesSize;
    int greatest = 0;

    for (int i = 0; i < candiesSize; i++)
        greatest = greatest > candies[i] ? greatest : candies[i];

    bool *ans = (bool *)malloc(candiesSize * sizeof(bool));

    for (int i = 0; i < candiesSize; i++)
        ans[i] = (candies[i] + extraCandies >= greatest);

    return ans;
}
