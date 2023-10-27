class Solution {
    public int minFlips(int a, int b, int c) {
        int count = 0;
        int bitA, bitB, bitC;

        while (a != 0 || b != 0 || c != 0) {
            bitA = a & 1;
            bitB = b & 1;
            bitC = c & 1;
            if ((bitA | bitB) != bitC)
                if (bitC == 0)
                    count += (bitA + bitB);
                else
                    count += 1;
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }

        return count;
    }
}
