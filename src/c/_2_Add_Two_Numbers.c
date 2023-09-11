struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *dummy;
    dummy->val = 0;
    dummy->next = NULL;
    struct ListNode *curr = dummy;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry == 1)
    {
        int sum = 0;
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
        struct ListNode *temp = (struct Listnode *)malloc(sizeof(struct ListNode));
        temp->val = sum % 10;
        temp->next = NULL;
        curr->next = temp;
        curr = curr->next;
    }
}
