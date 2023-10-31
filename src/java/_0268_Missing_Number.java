class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length, total = 0;

        for (int num : nums)
            total += num;

        return n * (n + 1) / 2 - total;
    }
}
