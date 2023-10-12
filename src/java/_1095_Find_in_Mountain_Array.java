/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int length = mountainArr.length();

        int l = 1, r = length - 2, peak = -1;

        while(l <= r){
            int m = (l + r) / 2;
            int prevVal = mountainArr.get(m - 1);
            int currVal = mountainArr.get(m);
            int nextVal = mountainArr.get(m + 1);

            if(prevVal < currVal && currVal > nextVal){
                if(currVal == target)
                    return m;
                peak = m;
                break;
            }
            else if(prevVal < currVal && currVal < nextVal)
                l = m + 1;
            else
                r = m - 1;
        }

        l = 0;
        r = peak - 1;

        while(l <= r){
            int m = (l + r) / 2;
            int currVal = mountainArr.get(m);

            if(currVal == target)
                return m;
            else if(currVal < target)
                l = m + 1;
            else
                r = m - 1;
        }

        l = peak + 1;
        r = length - 1;

        while(l <= r){
            int m = (l + r) / 2;
            int currVal = mountainArr.get(m);

            if(currVal == target)
                return m;
            else if(currVal < target)
                r = m - 1;
            else
                l = m + 1;
        }

        return -1;
    }
}
