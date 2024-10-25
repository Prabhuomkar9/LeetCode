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
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null)
            return new ArrayList<>();

        List<Integer> ans = new ArrayList<>();

        Deque<TreeNode> dq = new ArrayDeque<>();

        dq.add(root);

        while (dq.size() > 0) {
            int size = dq.size(), rightMost = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = dq.removeFirst();
                if (node.left != null)
                    dq.add(node.left);
                if (node.right != null)
                    dq.add(node.right);
                rightMost = node.val;
            }

            ans.add(rightMost);
        }

        return ans;
    }
}
