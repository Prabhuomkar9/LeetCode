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
    private int ans = 0;

    private int[] dfs(TreeNode root) {
        int total = root.val, count = 1;

        if (root.left != null) {
            int[] left = dfs(root.left);
            total += left[0];
            count += left[1];
        }

        if (root.right != null) {
            int[] right = dfs(root.right);
            total += right[0];
            count += right[1];
        }

        if (total / count == root.val)
            this.ans += 1;

        return new int[] { total, count };
    }

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return this.ans;
    }
}
