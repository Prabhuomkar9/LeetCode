class Solution {
    public void reverseString(char[] s) {
        int head = 0, tail = s.length - 1;

        while (head < tail) {
            char temp = s[head];
            s[head] = s[tail];
            s[tail] = temp;
            head++;
            tail--;
        }
    }
}
