#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Determines whether a singly-linked list contains a cycle.
 * @list: A pointer to a singly-linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *slows, *fast;

    if (list == NULL || list->next == NULL)
        return 0;

    slows = list->next;
    fast = list->next->next;

    for (; slows && fast && fast->next; slows = slows->next, fast = fast->next->next)
    {
        if (slows == fast)
            return 1;
    }

    return 0;
}
