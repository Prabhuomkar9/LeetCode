class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int num : nums)
            total += num;

        int prefix = 0;
        for (int i = 0; i < nums.length; prefix += nums[i++])
            if (prefix == total - prefix - nums[i])
                return i;

        return -1;
    }
}
