class Solution {
    public int countHomogenous(String s) {
        int MOD = (int) Math.pow(10, 9) + 7;
        long ans = 0;
        long length = 0;
        char lastSeen = s.charAt(0);

        for (char c : s.toCharArray()) {
            if (c == lastSeen) {
                length += 1;
            } else {
                ans = (ans + length * (length + 1) / 2) % MOD;
                lastSeen = c;
                length = 1;
            }
        }

        ans = (ans + length * (length + 1) / 2) % MOD;

        return (int) ans;
    }
}
