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
    private List<Integer> ans = new ArrayList<>();

    private void dfs(TreeNode root, int row) {
        if (root == null)
            return;

        if (this.ans.size() <= row)
            ans.add(root.val);
        else
            ans.set(row, Math.max(ans.get(row), root.val));

        this.dfs(root.left, row + 1);
        this.dfs(root.right, row + 1);
    }

    public List<Integer> largestValues(TreeNode root) {
        this.dfs(root, 0);
        return this.ans;
    }
}
