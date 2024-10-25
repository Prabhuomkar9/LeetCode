class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = 0, r = nums.length - 1, m;

        int[] ans = { -1, -1 };

        while (l <= r) {
            m = l + (r - l) / 2;

            if (nums[m] == target) {
                int first = m, last = m;

                while (first >= 0 && nums[first] == target)
                    first -= 1;

                while (last < nums.length && nums[last] == target)
                    last += 1;

                ans[0] = first + 1;
                ans[1] = last - 1;

                break;
            } else if (nums[m] < target)
                l = m + 1;
            else
                r = m - 1;
        }

        return ans;
    }
}
