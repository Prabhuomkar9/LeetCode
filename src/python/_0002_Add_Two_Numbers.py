# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        first = temp = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            carry += l1.val if l1 else 0
            carry += l2.val if l2 else 0

            temp.next = ListNode(carry % 10)
            temp = temp.next

            carry //= 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return first.next
