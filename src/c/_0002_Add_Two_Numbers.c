/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *first = (struct ListNode *)malloc(sizeof(struct ListNode));
    first->val = 0;
    first->next = NULL;
    struct ListNode *point = first;
    int sum = 0, carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0)
    {
        if (l1 != NULL)
        {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL)
        {
            sum += l2->val;
            l2 = l2->next;
        }
        sum += carry;
        carry = sum / 10;
        struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        newNode->val = sum % 10;
        newNode->next = NULL;
        point->next = newNode;
        point = point->next;
        sum = 0;
    }
    return first->next;
}
