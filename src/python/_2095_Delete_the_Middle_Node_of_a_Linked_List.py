# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        while head and head.next:
            tail = tail.next
            head = head.next.next

        tail.next = tail.next.next

        return dummy.next
