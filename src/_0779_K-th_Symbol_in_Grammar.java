class Solution {
    private int dfs(int n, int k) {
        if (n == 0)
            return 0;

        if (n == 1)
            return k;

        int power = (int) Math.pow(2, n - 1);

        if (power > k)
            return dfs(n - 1, k);
        else if (dfs(n - 1, k % power) == 1)
            return 0;
        else
            return 1;
    }

    public int kthGrammar(int n, int k) {
        return dfs(n - 1, k - 1);
    }
}
