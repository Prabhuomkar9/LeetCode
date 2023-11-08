class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int horizontal = Math.abs(fx - sx);
        int vertical = Math.abs(fy - sy);
        int need = Math.max(horizontal, vertical);

        if (need > 0)
            return need <= t;
        else
            return t != 1;
    }
}
