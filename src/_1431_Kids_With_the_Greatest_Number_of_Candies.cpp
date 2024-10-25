class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        int greatest = 0;

        for (int candy : candies)
            greatest = max(greatest, candy);

        vector<bool> ans;

        for (int candy : candies)
            ans.push_back(candy + extraCandies >= greatest);

        return ans;
    }
};
