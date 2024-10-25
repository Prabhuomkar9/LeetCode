/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
    let rowCount = grid.length;
    let colCount = grid[0].length;
    let perimeter = 0;

    for (let i = 0; i < rowCount; i++)
        for (let j = 0; j < colCount; j++)
            if (grid[i][j] == 1) {
                if (i == 0 || grid[i - 1][j] != 1)
                    perimeter += 2;
                if (j == 0 || grid[i][j - 1] != 1)
                    perimeter += 2;
            }

    return perimeter;
};
