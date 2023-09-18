bool isValid(char *s)
{
    if (strlen(s) % 2 == 1)
        return false;
    char *temp = (char *)malloc((strlen(s) + 1) * sizeof(char));
    int i = 0, j = 0;
    while (s[i] != '\0')
    {
        if (s[i] == ')')
            if (temp[j] == '(')
                j--;
            else
                return false;
        else if (s[i] == '}')
            if (temp[j] == '{')
                j--;
            else
                return false;
        else if (s[i] == ']')
            if (temp[j] == '[')
                j--;
            else
                return false;
        else
            temp[++j] = s[i];
        i++;
    }
    if (j == 0)
        return true;
    return false;
}
