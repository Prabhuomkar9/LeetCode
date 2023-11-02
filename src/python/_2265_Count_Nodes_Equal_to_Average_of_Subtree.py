# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            total = root.val
            count = 1

            if root.left:
                left = dfs(root.left)
                total += left[0]
                count += left[1]

            if root.right:
                right = dfs(root.right)
                total += right[0]
                count += right[1]

            nonlocal ans

            if total // count == root.val:
                ans += 1

            return (total, count)

        ans = 0

        dfs(root)

        return ans
