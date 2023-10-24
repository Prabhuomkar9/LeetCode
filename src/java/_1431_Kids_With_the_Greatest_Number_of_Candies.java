class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int greatest = 0;

        for (int candy : candies)
            greatest = Math.max(greatest, candy);

        List<Boolean> ans = new ArrayList<>();

        for (int candy : candies)
            ans.add(candy + extraCandies >= greatest);

        return ans;
    }
}
