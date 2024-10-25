class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        int ans = 0;

        for (int num : nums) {
            if (seen.containsKey(num))
                seen.put(num, seen.get(num) + 1);
            else
                seen.put(num, 0);
            ans += seen.get(num);
        }

        return ans;
    }
}
