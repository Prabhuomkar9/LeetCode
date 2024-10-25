/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *swapPairs(struct ListNode *head)
{
    struct ListNode *prev = (struct ListNode *)malloc(sizeof(struct ListNode)), *res = prev, *curr = head, *next;
    prev->next = head;

    while (curr != NULL && curr->next != NULL)
    {
        next = curr->next->next;
        curr->next->next = curr;
        prev->next = curr->next;
        curr->next = next;
        prev = curr;
        curr = prev->next;
    }

    return res->next;
}
