char *convert(char *s, int numRows)
{
    if (numRows == 1)
        return s;
    int n = strlen(s), limit = (numRows - 1) * 2;
    char *ans = (char *)malloc((n + 1) * sizeof(char));
    int end = 0, i = 0, row = 0, alt = 0, flag = 0;
    while (end != n)
    {
        if (i >= n)
        {
            row++;
            i = row;
            alt = 0;
            continue;
        }
        if (!flag)
            ans[end++] = s[i];
        flag = 0;
        if (alt)
        {
            alt = 0;
            i += row * 2;
            if (row * 2 == 0)
                flag = 1;
        }
        else
        {
            alt++;
            i += limit - (row * 2);
            if (limit - (row * 2) == 0)
                flag = 1;
        }
    }
    ans[n] = '\0';
    return ans;
}
