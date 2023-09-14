#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *convert(char *s, int numRows)
{
    if (numRows == 1)
        return s;

    int n = strlen(s);

    char **row = (char **)malloc(numRows * sizeof(char *));
    int *rowSize = (int *)malloc(numRows * sizeof(int));
    for (int i = 0; i < numRows; i++)
    {
        rowSize[i] = 0;
        row[i] = (char *)malloc((rowSize[i] + 1) * sizeof(char));
    }

    int goingDown = 1, rowNo = -1;
    for (int i = 0; i < n; i++)
    {
        if (goingDown)
            rowNo++;
        else
            rowNo--;
        if (rowNo == numRows - 1)
            goingDown = 0;
        if (rowNo == 0)
            goingDown = 1;
        row[rowNo][rowSize[rowNo]++] = s[i];
        row[rowNo] = (char *)realloc(row[rowNo], (rowSize[i] + 1) * sizeof(char));
    }

    for (int i = 0; i < numRows; i++)
        row[i][rowSize[i]] = '\0';

    for (int i = 0; i < numRows; i++)
    {
        for (int j = 0; row[i][j] != '\0'; j++)
        {
            printf("%c\t", row[i][j]);
        }
        printf("\n");
    }

    rowNo = 0;
    int rowCell = 0;
    for (int i = 0; i < n; i++)
    {
        if (rowCell >= rowSize[rowNo])
        {
            rowNo++;
            rowCell = 0;
        }
        s[i] = row[rowNo][rowCell++];
    }
    for (int i = 0; i < numRows; i++)
        free(row[i]);
    free(row);
    free(rowSize);
    return s;
}

// Driver code
int main(int argc, char const *argv[])
{
    char s[] = "0123456789ABCDEF";
    char *ans = convert(s, 3);
    printf("%s", ans);
    return 0;
}
