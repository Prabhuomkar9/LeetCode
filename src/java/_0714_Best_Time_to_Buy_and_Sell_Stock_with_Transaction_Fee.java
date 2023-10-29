class Solution {
    public int maxProfit(int[] prices, int fee) {
        int investment = -prices[0], profit = 0;

        for(int price : prices){
            investment = Math.max(investment, profit - price);
            profit = Math.max(profit, investment + price - fee);
        }

        return profit;
    }
}
