char *intToRoman(int num)
{
    int size;
    char *M[] = {"", "M", "MM", "MMM"};
    char *C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    char *X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    char *I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    size = strlen(M[num / 1000]) + strlen(C[(num % 1000) / 100]) + strlen(X[(num % 100) / 10]) + strlen(I[num % 10]) + 1;
    char *ans = malloc(size * sizeof(char));
    strcpy(ans, M[num / 1000]);
    strcat(ans, C[(num % 1000) / 100]);
    strcat(ans, X[(num % 100) / 10]);
    strcat(ans, I[num % 10]);
    return ans;
}
