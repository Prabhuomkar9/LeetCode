class Solution {
    public int[] circularGameLosers(int n, int k) {
        boolean seen[] = new boolean[n];

        int i = 1, num = 0;

        while (!seen[num]) {
            seen[num] = true;
            num += i * k;
            num %= n;
            i++;
        }

        int[] ans = new int[n - i + 1];
        i = 0;

        for (int j = 0; j < n; j++)
            if (!seen[j])
                ans[i++] = j + 1;

        return ans;
    }
}
