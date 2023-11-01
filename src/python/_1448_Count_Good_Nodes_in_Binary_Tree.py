# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            good = 0

            if node.val >= maxVal:
                good += 1
                maxVal = node.val

            if node.left:
                good += dfs(node.left, maxVal)

            if node.right:
                good += dfs(node.right, maxVal)

            return good

        return dfs(root, root.val)
