/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    if (headA == NULL || headB == NULL)
        return NULL;

    struct ListNode *a = headA, *b = headB;

    while (a != b)
    {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }

    return a;
}
