class Solution {
    public boolean winnerOfGame(String colors) {
        int moveA = 0, moveB = 0, countA = 0, countB = 0;

        for (char color : colors.toCharArray()) {
            if (color == 'A') {
                countB = 0;
                countA++;
                if (countA > 2)
                    moveA++;
            } else {
                countA = 0;
                countB++;
                if (countB > 2)
                    moveB++;
            }
        }

        return moveA > moveB;
    }
}
