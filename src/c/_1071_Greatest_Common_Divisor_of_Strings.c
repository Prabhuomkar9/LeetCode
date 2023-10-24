int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }

    return a;
}

char *gcdOfStrings(char *str1, char *str2)
{
    int m = strlen(str1), n = strlen(str2);
    if (m > n)
        return gcdOfStrings(str2, str1);

    for (int i = 0; i < m; i++)
        if (str1[i] != str2[i])
            return "\0";

    for (int i = m; i < n; i++)
        if (str2[i - m] != str2[i])
            return "\0";

    for (int i = n; i < m + n; i++)
        if (str2[i - m] != str1[i - n])
            return "\0";

    int end = gcd(m, n);
    char *ans = (char *)malloc(end + 1);
    strncpy(ans, str2, end);
    ans[end] = '\0';
    return ans;
}
