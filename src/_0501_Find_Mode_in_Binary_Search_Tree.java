/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    private void dfs(TreeNode root, Map<Integer, Integer> seen) {
        if (root == null)
            return;

        seen.put(root.val, seen.getOrDefault(root.val, 0) + 1);

        this.dfs(root.left, seen);
        this.dfs(root.right, seen);
    }

    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> seen = new HashMap<>();

        this.dfs(root, seen);

        int mode = 0, count = 0;

        for (int freq : seen.values()) {
            if (freq > mode) {
                mode = freq;
                count = 1;
            } else if (freq == mode) {
                count++;
            }
        }

        int[] modes = new int[count];
        int j = 0;

        for (int key : seen.keySet()) {
            if (seen.get(key) == mode) {
                modes[j++] = key;
            }
        }

        return modes;
    }
}
