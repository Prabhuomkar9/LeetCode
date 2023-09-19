class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {k: [] for k in range(9)}
        colHash = {k: [] for k in range(9)}
        squareHash = {k: [] for k in range(9)}
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                val = board[row][col]
                if (
                    val in rowHash[col]
                    or val in colHash[row]
                    or val in squareHash[row // 3 * 3 + col // 3]
                ):
                    return False
                rowHash[col].append(val)
                colHash[row].append(val)
                squareHash[row // 3 * 3 + col // 3].append(val)
        return True
