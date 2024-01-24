# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, seen):
            seen[root.val] += 1
            if not root.left and not root.right:
                odd = 0
                for v in seen.values():
                    if v % 2 == 1:
                        odd += 1

                seen[root.val] -= 1
                if odd == 0 or odd == 1:
                    return 1
                else:
                    return 0

            ans = 0
            if root.left:
                ans = dfs(root.left, seen)

            if root.right:
                ans += dfs(root.right, seen)

            seen[root.val] -= 1

            return ans

        return dfs(root, defaultdict(int))
