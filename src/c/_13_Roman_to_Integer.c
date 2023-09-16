#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <limits.h>
#include <stdbool.h>

int romanToInt(char *s)
{
    int t['X' + 1] = {['I'] = 1, ['V'] = 5, ['X'] = 10, ['L'] = 50, ['C'] = 100, ['D'] = 500, ['M'] = 1000};
    int res = 0;
    for (int i = 0; s[i]; i++)
    {
        if (t[s[i]] < t[s[i + 1]])
            res -= t[s[i]];
        else
            res += t[s[i]];
    }
    return res;
}

// Driver code
int main(int argc, char const *argv[])
{
    char str[] = "MMMDCCCLXXXVIII";
    printf("%d", romanToInt(str));
    return 0;
}
