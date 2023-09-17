/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *mergeTwoLists(struct ListNode *list1, struct ListNode *list2)
{
    struct ListNode *ans, *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
    temp->val = 0;
    temp->next = NULL;
    ans = temp;
    while (list1 || list2)
    {
        if (!list1)
        {
            temp->next = list2;
            break;
        }
        else if (!list2)
        {
            temp->next = list1;
            break;
        }
        else
        {
            if (list1->val < list2->val)
            {
                temp->next = list1;
                temp = temp->next;
                list1 = list1->next;
            }
            else
            {
                temp->next = list2;
                temp = temp->next;
                list2 = list2->next;
            }
        }
    }
    return ans->next;
}
