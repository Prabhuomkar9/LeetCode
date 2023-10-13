# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = prev = ListNode(0, head)
        curr = head

        while curr and curr.next:
            next = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = next
            prev = curr
            curr = prev.next

        return res.next
