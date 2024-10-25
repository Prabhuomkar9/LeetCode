public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (seenMap.containsKey(nums[i]) == true)
                return new int[] { seenMap.get(nums[i]), i };
            seenMap.put(target - nums[i], i);
        }

        return null;
    }
}
