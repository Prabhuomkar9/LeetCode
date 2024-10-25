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
    public int pairSum(ListNode head) {
        ListNode prev = null, slow = head, fast = head;

        while (fast != null) {
            fast = fast.next.next;
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }

        int maxSum = 0;

        while (slow != null) {
            if (slow.val + prev.val > maxSum)
                maxSum = slow.val + prev.val;
            slow = slow.next;
            prev = prev.next;
        }

        System.gc();

        return maxSum;
    }
}
