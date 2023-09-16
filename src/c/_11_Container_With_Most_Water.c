int maxArea(int *height, int heightSize)
{
    int ans = 0, volume = 0, i = 0, j = heightSize - 1, width = j - i;
    while (i < j)
    {
        if (height[i] < height[j])
        {
            volume = height[i] * width--;
            i++;
        }
        else
        {
            volume = height[j] * width--;
            j--;
        }
        if (volume > ans)
            ans = volume;
    }
    return ans;
}
