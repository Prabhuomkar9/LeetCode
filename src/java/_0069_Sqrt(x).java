class Solution {
    public int mySqrt(int x) {
        if(x <= 1)
            return x;

        int l = 0, r = 46340;

        while(l <= r){
            int m = (l + r) / 2, val = m * m;

            if(val == x)
                return m;
            else if(val < x)
                l = m + 1;
            else
                r = m - 1;
        }

        return r;
    }
}
