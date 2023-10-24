char *mergeAlternately(char *word1, char *word2)
{
    int m = strlen(word1), n = strlen(word2);
    char *ans = (char *)malloc((m + n + 1) * sizeof(char));
    ans[m + n] = '\0';

    for (int i = 0, idx = 0; i < m || i < n; i++)
    {
        if (i < m)
            ans[idx++] = word1[i];

        if (i < n)
            ans[idx++] = word2[i];
    }

    return ans;
}
