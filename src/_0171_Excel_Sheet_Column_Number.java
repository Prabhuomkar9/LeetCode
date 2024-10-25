public class _0171_Excel_Sheet_Column_Number {

}

class Solution {
    public int titleToNumber(String columnTitle) {
        int ans = 0;

        for (int i = 0; i < columnTitle.length(); i++) {
            int digit = columnTitle.charAt(i) - 'A' + 1;

            ans = (ans * 26) + digit;
        }

        return ans;
    }
}
