class Solution {
    public boolean isPerfectSquare(int num) {
        long l = 0, r = num, m;

        while (l <= r) {
            m = l + (r - l) / 2;

            if (m * m == num)
                return true;
            else if (m * m < num)
                l = m + 1;
            else
                r = m - 1;
        }

        return false;
    }
}
