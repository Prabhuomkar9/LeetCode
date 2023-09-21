# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Easy to understand
        allListValues = []
        head = ptr = ListNode()

        while list1 or list2:
            if list1:
                allListValues.append(list1.val)
                list1 = list1.next

            if list2:
                allListValues.append(list2.val)
                list2 = list2.next

        allListValues.sort()

        for val in allListValues:
            ptr.next = ListNode(val)
            ptr = ptr.next

        return head.next


class Solution:
    # Iteration
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ptr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next

        ptr.next = list1 or list2

        return head.next


class Solution:
    # Recursion
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not (list1 and list2):
            return list1 or list2

        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)

        lil.next = self.mergeTwoLists(lil.next, big)

        return lil
