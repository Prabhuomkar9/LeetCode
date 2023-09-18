int myAtoi(char *s)
{
    long int ans = 0;
    int isNegative = 0;
    while (*s == ' ')
        s++;
    if (*s == '+')
        s++;
    else if (*s == '-')
    {
        s++;
        isNegative = 1;
    }
    while (isdigit(*s) && ans >= -2147483648 && ans <= 2147483647)
    {
        if (isNegative)
            ans = (ans * 10) + '0' - *s++;
        else
            ans = (ans * 10) + *s++ - '0';
    }
    if (ans < -2147483648)
        return -2147483648;
    if (ans > 2147483647)
        return 2147483647;
    return ans;
}
