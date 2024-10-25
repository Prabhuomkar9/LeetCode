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
    public ListNode swapPairs(ListNode head) {
        ListNode prev = new ListNode(0, head), res = prev, curr = head, next;

        while (curr != null && curr.next != null) {
            next = curr.next.next;
            curr.next.next = curr;
            prev.next = curr.next;
            curr.next = next;
            prev = curr;
            curr = prev.next;
        }

        return res.next;
    }
}
