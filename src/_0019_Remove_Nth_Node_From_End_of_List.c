/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{
    struct ListNode *temp = head;
    int count = 1;
    while (temp->next != NULL)
    {
        temp = temp->next;
        count++;
    }
    if (count == n)
        return head->next;
    temp = head;
    for (int i = 0; i < count - n - 1; i++)
        temp = temp->next;
    temp->next = temp->next->next;
    return head;
}
