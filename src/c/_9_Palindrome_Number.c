bool isPalindrome(int x)
{
    if (x < 0)
        return false;
    int temp = x, len = 0;
    while (temp != 0)
    {
        temp = temp / 10;
        len++;
    }
    for (int i = 0; i < len / 2; i++)
    {
        temp = (temp * 10) + (x % 10);
        x = x / 10;
    }
    if (len % 2 == 1)
        x = x / 10;
    if (temp == x)
        return true;
    return false;
}
