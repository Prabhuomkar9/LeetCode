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
    public int maxLevelSum(TreeNode root) {
        int maxLevel = 1, maxSum = Integer.MIN_VALUE, currLevel = 1;
        Deque<TreeNode> dq = new ArrayDeque<>();

        dq.add(root);

        while (dq.size() > 0) {
            int size = dq.size(), currSum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = dq.removeFirst();
                currSum += node.val;
                if (node.left != null)
                    dq.add(node.left);
                if (node.right != null)
                    dq.add(node.right);
            }
            if (currSum > maxSum) {
                maxSum = currSum;
                maxLevel = currLevel;
            }
            currLevel += 1;
        }

        return maxLevel;
    }
}
