int lengthOfLastWord(char *s)
{
    int count = 0, i = 0;

    while (*s)
    {
        if (*s == ' ')
            i = 0;
        else
            i++, count = i;

        s++;
    }

    return count;
}
