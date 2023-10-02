/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode *root, int targetSum)
{
    if (root == NULL)
        return false;

    targetSum -= root->val;

    if (root->left == NULL && root->right == NULL)
        return targetSum == 0;

    bool left = hasPathSum(root->left, targetSum);
    bool right = hasPathSum(root->right, targetSum);

    return left || right;
}
