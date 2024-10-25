public class Solution {
    public String reverseVowels(String s) {
        boolean[] vowels = new boolean[128];
        vowels['a'] = true;
        vowels['A'] = true;
        vowels['e'] = true;
        vowels['E'] = true;
        vowels['i'] = true;
        vowels['I'] = true;
        vowels['o'] = true;
        vowels['O'] = true;
        vowels['u'] = true;
        vowels['U'] = true;

        char[] str = s.toCharArray();
        int l = 0, r = s.length() - 1;

        while (l < r) {
            while (l < r && !vowels[str[l]])
                l++;

            while (l < r && !vowels[str[r]])
                r--;

            char temp = str[l];
            str[l] = str[r];
            str[r] = temp;

            l++;
            r--;
        }

        return new String(str);
    }
}
