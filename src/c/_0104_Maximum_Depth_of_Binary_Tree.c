/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode *root)
{
    if (!root)
        return 0;

    int leftDepth = maxDepth(root->left), rightDepth = maxDepth(root->right);

    if (leftDepth > rightDepth)
        return 1 + leftDepth;

    return 1 + rightDepth;
}
