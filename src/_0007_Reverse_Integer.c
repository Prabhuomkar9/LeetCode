int reverse(int x)
{
    long int res = 0;
    while (x != 0)
    {
        res = (res * 10) + (x % 10);
        x = x / 10;
    }
    if (res <= -2147483648 || res >= 2147483647)
        return 0;
    return (int *)res;
}
