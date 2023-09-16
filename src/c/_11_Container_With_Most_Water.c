int maxArea(int *height, int heightSize)
{
    int ans = 0, vol = 0, *rHeight = height + heightSize - 1;
    while (height < rHeight)
    {
        if (*height < *rHeight)
            vol = *(height++) * --heightSize;
        else
            vol = *(rHeight--) * --heightSize;
        if (vol > ans)
            ans = vol;
    }
    return ans;
}
