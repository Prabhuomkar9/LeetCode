bool isPalindrome(int x)
{
    if (x < 0)
        return false;
    long rev = 0, temp = x;
    while (temp > 0)
    {
        rev = (rev * 10) + (temp % 10);
        temp = temp / 10;
    }
    if (x == rev)
        return true;
    return false;
}
