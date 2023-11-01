# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque([root] if root else [])
        maxLevel = currLevel = 1
        maxSum = float("-inf")

        while dq:
            currSum = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                currSum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            if currSum > maxSum:
                maxSum = currSum
                maxLevel = currLevel

            currLevel += 1

        return maxLevel
