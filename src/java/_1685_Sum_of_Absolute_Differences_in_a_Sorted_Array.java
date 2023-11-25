class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        int prefix = 0, suffix = 0, n = nums.length;
        int[] ans = new int[n];

        for(int num : nums)
            suffix += num;

        for(int i = 0; i < n; i++){
            int num = nums[i];
            ans[i] = num * i - prefix + suffix - num * (n - i);
            prefix += num;
            suffix -= num;
        }

        return ans;
    }
}
