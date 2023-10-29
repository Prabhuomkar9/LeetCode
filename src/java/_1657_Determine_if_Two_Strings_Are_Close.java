class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length())
            return false;

        int[] seen1 = new int[26];
        int[] seen2 = new int[26];

        for (char c : word1.toCharArray())
            seen1[c - 'a']++;

        for (char c : word2.toCharArray())
            seen2[c - 'a']++;

        for (int i = 0; i < 26; i++)
            if (seen1[i] * seen2[i] == 0 && seen1[i] + seen2[i] != 0)
                return false;

        Arrays.sort(seen1);
        Arrays.sort(seen2);

        for (int i = 0; i < 26; i++)
            if (seen1[i] != seen2[i])
                return false;

        return true;
    }
}
