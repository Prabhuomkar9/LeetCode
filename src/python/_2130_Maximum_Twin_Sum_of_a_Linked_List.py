# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = head
        fast = head

        while fast:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        maxSum = 0

        while slow:
            maxSum = max(maxSum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return maxSum
