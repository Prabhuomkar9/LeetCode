class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int currSum = 0, maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            if (i >= k)
                currSum -= nums[i - k];
            if (i >= k - 1)
                maxSum = maxSum > currSum ? maxSum : currSum;
        }

        return (double) maxSum / k;
    }
}
