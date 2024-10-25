int titleToNumber(char *columnTitle)
{
    int ans = 0;

    for (; *columnTitle; columnTitle++)
    {
        int digit = *columnTitle - 'A' + 1;

        ans = (ans * 26) + digit;
    }

    return ans;
}
