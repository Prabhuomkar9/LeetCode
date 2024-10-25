class Solution {
    public int countVowelPermutation(int n) {
        final int MOD = 1000000007;

        long a = 1, e = 1, i = 1, o = 1, u = 1;

        for (int idx = 0; idx < n - 1; idx++) {
            long A = e;
            long E = (a + i) % MOD;
            long I = (a + e + o + u) % MOD;
            long O = (i + u) % MOD;
            long U = a;

            a = A;
            e = E;
            i = I;
            o = O;
            u = U;
        }

        return (int) ((a + e + i + o + u) % MOD);
    }
}
