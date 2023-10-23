class Solution {
    public boolean isPowerOfFour(int n) {
        return (n & (n - 1)) == 0 && (n | 0xAAAAAAAA) != 0xAAAAAAAA;
    }
}
