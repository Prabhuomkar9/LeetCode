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
    public ListNode deleteMiddle(ListNode head) {
        ListNode dummy = new ListNode(0, head), tail = dummy;

        while (head != null && head.next != null) {
            tail = tail.next;
            head = head.next.next;
        }

        tail.next = tail.next.next;

        return dummy.next;
    }
}
