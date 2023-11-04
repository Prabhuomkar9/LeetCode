class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0, col = matrix[0].length - 1;

        while (row < matrix.length && col > -1)
            if (matrix[row][col] == target)
                return true;
            else if (matrix[row][col] < target)
                row += 1;
            else
                col -= 1;

        return false;
    }
}
