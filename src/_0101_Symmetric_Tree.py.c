/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool dfs(struct TreeNode *left, struct TreeNode *right)
{
    if (!left && !right)
        return true;

    if (!left || !right)
        return false;

    if (left->val != right->val)
        return false;

    return dfs(left->left, right->right) && dfs(left->right, right->left);
}

bool isSymmetric(struct TreeNode *root)
{
    return dfs(root->left, root->right);
}
