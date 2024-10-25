char *longestPalindrome(char *s)
{
    int start, resultSize = 0;
    int sSize = strlen(s);
    int l, r;
    for (int i = 0; i < sSize; i++)
    {
        l = r = i;
        while (l >= 0 && r < sSize && s[l] == s[r])
        {
            if (r - l + 1 > resultSize)
            {
                start = l;
                resultSize = r - l + 1;
            }
            l--, r++;
        }
        l = i, r = i + 1;
        while (l >= 0 && r < sSize && s[l] == s[r])
        {
            if (r - l + 1 > resultSize)
            {
                start = l;
                resultSize = r - l + 1;
            }
            l--, r++;
        }
    }

    char *result = (char *)malloc((resultSize + 1) * sizeof(char));
    for (int i = 0; i < resultSize; i++, start++)
        result[i] = s[start];
    result[resultSize] = '\0';
    return result;
}
