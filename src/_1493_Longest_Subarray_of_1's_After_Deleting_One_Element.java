class Solution {
    public int longestSubarray(int[] nums) {
        int l = 0, r = 0, zeroIndex = -1, ans = 0;

        while (r < nums.length) {
            if (nums[r] == 0) {
                ans = Math.max(ans, r - l - 1);
                if (zeroIndex >= 0)
                    l = zeroIndex + 1;
                zeroIndex = r;
            }
            r += 1;
        }

        ans = Math.max(ans, r - l - 1);

        if (zeroIndex < 0)
            return nums.length - 1;

        return ans;
    }
}
