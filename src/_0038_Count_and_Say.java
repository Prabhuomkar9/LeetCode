class Solution {
    public String countAndSay(int n) {
        if (n == 1)
            return "1";

        StringBuilder sb = new StringBuilder();
        String lastAns = this.countAndSay(n - 1);
        char seenCh = lastAns.charAt(0);
        int freq = 1;

        for (int i = 1; i < lastAns.length(); i++) {
            char ch = lastAns.charAt(i);
            if (seenCh == ch) {
                freq++;
            } else {
                sb.append(freq).append(seenCh);
                freq = 1;
                seenCh = ch;
            }
        }

        sb.append(freq).append(seenCh);

        return sb.toString();
    }
}
