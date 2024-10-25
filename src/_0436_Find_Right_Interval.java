class Solution {
    public int[] findRightInterval(int[][] intervals) {
        int length = intervals.length;
        int[] starts = new int[length];
        Map<Integer, Integer> indices = new HashMap<>();

        for (int i = 0; i < length; i++) {
            starts[i] = intervals[i][0];
            indices.put(intervals[i][0], i);
        }

        Arrays.sort(starts);

        int[] ans = new int[length];

        for (int i = 0; i < length; i++) {
            int idx = Arrays.binarySearch(starts, intervals[i][1]);

            if (idx >= 0)
                ans[i] = indices.get(starts[idx]);
            else if (idx + length >= 0)
                ans[i] = indices.get(starts[-idx - 1]);
            else
                ans[i] = -1;
        }

        return ans;
    }
}
