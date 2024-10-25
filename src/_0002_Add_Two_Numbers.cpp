/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *start = new ListNode(), *curr = start;
        int carry = 0;

        while (l1 || l2 || carry)
        {
            carry += l1 != NULL ? l1->val : 0;
            carry += l2 != NULL ? l2->val : 0;

            curr->next = new ListNode(carry % 10);
            curr = curr->next;

            carry /= 10;

            l1 = l1 != NULL ? l1->next : NULL;
            l2 = l2 != NULL ? l2->next : NULL;
        }

        return start->next;
    }
};
