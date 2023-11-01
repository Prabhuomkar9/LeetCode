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
    private int dfs(TreeNode root, int maxVal) {
        int good = 0;

        if (root.val >= maxVal) {
            good++;
            maxVal = root.val;
        }

        if (root.left != null)
            good += this.dfs(root.left, maxVal);

        if (root.right != null)
            good += this.dfs(root.right, maxVal);

        return good;
    }

    public int goodNodes(TreeNode root) {
        return this.dfs(root, root.val);
    }
}
