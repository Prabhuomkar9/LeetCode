class Solution {
    public String removeStars(String s) {
        int i = 0;
        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray())
            if (c == '*')
                sb.deleteCharAt(--i);
            else
                sb.insert(i++, c);

        return sb.toString();
    }
}
