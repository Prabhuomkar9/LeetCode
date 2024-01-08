# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        dq = deque([root])

        while dq:
            node = dq.popleft()
            if node.left and low < node.val:
                dq.append(node.left)
            if node.right and node.val < high:
                dq.append(node.right)

            if low <= node.val <= high:
                ans += node.val

        return ans
