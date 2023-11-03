class Solution {
    public List<String> buildArray(int[] target, int n) {
        int j = 0;
        List<String> ans = new ArrayList<>();

        for (int i = 1; i <= target[target.length - 1]; i++) {
            ans.add("Push");
            if (target[j] != i)
                ans.add("Pop");
            else
                j += 1;
        }

        return ans;
    }
}
