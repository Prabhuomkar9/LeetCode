# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen = defaultdict(int)

        def dfs(node):
            if not node:
                return

            seen[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        mode = max(seen.values())

        return [key for key, val in seen.items() if val == mode]
