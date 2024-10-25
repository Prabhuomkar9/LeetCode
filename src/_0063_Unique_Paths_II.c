int uniquePathsWithObstacles(int **obstacleGrid, int obstacleGridSize, int *obstacleGridColSize)
{
    if (obstacleGrid[0][0] == 1)
        return 0;

    for (int i = 0; i < obstacleGridSize; i++)
    {
        for (int j = 0; j < *obstacleGridColSize; j++)
        {
            if (obstacleGrid[i][j] == 1)
                obstacleGrid[i][j] = 0;
            else if (i == 0 && j == 0)
                obstacleGrid[i][j] = 1;
            else if (i == 0)
                obstacleGrid[i][j] = obstacleGrid[i][j - 1];
            else if (j == 0)
                obstacleGrid[i][j] = obstacleGrid[i - 1][j];
            else
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
        }
    }

    return obstacleGrid[obstacleGridSize - 1][*obstacleGridColSize - 1];
}
