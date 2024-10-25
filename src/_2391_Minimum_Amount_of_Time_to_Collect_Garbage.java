class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int n = garbage.length, ans = 0;

        for(int time: travel)
            ans += 3 * time;

        for(String house: garbage)
            ans += house.length();

        for(int i = n - 1; i > 0; i--)
            if (!garbage[i].contains("G"))
                ans -= travel[i - 1];
            else
                break;

        for(int i = n - 1; i > 0; i--)
            if (!garbage[i].contains("P"))
                ans -= travel[i - 1];
            else
                break;

        for(int i = n - 1; i > 0; i--)
            if (!garbage[i].contains("M"))
                ans -= travel[i - 1];
            else
                break;

        return ans;
    }
}
