/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int l = 0;

        while (l <= n) {
            int m = l + (n - l) / 2;

            if (isBadVersion(m))
                n = m - 1;
            else
                l = m + 1;
        }

        return n + 1;
    }
}
