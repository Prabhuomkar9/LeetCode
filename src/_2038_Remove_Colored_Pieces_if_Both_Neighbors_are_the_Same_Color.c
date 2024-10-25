bool winnerOfGame(char *colors)
{
    int moveA = 0, moveB = 0, countA = 0, countB = 0;

    while (*colors)
    {
        if (*colors == 'A')
        {
            countB = 0;
            countA++;
            if (countA > 2)
                moveA++;
        }
        else
        {
            countA = 0;
            countB++;
            if (countB > 2)
                moveB++;
        }
        colors++;
    }

    return moveA > moveB;
}
