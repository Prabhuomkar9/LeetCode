class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moveA, moveB, countA, countB = 0, 0, 0, 0

        for color in colors:
            if color == "A":
                countB = 0
                countA += 1
                if countA > 2:
                    moveA += 1
            else:
                countA = 0
                countB += 1
                if countB > 2:
                    moveB += 1

        return moveA > moveB
