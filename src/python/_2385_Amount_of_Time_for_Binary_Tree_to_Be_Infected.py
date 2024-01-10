# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)

        dq = [(None, root)]

        while dq:
            u, v = dq.pop()

            if u:
                graph[u.val].add(v.val)
                graph[v.val].add(u.val)

            if v.left:
                dq.append((v, v.left))

            if v.right:
                dq.append((v, v.right))

        ans = -1
        dq = deque([start])
        seen = set()

        while dq:
            size = len(dq)

            for _ in range(size):
                u = dq.popleft()

                for v in graph[u]:
                    if v not in seen:
                        dq.append(v)

                seen.add(u)

            ans += 1

        return ans
