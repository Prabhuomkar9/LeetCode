class Solution {
    public int arrangeCoins(int n) {
        long l = 1, r = n / 2 + 1, k, total;

        while (l <= r) {
            k = l + (r - l) / 2;
            total = k * (k + 1) / 2;

            if (total == n)
                return (int) k;
            else if (total < n)
                l = k + 1;
            else
                r = k - 1;
        }

        return (int) r;
    }
}
