/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first = new ListNode(0), curr = first;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            carry += l1 != null ? l1.val : 0;
            carry += l2 != null ? l2.val : 0;

            curr.next = new ListNode(carry % 10);
            curr = curr.next;

            carry /= 10;

            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }

        return first.next;
    }
}
