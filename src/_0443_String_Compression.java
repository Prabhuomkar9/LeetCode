class Solution {
    public int compress(char[] chars) {
        int turtle = 0, idx = 0;

        for (int hare = 1; hare <= chars.length; hare++) {
            if (hare < chars.length && chars[turtle] == chars[hare])
                continue;

            int count = hare - turtle;
            chars[idx++] = chars[turtle];
            turtle = hare;

            if (count == 1)
                continue;

            if (count < 10) {
                chars[idx++] = (char) (count + '0');
            }

            for (char digit : Integer.toString(count).toCharArray())
                chars[idx++] = digit;

        }

        return idx;
    }
}
