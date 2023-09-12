int lengthOfLongestSubstring(char *s)
{
    // int array with index accessed as ascii values, behaving as a hash table
    int set[128] = {0};
    int length = 0, left = 0;
    for (int right = 0; s[right] != '\0'; right++)
    {
        while (set[s[right]] == 1)
        {
            set[s[left]] = 0;
            left++;
        }
        set[s[right]] = 1;
        length = right - left + 1 > length ? right - left + 1 : length;
    }
    return length;
}
