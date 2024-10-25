class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int time = 0;

        for (int ant : left)
            if (ant > time)
                time = ant;

        for (int ant : right)
            if (n - ant > time)
                time = n - ant;

        return time;
    }
}
