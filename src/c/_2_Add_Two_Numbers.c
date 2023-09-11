#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

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

int main(int argc, char const *argv[])
{
    struct ListNode l13, l12, l1, l23, l22, l2;
    l23.val = 4;
    l22.val = 6;
    l22.next = &l23;
    l2.val = 5;
    l2.next = &l22;
    l13.val = 3;
    l12.val = 4;
    l12.next = &l13;
    l1.val = 2;
    l1.next = &l12;
    struct ListNode *ans = addTwoNumbers(&l1, &l2);
    return 0;
}
