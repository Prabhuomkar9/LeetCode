class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int prevSpend = 0, spend = 0;

        for (int c : cost) {
            int temp = prevSpend;
            prevSpend = spend;
            spend = c + (temp < prevSpend ? temp : prevSpend);
        }

        if (prevSpend < spend)
            return prevSpend;
        else
            return spend;
    }
}
