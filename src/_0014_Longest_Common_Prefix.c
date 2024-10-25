char *longestCommonPrefix(char **strs, int strsSize)
{
    if (strsSize == 1)
        return strs[0];
    int ansLength = strlen(strs[0]);
    char *ans = (char *)malloc((ansLength + 1) * sizeof(char));
    strcpy(ans, strs[0]);
    for (int i = 1; i < strsSize; i++)
    {
        while (strncmp(ans, strs[i], ansLength) != 0)
            ans[--ansLength] = '\0';
        if (ansLength == 0)
            return ans;
    }
    return ans;
}
